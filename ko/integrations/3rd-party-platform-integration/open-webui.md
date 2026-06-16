# Open WebUI

[Open WebUI](https://github.com/open-webui/open-webui)는 완전한 오프라인 운영을 위해 설계된 확장 가능하고 기능이 풍부하며 사용자 친화적인 _셀프 호스팅 AI 플랫폼_입니다.

[Functions](https://docs.openwebui.com/features/plugin/functions/)는 Open WebUI를 위한 플러그인과 같습니다. Flowise Prediction API를 호출하여 입력을 처리하고 응답을 생성한 후 사용자에게 결과를 반환하는 커스텀 [Pipe Function](https://docs.openwebui.com/features/plugin/functions/pipe)을 만들 수 있습니다. 이를 통해 Flowise를 Open WebUI에서 사용할 수 있습니다.

## 설정

1. 먼저 Open WebUI를 실행 중이어야 합니다. [Quickstart](https://docs.openwebui.com/getting-started/quick-start/) 가이드를 참조할 수 있습니다. 좌측 하단에서 프로필을 클릭하고 **Admin Panel**을 클릭하세요.

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt="" width="235"><figcaption></figcaption></figure>

2. **Functions** 탭을 열고 새로운 Function을 추가하세요.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1).png" alt="" width="423"><figcaption></figcaption></figure>

3. Function에 이름을 지정하고 다음 코드를 추가하세요:

```python
"""
title: Flowise Integration for OpenWebUI
Requirements:
  - Flowise API URL (set via FLOWISE_API_URL)
  - Flowise API Key (set via FLOWISE_API_KEY)
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List, Union, Generator, Iterator
import requests
import json
import os


class Pipe:
    class Valves(BaseModel):
        flowise_url: str = Field(
            default=os.getenv("FLOWISE_API_URL", ""),
            description="Flowise URL",
        )
        flowise_api_key: str = Field(
            default=os.getenv("FLOWISE_API_KEY", ""),
            description="Flowise API key for authentication",
        )

    def __init__(self):
        self.type = "manifold"
        self.id = "flowise_chat"
        self.valves = self.Valves()

        # Validate required settings
        if not self.valves.flowise_url:
            print(
                "⚠️ Please set your Flowise URL using the FLOWISE_API_URL environment variable"
            )
        if not self.valves.flowise_api_key:
            print(
                "⚠️ Please set your Flowise API key using the FLOWISE_API_KEY environment variable"
            )

    def pipes(self):
        if self.valves.flowise_api_key and self.valves.flowise_url:
            try:
                headers = {
                    "Authorization": f"Bearer {self.valves.flowise_api_key}",
                    "Content-Type": "application/json",
                }

                r = requests.get(
                    f"{self.valves.flowise_url}/api/v1/chatflows?type=AGENTFLOW",
                    headers=headers,
                )
                models = r.json()
                return [
                    {
                        "id": model["id"],
                        "name": model["name"],
                    }
                    for model in models
                ]

            except Exception as e:
                return [
                    {
                        "id": "error",
                        "name": str(e),
                    },
                ]
        else:
            return [
                {
                    "id": "error",
                    "name": "API Key not provided.",
                },
            ]

    def _process_message_content(self, message: dict) -> str:
        """Process message content, handling text for now"""
        if isinstance(message.get("content"), list):
            processed_content = []
            for item in message["content"]:
                if item["type"] == "text":
                    processed_content.append(item["text"])
            return " ".join(processed_content)
        return message.get("content", "")

    def pipe(
        self, body: dict, __user__: Optional[dict] = None, __metadata__: dict = None
    ):
        try:
            stream_enabled = body.get("stream", True)
            session_id = (__metadata__ or {}).get("chat_id") or "owui-session"
            # model can be "flowise.<id>" or just "<id>"
            model_name = body.get("model", "")
            dot = model_name.find(".")
            model_id = model_name[dot + 1 :] if dot != -1 else model_name

            messages = body.get("messages") or []
            if not messages:
                raise Exception("No messages found in request body")
            question = self._process_message_content(messages[-1])

            data = {
                "question": question,
                "overrideConfig": {"sessionId": session_id},
                "streaming": stream_enabled,
            }

            headers = {
                "Authorization": f"Bearer {self.valves.flowise_api_key}",
                "Content-Type": "application/json",
                "Accept": "text/event-stream" if stream_enabled else "application/json",
            }

            url = f"{self.valves.flowise_url}/api/v1/prediction/{model_id}"
            with requests.post(
                url, json=data, headers=headers, stream=stream_enabled, timeout=60
            ) as r:
                r.raise_for_status()

                if stream_enabled:
                    # Ensure correct decoding for SSE (prevents â€™ etc.)
                    r.encoding = "utf-8"

                    for raw_line in r.iter_lines(decode_unicode=True):
                        if not raw_line:
                            continue
                        line = raw_line.strip()

                        # Skip keep-alives or non-data fields
                        if not line.startswith("data:"):
                            continue

                        payload = line[5:].strip()
                        if payload in ("[DONE]", '"[DONE]"'):
                            break

                        # Flowise usually sends {"event":"token","data":"..."}
                        try:
                            obj = json.loads(payload)
                        except json.JSONDecodeError:
                            # Occasionally plain text arrives—stream it anyway
                            if payload:
                                yield payload
                            continue

                        if isinstance(obj, dict):
                            if obj.get("event") == "token":
                                token = obj.get("data") or ""
                                if token:
                                    yield token
                            else:
                                # Some versions send {"data":{"text":"..."}}
                                data_field = obj.get("data")
                                if isinstance(data_field, dict):
                                    text = data_field.get("text")
                                    if text:
                                        yield text
                    return  # end streaming

                # Non-streaming fallback
                resp = r.json()
                return (
                    resp.get("text") or (resp.get("data") or {}).get("text", "") or ""
                )

        except requests.HTTPError as http_err:
            try:
                detail = http_err.response.text[:500]
            except Exception:
                detail = ""
            return f"HTTP error from Flowise: {http_err.response.status_code} {detail}"
        except Exception as e:
            return f"Error in Flowise pipe: {e}"
```

4. Function이 저장되면 활성화하고 설정 버튼을 클릭하여 Flowise URL과 Flowise API 키를 입력하세요:

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt="" width="431"><figcaption></figcaption></figure>

5. 새로고침 후 새 채팅을 클릭하면 flows 목록을 볼 수 있습니다. 코드를 수정하여 다음을 표시할 수 있습니다:

* Agentflows V2만: `f"{self.valves.flowise_url}/api/v1/chatflows?type=AGENTFLOW"`
* Chatflows만: `f"{self.valves.flowise_url}/api/v1/chatflows?type=CHATFLOW"`
* Assistants만: `f"{self.valves.flowise_url}/api/v1/chatflows?type=ASSISTANT"`

<figure><img src="../../.gitbook/assets/image (4) (1) (1).png" alt=""><figcaption></figcaption></figure>

6. 테스트:

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>
