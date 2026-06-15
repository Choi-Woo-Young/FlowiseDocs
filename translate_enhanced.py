#!/usr/bin/env python3
"""
Enhanced Flowise Documentation Translator - English to Korean
Comprehensive translation dictionary with better sentence-level translation
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, Tuple


# Enhanced comprehensive Korean translation dictionary
TRANSLATION_DICT = {
    # Section headings and major terms
    'Table of contents': '목차',
    'Introduction': '소개',
    'Get Started': '시작하기',
    'Contribution Guide': '기여 가이드',
    'Building Node': '노드 구축',
    'API Reference': 'API 참고',
    'CLI Reference': 'CLI 참고',
    'Using Flowise': 'Flowise 사용',
    'Configuration': '구성',
    'Integrations': '통합',

    # Specific section names
    'Assistants': '어시스턴트',
    'Attachments': '첨부파일',
    'Chat Message': '채팅 메시지',
    'Chatflows': '챗플로우',
    'Document Store': '문서 저장소',
    'Feedback': '피드백',
    'Leads': '리드',
    'Ping': '핑',
    'Prediction': '예측',
    'Tools': '도구',
    'Upsert History': 'Upsert 이력',
    'Variables': '변수',
    'Vector Upsert': '벡터 Upsert',

    # Using Flowise sections
    'Agentflow V2': 'Agentflow V2',
    'Agentflow V1 (Deprecating)': 'Agentflow V1 (지원 중단)',
    'Multi-Agents': '다중 에이전트',
    'Sequential Agents': '순차 에이전트',
    'Video Tutorials': '비디오 튜토리얼',
    'Streaming': '스트리밍',
    'Document Stores': '문서 저장소',
    'Upsertion': 'Upsert',
    'Analytic': '분석',
    'Monitoring': '모니터링',
    'Embed': '임베드',
    'Uploads': '업로드',
    'Workspaces': '작업 공간',
    'Evaluations': '평가',

    # Analytics
    'Arize': 'Arize',
    'LangWatch': 'LangWatch',
    'Langfuse': 'Langfuse',
    'Lunary': 'Lunary',
    'Opik': 'Opik',
    'Phoenix': 'Phoenix',

    # Configuration items
    'Auth': '인증',
    'Application': '애플리케이션',
    'Flows': '플로우',
    'Databases': '데이터베이스',
    'Deployment': '배포',
    'AWS': 'AWS',
    'Azure': 'Azure',
    'GCP': 'GCP',
    'Hugging Face': 'Hugging Face',
    'Kubernetes using Helm': 'Helm을 사용한 Kubernetes',
    'Railway': 'Railway',
    'Render': 'Render',
    'Replit': 'Replit',
    'Sealos': 'Sealos',
    'Zeabur': 'Zeabur',
    'Environment Variables': '환경 변수',
    'Rate Limit': '레이트 제한',
    'SSO': 'SSO',
    'Running Flowise behind company proxy': '회사 프록시 뒤에서 Flowise 실행',
    'Running Flowise using Queue': '큐를 사용하여 Flowise 실행',
    'Running in Production': '프로덕션에서 실행',

    # LangChain specific
    'LangChain': 'LangChain',
    'Agents': '에이전트',
    'Airtable Agent': 'Airtable 에이전트',
    'Airtable Agent Functionality': 'Airtable 에이전트 기능',
    'AutoGPT': 'AutoGPT',
    'BabyAGI': 'BabyAGI',
    'CSV Agent': 'CSV 에이전트',
    'Conversational Agent': '대화형 에이전트',
    'Conversational Retrieval Agent': '대화형 검색 에이전트',
    'MistralAI Tool Agent': 'MistralAI 도구 에이전트',
    'OpenAI Assistant': 'OpenAI 어시스턴트',
    'Threads': '스레드',
    'OpenAI Function Agent': 'OpenAI 함수 에이전트',
    'OpenAI Tool Agent': 'OpenAI 도구 에이전트',
    'ReAct Agent Chat': 'ReAct 에이전트 채팅',
    'ReAct Agent LLM': 'ReAct 에이전트 LLM',
    'Tool Agent': '도구 에이전트',
    'XML Agent': 'XML 에이전트',

    # Cache related
    'Cache': '캐시',
    'InMemory Cache': '메모리 내 캐시',
    'InMemory Embedding Cache': '메모리 내 임베딩 캐시',
    'Momento Cache': 'Momento 캐시',
    'Redis Cache': 'Redis 캐시',
    'Redis Embeddings Cache': 'Redis 임베딩 캐시',
    'Upstash Redis Cache': 'Upstash Redis 캐시',

    # Chains
    'Chains': '체인',
    'GET API Chain': 'GET API 체인',
    'OpenAPI Chain': 'OpenAPI 체인',
    'POST API Chain': 'POST API 체인',
    'Conversation Chain': '대화 체인',
    'Conversational Retrieval QA Chain': '대화형 검색 QA 체인',
    'LLM Chain': 'LLM 체인',
    'Multi Prompt Chain': '다중 프롬프트 체인',
    'Multi Retrieval QA Chain': '다중 검색 QA 체인',
    'Retrieval QA Chain': '검색 QA 체인',
    'SQL Database Chain': 'SQL 데이터베이스 체인',
    'VectorDB QA Chain': 'VectorDB QA 체인',

    # Chat Models
    'Chat Models': '채팅 모델',
    'AWS ChatBedrock': 'AWS ChatBedrock',
    'Azure ChatOpenAI': 'Azure ChatOpenAI',
    'Chat Fireworks': 'Chat Fireworks',
    'Chat SambaNova': 'Chat SambaNova',
    'ChatAnthropic': 'ChatAnthropic',
    'ChatCohere': 'ChatCohere',
    'ChatCometAPI': 'ChatCometAPI',
    'ChatHuggingFace': 'ChatHuggingFace',

    # Common structural terms
    'Inputs': '입력',
    'Input': '입력',
    'Outputs': '출력',
    'Output': '출력',
    'Functionality': '기능',
    'Description': '설명',
    'Parameters': '매개변수',
    'Parameter': '매개변수',
    'Required': '필수',
    'Optional': '선택사항',
    'Note': '참고',
    'Notes': '참고사항',
    'Example': '예시',
    'Examples': '예시',
    'Usage': '사용법',
    'Installation': '설치',
    'Setup': '설정',
    'Features': '기능',
    'Feature': '기능',
    'Benefits': '이점',
    'Benefit': '이점',
    'Limitations': '제한사항',
    'Limitation': '제한사항',
    'Troubleshooting': '문제 해결',
    'FAQ': '자주 묻는 질문',
    'See Also': '참고 항목',
    'References': '참고자료',
    'Related': '관련',
    'Additional': '추가',

    # Common sentence fragments (longer phrases for better translation)
    'Agent used to answer queries': '쿼리에 답변하는 데 사용되는 에이전트',
    'is designed to facilitate': '를 촉진하기 위해 설계되었습니다',
    'enables users to': '사용자가 할 수 있도록 합니다',
    'can be used to': '에 사용할 수 있습니다',
    'can be particularly useful for': '특히 다음에 유용할 수 있습니다',
    'helps users get insights': '사용자가 인사이트를 얻도록 도와줍니다',
    'making it easier to': '더 쉽게 할 수 있게 해줍니다',
    'without needing to': '할 필요 없이',
    'This is a required field': '필수 필드입니다',
    'This is also a required field': '필수 필드입니다',
    'This option allows users': '이 옵션은 사용자가',
    'This input is required': '이 입력은 필수입니다',
    'Optional input': '선택사항 입력',
    'Required input': '필수 입력',
    'for more information': '자세한 내용은',
    'If enabled': '활성화된 경우',
    'If your': '당신의',
    'It is used to': '는 다음을 위해 사용됩니다',
    'is used to specify': '를 지정하기 위해 사용됩니다',
    'helps the agent': '에이전트가 도움이 됩니다',
    'The default value': '기본값은',
    'by using this agent': '이 에이전트를 사용하여',
    'For example': '예를 들어',

    # Individual common words (for fallback)
    'the': '그',
    'a': '한',
    'an': '한',
    'and': '그리고',
    'or': '또는',
    'to': '에',
    'for': '위해',
    'in': '에서',
    'of': '의',
    'with': '함께',
    'from': '에서',
    'that': '그',
    'which': '어느',
    'this': '이',
    'is': '입니다',
    'are': '입니다',
    'be': '있다',
    'being': '되고',
    'have': '가지고',
    'has': '가지고',
    'by': '에 의해',
}


class MarkdownPreserver:
    """Preserve code blocks, URLs, and special syntax during translation"""

    def __init__(self):
        self.preserved = {}
        self.counter = 0

    def preserve(self, content: str, pattern: str, name: str) -> str:
        """Replace matches with placeholders"""
        def replace_match(match):
            placeholder = f"__PRESERVE_{name}_{self.counter}__"
            self.preserved[placeholder] = match.group(0)
            self.counter += 1
            return placeholder

        return re.sub(pattern, replace_match, content, flags=re.MULTILINE | re.DOTALL)

    def preserve_all(self, content: str) -> str:
        """Preserve all non-translatable content"""
        # YAML frontmatter
        content = self.preserve(content, r'^---\n[\s\S]*?\n---\n', 'YAML')

        # Code blocks
        content = self.preserve(content, r'```[\s\S]*?```', 'CODE')

        # Inline code
        content = self.preserve(content, r'`[^`\n]+`', 'INLINE')

        # URLs
        content = self.preserve(content, r'https?://[^\s\)]+', 'URL')

        # HTML tags and GitBook syntax
        content = self.preserve(content, r'<[^>]+>', 'HTML')
        content = self.preserve(content, r'{%[^%]*%}', 'GITBOOK')

        # Images and markdown links
        content = self.preserve(content, r'!\[[^\]]*\]\([^\)]+\)', 'IMAGE')
        content = self.preserve(content, r'\[[^\]]+\]\([^\)]+\)', 'LINK')

        return content

    def restore(self, content: str) -> str:
        """Restore preserved content"""
        for placeholder, original in self.preserved.items():
            content = content.replace(placeholder, original)
        return content


class TextTranslator:
    """Translate text to Korean using comprehensive dictionary"""

    @staticmethod
    def translate_phrase(phrase: str) -> str:
        """Translate a phrase, prioritizing longer matches"""
        if not phrase or not phrase.strip():
            return phrase

        phrase_original = phrase
        phrase_lower = phrase.lower()

        # Find longest matching phrase in dictionary
        longest_match = ""
        longest_value = ""

        for key, value in sorted(TRANSLATION_DICT.items(), key=lambda x: len(x[0]), reverse=True):
            if key.lower() in phrase_lower:
                if len(key) > len(longest_match):
                    longest_match = key
                    longest_value = value

        # If we found a match, replace it
        if longest_match:
            # Case-insensitive replacement
            pattern = re.compile(re.escape(longest_match), re.IGNORECASE)
            result = pattern.sub(longest_value, phrase_original, count=1)
            return result

        return phrase

    @staticmethod
    def translate_line(line: str) -> str:
        """Translate a single line intelligently"""
        if not line or not line.strip():
            return line

        # For headings - translate the entire heading
        heading_match = re.match(r'^(#+\s+)(.+)$', line)
        if heading_match:
            prefix = heading_match.group(1)
            heading_text = heading_match.group(2)
            translated_heading = TextTranslator.translate_phrase(heading_text)
            return prefix + translated_heading

        # For bullet points
        bullet_match = re.match(r'^(\s*[\*\-\+]\s+)(.*?)(\s*)$', line)
        if bullet_match:
            indent_prefix = bullet_match.group(1)
            content = bullet_match.group(2)
            trailing = bullet_match.group(3)
            # Only translate if there's actual content
            if content.strip():
                translated_content = TextTranslator.translate_phrase(content)
                return indent_prefix + translated_content + trailing
            return line

        # For numbered lists
        num_match = re.match(r'^(\s*\d+\.\s+)(.*?)(\s*)$', line)
        if num_match:
            indent_prefix = num_match.group(1)
            content = num_match.group(2)
            trailing = num_match.group(3)
            if content.strip():
                translated_content = TextTranslator.translate_phrase(content)
                return indent_prefix + translated_content + trailing
            return line

        # For regular paragraphs - only translate substantial content
        if line.strip() and not re.match(r'^[\s\-\*\|]', line):
            # Only translate if line is not mostly preserved content
            translated_line = TextTranslator.translate_phrase(line)
            return translated_line

        return line


def translate_file(source_path: str, target_path: str) -> Tuple[bool, str]:
    """Translate a markdown file"""
    try:
        # Read source
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Preserve special content
        preserv = MarkdownPreserver()
        preserved_content = preserv.preserve_all(content)

        # Translate line by line
        lines = preserved_content.split('\n')
        translated_lines = [TextTranslator.translate_line(line) for line in lines]
        translated_content = '\n'.join(translated_lines)

        # Restore preserved content
        translated_content = preserv.restore(translated_content)

        # Create target directory
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        # Write translated file
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True, f"✓ {Path(source_path).relative_to('/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en')}"

    except Exception as e:
        return False, f"✗ {str(e)[:60]}"


def main():
    """Main translation script"""
    source_base = Path('/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en')
    target_base = Path('/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko')

    files_to_translate = [
        'SUMMARY.md',
        'api-reference/chatflows.md',
        'api-reference/document-store.md',
        'api-reference/feedback.md',
        'api-reference/leads.md',
        'api-reference/ping.md',
        'api-reference/prediction.md',
        'api-reference/tools.md',
        'api-reference/upsert-history.md',
        'api-reference/variables.md',
        'api-reference/vector-upsert.md',
        'integrations/langchain/agents/airtable-agent.md',
        'integrations/langchain/agents/autogpt.md',
        'integrations/langchain/agents/babyagi.md',
        'integrations/langchain/agents/conversational-agent.md',
        'integrations/langchain/agents/conversational-retrieval-agent.md',
        'integrations/langchain/agents/mistralai-tool-agent.md',
        'integrations/langchain/agents/openai-assistant/threads.md',
        'integrations/langchain/agents/openai-function-agent.md',
        'integrations/langchain/agents/openai-tool-agent.md',
        'integrations/langchain/agents/react-agent-chat.md',
        'integrations/langchain/agents/react-agent-llm.md',
        'integrations/langchain/agents/tool-agent.md',
        'integrations/langchain/agents/xml-agent.md',
        'integrations/langchain/cache/in-memory-cache.md',
        'integrations/langchain/cache/inmemory-embedding-cache.md',
        'integrations/langchain/cache/momento-cache.md',
        'integrations/langchain/cache/redis-cache.md',
        'integrations/langchain/cache/redis-embeddings-cache.md',
        'integrations/langchain/cache/upstash-redis-cache.md',
        'integrations/langchain/chains/conversation-chain.md',
        'integrations/langchain/chains/conversational-retrieval-qa-chain.md',
        'integrations/langchain/chains/get-api-chain.md',
        'integrations/langchain/chains/llm-chain.md',
        'integrations/langchain/chains/multi-prompt-chain.md',
        'integrations/langchain/chains/multi-retrieval-qa-chain.md',
        'integrations/langchain/chains/openapi-chain.md',
        'integrations/langchain/chains/post-api-chain.md',
        'integrations/langchain/chains/retrieval-qa-chain.md',
        'integrations/langchain/chains/sql-database-chain.md',
        'integrations/langchain/chains/vectordb-qa-chain.md',
        'integrations/langchain/chat-models/aws-chatbedrock.md',
        'integrations/langchain/chat-models/azure-chatopenai-1.md',
        'integrations/langchain/chat-models/chat-fireworks.md',
        'integrations/langchain/chat-models/chat-sambanova.md',
        'integrations/langchain/chat-models/chatanthropic.md',
        'integrations/langchain/chat-models/chatcohere.md',
        'integrations/langchain/chat-models/chatcometapi.md',
        'integrations/langchain/chat-models/chathuggingface.md',
    ]

    print("=" * 75)
    print("Flowise Documentation Translator (English → Korean)")
    print("=" * 75)
    print(f"Source: {source_base}")
    print(f"Target: {target_base}")
    print(f"Files: {len(files_to_translate)}\n")

    successful = 0
    failed = 0
    failed_files = []

    for i, file_path in enumerate(files_to_translate, 1):
        source_file = source_base / file_path
        target_file = target_base / file_path

        if not source_file.exists():
            print(f"[{i:2d}/{len(files_to_translate)}] ✗ {file_path} (not found)")
            failed += 1
            failed_files.append(file_path)
            continue

        success, message = translate_file(str(source_file), str(target_file))

        print(f"[{i:2d}/{len(files_to_translate)}] {message}")

        if success:
            successful += 1
        else:
            failed += 1
            failed_files.append(file_path)

    # Summary
    print("\n" + "=" * 75)
    print("Summary")
    print("=" * 75)
    print(f"Total:     {len(files_to_translate)}")
    print(f"Successful: {successful}")
    print(f"Failed:     {failed}")
    print(f"Success rate: {successful/len(files_to_translate)*100:.1f}%")

    if failed_files:
        print(f"\nFailed files ({len(failed_files)}):")
        for f in failed_files:
            print(f"  - {f}")

    # Verify output
    print(f"\nVerifying Korean files:")
    ko_files = list(target_base.glob('**/*.md'))
    print(f"Total Korean markdown files: {len(ko_files)}")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
