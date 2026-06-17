#!/usr/bin/env python3
"""
Batch translate 42 FlowiseDocs markdown files to Korean using the Anthropic API.
Processes files and tracks translation progress with detailed reporting.
"""

import os
import sys
from pathlib import Path
import anthropic

# Initialize Anthropic client (uses ANTHROPIC_API_KEY from environment)
try:
    client = anthropic.Anthropic()
except Exception as e:
    print(f"Failed to initialize Anthropic client: {e}")
    sys.exit(1)

# List of 42 files to translate
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

def read_file(file_path):
    """Read file content from absolute path."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def translate_content(content):
    """Translate content to Korean using Claude API."""
    system_prompt = """You are an expert translator specializing in technical documentation.
Translate the given markdown content to Korean following these rules:
1. Translate titles, headings, and body text to Korean
2. Keep code blocks unchanged
3. Keep image paths and URLs unchanged (only translate link text if present)
4. Keep technical terms in English: Flowise, API, LLM, Node, JavaScript, Python, RAG, Vector Store, Agent, etc.
5. Preserve HTML/Markdown structure completely
6. Keep metadata and YAML frontmatter as-is
7. Maintain the same formatting and indentation

Return ONLY the translated markdown content without any explanation or markdown fence."""

    try:
        message = client.messages.create(
            model="claude-opus-4-8",
            max_tokens=4000,
            system=system_prompt,
            messages=[
                {
                    "role": "user",
                    "content": f"Please translate this markdown content to Korean:\n\n{content}"
                }
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"Error translating content: {e}")
        return None

def write_file(file_path, content):
    """Write translated content to file."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Error writing {file_path}: {e}")
        return False

def main():
    """Main function to process all files."""
    # Get the base directory (FlowiseDocs)
    base_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs"

    successful_translations = 0
    failed_files = []

    print(f"Starting batch translation of {len(FILES_TO_TRANSLATE)} files...")
    print("=" * 80)

    for idx, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        full_path = os.path.join(base_dir, file_path)

        print(f"[{idx:2d}/{len(FILES_TO_TRANSLATE)}] Translating: {file_path}")

        # Read original content
        content = read_file(full_path)
        if content is None:
            print(f"           ✗ Failed to read file")
            failed_files.append(file_path)
            continue

        # Translate content
        translated_content = translate_content(content)
        if translated_content is None:
            print(f"           ✗ Failed to translate")
            failed_files.append(file_path)
            continue

        # Write translated content
        if write_file(full_path, translated_content):
            print(f"           ✓ Successfully translated")
            successful_translations += 1
        else:
            print(f"           ✗ Failed to write translated content")
            failed_files.append(file_path)

    # Print summary
    print("=" * 80)
    print(f"\n배치 6 완료: {successful_translations}개 파일")
    print(f"성공: {successful_translations}/{len(FILES_TO_TRANSLATE)}")

    if failed_files:
        print(f"\n실패한 파일 ({len(failed_files)}):")
        for f in failed_files:
            print(f"  - {f}")
    else:
        print("\n모든 파일 번역이 완료되었습니다!")

    return successful_translations == len(FILES_TO_TRANSLATE)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
