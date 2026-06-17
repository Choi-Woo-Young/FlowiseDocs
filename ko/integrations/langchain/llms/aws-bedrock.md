---
description: AWS Bedrock 대형 언어 모델을 래핑합니다.
---

# AWS Bedrock

**AWS Bedrock LLM** 노드는 Generative AI 애플리케이션을 구축하기 위한 기초 모델에 대한 액세스를 제공하는 관리 서비스인 Amazon Bedrock과 통합됩니다.

Flowise에서 AWS Bedrock을 사용하려면 **AWS Bedrock LLM** 노드를 Chatflow에 추가하세요.

# 설정

1. Flowise에 대해 AWS 자격증명을 구성하세요.

Amazon Bedrock에서 Flowise와 함께 사용하려는 모델에 대한 액세스 권한이 있는지 확인하세요.

2. AWS Bedrock 노드를 Chatflow에 추가하세요.

Flowise 캔버스에서 AWS Bedrock LLM 노드를 Chatflow로 드래그하여 놓으세요.

3. AWS Bedrock 입력을 구성하세요:
<figure><img src="../../../.gitbook/assets/image (2) (5).png" alt="" width="275"><figcaption><p>AWS Bedrock Node</p></figcaption></figure>

* AWS Credential: 기존 AWS 자격증명을 선택하거나 새로 생성하세요. 관련 IAM 사용자 또는 역할은 `bedrock:InvokeModel` 및 Chatflow의 다른 필수 AWS 서비스에 대한 권한이 있어야 합니다.
* Region: Bedrock 모델을 사용할 수 있는 AWS 지역입니다.
* Model Name: 대화형 AI를 위한 AWS Bedrock 기초 모델입니다.

4. AWS Bedrock 노드를 Chatflow에 연결하세요.

다른 Chatflow 컴포넌트(입력 노드, 출력 노드, 메모리 노드 등)를 추가한 후 AWS Bedrock LLM 노드를 적절한 컴포넌트에 연결하여 Chatflow를 생성하세요.

AWS에 Flowise를 배포하는 것에 대한 정보는 [AWS](../../../configuration/deployment/aws.md)를 참조하세요.

