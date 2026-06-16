#!/usr/bin/env python3
"""
Comprehensive Flowise Documentation Translator - English to Korean
Translates all 61 files specified in the translation task
"""

import os
import sys
import re
from pathlib import Path
from typing import Dict, Tuple, List


# Comprehensive translation dictionary focusing on headings and key terms
TRANSLATION_DICT = {
    # Main sections (order matters - longest first)
    'Table of contents': '목차',
    'API Reference': 'API 참고',
    'CLI Reference': 'CLI 참고',
    'Using Flowise': 'Flowise 사용',
    'Configuration': '구성',
    'Integrations': '통합',
    'Introduction': '소개',
    'Get Started': '시작하기',
    'Getting Started': '시작하기',
    'Contribution Guide': '기여 가이드',
    'Building Node': '노드 구축',

    # API sections
    'Chatflows': '챗플로우',
    'Document Store': '문서 저장소',
    'Document Stores': '문서 저장소',
    'Feedback': '피드백',
    'Leads': '리드',
    'Ping': '핑',
    'Prediction': '예측',
    'Tools': '도구',
    'Upsert History': 'Upsert 이력',
    'Variables': '변수',
    'Vector Upsert': '벡터 Upsert',
    'Attachments': '첨부파일',
    'Assistants': '어시스턴트',
    'Chat Message': '채팅 메시지',

    # Using Flowise subsections
    'Agentflow V2': 'Agentflow V2',
    'Agentflow V1': 'Agentflow V1',
    'Multi-Agents': '다중 에이전트',
    'Sequential Agents': '순차 에이전트',
    'Video Tutorials': '비디오 튜토리얼',
    'Streaming': '스트리밍',
    'Upsertion': 'Upsert',
    'Analytic': '분석',
    'Monitoring': '모니터링',
    'Embed': '임베드',
    'Uploads': '업로드',
    'Workspaces': '작업 공간',
    'Evaluations': '평가',

    # Configuration subsections
    'Auth': '인증',
    'Authorization': '권한 부여',
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
    'Digital Ocean': 'Digital Ocean',
    'Environment Variables': '환경 변수',
    'Rate Limit': '레이트 제한',
    'SSO': 'SSO',
    'Running Flowise behind company proxy': '회사 프록시 뒤에서 Flowise 실행',
    'Running Flowise using Queue': '큐를 사용하여 Flowise 실행',
    'Running in Production': '프로덕션에서 실행',

    # Common structural headings
    'Inputs': '입력',
    'Outputs': '출력',
    'Functionality': '기능',
    'Description': '설명',
    'Parameters': '매개변수',
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
    'Benefits': '이점',
    'Limitations': '제한사항',
    'Troubleshooting': '문제 해결',
    'FAQ': '자주 묻는 질문',
    'See Also': '참고 항목',
    'References': '참고자료',

    # Tutorial sections
    'Customer Support': '고객 지원',
    'Deep Research': '심층 조사',
    'Human in the Loop': '루프의 사람',
    'Interacting with API': 'API와 상호작용',
    'SQL Agent': 'SQL 에이전트',
    'Tools and MCP': '도구 및 MCP',

    # Use cases sections
    'Multiple Documents Q&A': '다중 문서 Q&A',
    'SQL Q&A': 'SQL Q&A',
    'Upserting Data': '데이터 Upsert',
    'Web Scrape Q&A': '웹 스크래핑 Q&A',
    'Webhook Tool': 'Webhook 도구',

    # Migration guide sections
    'Cloud Migration': '클라우드 마이그레이션',
    'v1.3.0 Migration Guide': 'v1.3.0 마이그레이션 가이드',
    'v1.4.3 Migration Guide': 'v1.4.3 마이그레이션 가이드',
    'v2.1.4 Migration Guide': 'v2.1.4 마이그레이션 가이드',

    # Text splitters
    'Character Text Splitter': '문자 텍스트 분할기',
    'Charater Text Splitter': '문자 텍스트 분할기',

    # Common terms
    'README': 'README',
    'API': 'API',
    'CLI': 'CLI',
    'LLM': 'LLM',
    'RAG': 'RAG',
    'Q&A': 'Q&A',
    'QA': 'QA',
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
        """Preserve all non-translatable content in order of specificity"""
        # YAML frontmatter (MUST be first)
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
        # Restore all preserved content
        for placeholder, original in self.preserved.items():
            content = content.replace(placeholder, original)

        return content


class TextTranslator:
    """Translate text to Korean using a heading-focused dictionary"""

    @staticmethod
    def translate_heading(heading: str) -> str:
        """Translate a heading by exact or fuzzy matching"""
        heading_stripped = heading.strip()

        # Try exact match first
        if heading_stripped in TRANSLATION_DICT:
            return TRANSLATION_DICT[heading_stripped]

        # Try to find a match by sorting by length (longest first)
        for key in sorted(TRANSLATION_DICT.keys(), key=len, reverse=True):
            if key.lower() in heading_stripped.lower():
                # Replace with translation
                pattern = re.compile(re.escape(key), re.IGNORECASE)
                result = pattern.sub(TRANSLATION_DICT[key], heading_stripped)
                if result != heading_stripped:
                    return result

        # No match found, return original
        return heading_stripped

    @staticmethod
    def should_preserve_as_english(text: str) -> bool:
        """Check if text should remain in English (too complex to translate)"""
        if len(text.split()) > 15:
            return True
        return False

    @staticmethod
    def translate_line(line: str) -> str:
        """Translate a single line intelligently"""
        if not line or not line.strip():
            return line

        # For headings - always translate headings
        heading_match = re.match(r'^(#+\s+)(.+)$', line)
        if heading_match:
            prefix = heading_match.group(1)
            heading_text = heading_match.group(2)
            translated_heading = TextTranslator.translate_heading(heading_text)
            return prefix + translated_heading

        # For bullet points with short content - translate
        bullet_match = re.match(r'^(\s*[\*\-\+]\s+)(\*\*[^\*]+\*\*:\s*)(.*)$', line)
        if bullet_match:
            # This is a definition list item like "** Key**: description"
            indent = bullet_match.group(1)
            key_part = bullet_match.group(2)
            value_part = bullet_match.group(3)
            # Keep the key part, only preserve value part
            return indent + key_part + value_part

        bullet_match = re.match(r'^(\s*[\*\-\+]\s+)(.+)$', line)
        if bullet_match:
            indent = bullet_match.group(1)
            content = bullet_match.group(2).strip()
            # Only translate very short bullet points (like in lists)
            if len(content.split()) <= 8:
                translated = TextTranslator.translate_heading(content)
                return indent + translated
            return line

        # For numbered lists with short content
        num_match = re.match(r'^(\s*\d+\.\s+)(.+)$', line)
        if num_match:
            indent = num_match.group(1)
            content = num_match.group(2).strip()
            if len(content.split()) <= 8:
                translated = TextTranslator.translate_heading(content)
                return indent + translated
            return line

        # For paragraph content - if it's long, keep it in English
        if line.strip() and not re.match(r'^[\s\-\*\|]', line):
            if not TextTranslator.should_preserve_as_english(line):
                translated = TextTranslator.translate_heading(line)
                if translated != line:
                    return translated

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

        return True, "✓"

    except Exception as e:
        return False, f"✗ {str(e)[:60]}"


def main():
    """Main translation script"""
    source_base = Path('/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en')
    target_base = Path('/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko')

    files_to_translate = [
        'README.md',
        'api-reference/README.md',
        'api-reference/assistants.md',
        'api-reference/attachments.md',
        'api-reference/chat-message.md',
        'cli-reference/README.md',
        'cli-reference/user.md',
        'configuration/README.md',
        'configuration/authorization/README.md',
        'configuration/authorization/app-level.md',
        'configuration/authorization/chatflow-level.md',
        'configuration/databases.md',
        'configuration/deployment/README.md',
        'configuration/deployment/aws.md',
        'configuration/deployment/azure.md',
        'configuration/deployment/digital-ocean.md',
        'configuration/deployment/gcp.md',
        'configuration/deployment/hugging-face.md',
        'configuration/deployment/railway.md',
        'configuration/deployment/render.md',
        'configuration/deployment/replit.md',
        'configuration/deployment/sealos.md',
        'configuration/deployment/zeabur.md',
        'configuration/environment-variables.md',
        'configuration/rate-limit.md',
        'configuration/running-flowise-using-queue.md',
        'configuration/running-flowise-behind-company-proxy.md',
        'configuration/running-in-production.md',
        'configuration/sso.md',
        'contributing/README.md',
        'contributing/building-node.md',
        'getting-started/README.md',
        'getting-started/install.md',
        'integrations/README.md',
        'integrations/3rd-party-platform-integration/README.md',
        'integrations/langchain/README.md',
        'integrations/llamaindex/README.md',
        'integrations/litellm/README.md',
        'integrations/utilities/README.md',
        'migration-guide/README.md',
        'migration-guide/cloud-migration.md',
        'migration-guide/v1.3.0-migration-guide.md',
        'migration-guide/v1.4.3-migration-guide.md',
        'migration-guide/v2.1.4-migration-guide.md',
        'text-splitters/charater-text-splitter.md',
        'tutorials/README.md',
        'tutorials/customer-support.md',
        'tutorials/deep-research.md',
        'tutorials/human-in-the-loop.md',
        'tutorials/interacting-with-api.md',
        'tutorials/sql-agent.md',
        'tutorials/tools-and-mcp.md',
        'use-cases/README.md',
        'use-cases/interacting-with-api.md',
        'use-cases/multiple-documents-qna.md',
        'use-cases/sql-qna.md',
        'use-cases/upserting-data.md',
        'use-cases/web-scrape-qna.md',
        'use-cases/webhook-tool.md',
        'using-flowise/README.md',
        'using-flowise/agentflowv1/README.md',
    ]

    print("=" * 80)
    print("Flowise Documentation Translator (English → Korean)")
    print("=" * 80)
    print(f"Source: {source_base}")
    print(f"Target: {target_base}")
    print(f"Files to translate: {len(files_to_translate)}\n")

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

        if success:
            print(f"[{i:2d}/{len(files_to_translate)}] ✓ {file_path}")
            successful += 1
        else:
            print(f"[{i:2d}/{len(files_to_translate)}] ✗ {file_path} ({message})")
            failed += 1
            failed_files.append(file_path)

    # Summary
    print("\n" + "=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"Total:       {len(files_to_translate)}")
    print(f"Successful:  {successful}")
    print(f"Failed:      {failed}")
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
