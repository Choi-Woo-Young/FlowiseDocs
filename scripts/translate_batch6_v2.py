#!/usr/bin/env python3
"""
Batch translate 42 FlowiseDocs markdown files to Korean using Claude API.
Uses the Anthropic SDK with proper error handling and progress tracking.
"""

import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Installing anthropic SDK...")
    os.system("pip install anthropic -q")
    import anthropic

# Base directory
BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs"

# Files to translate
FILES_TO_TRANSLATE = [
    "ko/integrations/langchain/tools/chatflow-tool.md",
    "ko/integrations/langchain/tools/custom-tool.md",
    "ko/integrations/langchain/tools/exa-search.md",
    "ko/integrations/langchain/tools/gmail.md",
    "ko/integrations/langchain/tools/google-calendar.md",
    "ko/integrations/langchain/tools/google-custom-search.md",
    "ko/integrations/langchain/tools/google-drive.md",
    "ko/integrations/langchain/tools/google-sheets.md",
    "ko/integrations/langchain/tools/microsoft-outlook.md",
    "ko/integrations/langchain/tools/microsoft-teams.md",
    "ko/integrations/langchain/tools/openapi-toolkit.md",
    "ko/integrations/langchain/tools/tavily-ai.md",
    "ko/integrations/langchain/tools/web-browser.md",
    "ko/integrations/langchain/tools/write-file.md",
    "ko/integrations/langchain/vector-stores/chroma.md",
    "ko/integrations/langchain/vector-stores/couchbase.md",
    "ko/integrations/langchain/vector-stores/elastic.md",
    "ko/integrations/langchain/vector-stores/in-memory-vector-store.md",
    "ko/integrations/langchain/vector-stores/opensearch.md",
    "ko/integrations/langchain/vector-stores/redis.md",
    "ko/integrations/langchain/vector-stores/singlestore.md",
    "ko/integrations/langchain/vector-stores/upstash-vector.md",
    "ko/integrations/langchain/vector-stores/zep-collection-cloud.md",
    "ko/integrations/langchain/vector-stores/zep-collection-open-source.md",
    "ko/integrations/litellm/README.md",
    "ko/integrations/llamaindex/README.md",
    "ko/integrations/llamaindex/vector-stores/README.md",
    "ko/integrations/README.md",
    "ko/integrations/utilities/README.md",
    "ko/migration-guide/v1.3.0-migration-guide.md",
    "ko/migration-guide/v1.4.3-migration-guide.md",
    "ko/migration-guide/v2.1.4-migration-guide.md",
    "ko/text-splitters/charater-text-splitter.md",
    "ko/use-cases/interacting-with-api.md",
    "ko/use-cases/multiple-documents-qna.md",
    "ko/use-cases/README.md",
    "ko/use-cases/sql-qna.md",
    "ko/use-cases/upserting-data.md",
    "ko/use-cases/web-scrape-qna.md",
    "ko/use-cases/webhook-tool.md",
    "ko/using-flowise/agentflowv1/README.md",
    "ko/using-flowise/analytics/langfuse.md",
]

def translate_with_claude(content):
    """Translate content using Claude API."""
    client = anthropic.Anthropic()

    message = client.messages.create(
        model="claude-opus-4-1",
        max_tokens=4096,
        system="""You are an expert translator specializing in technical documentation.
Translate the given markdown content to Korean following these rules:
1. Translate titles, headings, and body text to Korean
2. Keep code blocks unchanged
3. Keep image paths and URLs unchanged (only translate link text)
4. Keep technical terms in English: Flowise, API, LLM, Node, JavaScript, Python, RAG, Vector Store, Agent, etc.
5. Preserve HTML/Markdown structure completely
6. Keep YAML frontmatter/metadata as-is
7. Maintain all formatting and indentation

Return ONLY the translated markdown content without any explanation or markdown fence.""",
        messages=[
            {
                "role": "user",
                "content": f"Please translate this markdown content to Korean:\n\n{content}"
            }
        ]
    )
    return message.content[0].text

def main():
    """Main translation function."""
    successful = 0
    failed = 0
    failed_files = []

    print(f"Starting batch translation of {len(FILES_TO_TRANSLATE)} files...")
    print("=" * 70)

    for idx, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        full_path = os.path.join(BASE_DIR, file_path)

        try:
            # Read file
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            print(f"[{idx:2d}/{len(FILES_TO_TRANSLATE)}] Translating: {file_path}")

            # Translate
            translated = translate_with_claude(content)

            # Write back
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(translated)

            print(f"            ✓ Success")
            successful += 1

        except FileNotFoundError:
            print(f"            ✗ File not found")
            failed += 1
            failed_files.append(file_path)
        except Exception as e:
            print(f"            ✗ Error: {str(e)[:50]}")
            failed += 1
            failed_files.append(file_path)

    # Summary
    print("=" * 70)
    print(f"\n배치 6 완료: {successful}개 파일")
    print(f"성공: {successful}/{len(FILES_TO_TRANSLATE)}")

    if failed_files:
        print(f"\n실패한 파일 ({failed}):")
        for f in failed_files:
            print(f"  - {f}")

    return successful == len(FILES_TO_TRANSLATE)

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n번역이 중단되었습니다.")
        sys.exit(1)
