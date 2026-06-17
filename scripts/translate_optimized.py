#!/usr/bin/env python3
"""
Optimized Flowise documentation translator from English to Korean
Uses Claude API with batching for efficiency
"""

import os
import sys
import re
import time
from pathlib import Path
from typing import Tuple, List, Dict

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    print("Error: anthropic library not found. Install with: pip install anthropic")
    sys.exit(1)


class MarkdownPreserver:
    """Preserve code blocks, URLs, and special syntax during translation"""

    def __init__(self):
        self.preserved_items = {}
        self.counter = 0

    def preserve_pattern(self, content: str, pattern: str, prefix: str) -> str:
        """Replace matches of pattern with placeholders"""
        matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))

        # Process in reverse order to maintain indices
        for match in reversed(matches):
            placeholder = f"__{prefix}_{self.counter}__"
            self.preserved_items[placeholder] = match.group(0)
            content = content[:match.start()] + placeholder + content[match.end():]
            self.counter += 1

        return content

    def preserve_all(self, content: str) -> str:
        """Preserve all non-translatable content"""
        # Preserve YAML frontmatter
        content = self.preserve_pattern(content, r'^---\n.*?\n---\n', 'YAML')

        # Preserve code blocks
        content = self.preserve_pattern(content, r'```[\s\S]*?```', 'CODE')

        # Preserve inline code
        content = self.preserve_pattern(content, r'`[^`\n]+`', 'INLINE')

        # Preserve URLs
        content = self.preserve_pattern(content, r'https?://[^\s)]+', 'URL')

        # Preserve file paths
        content = self.preserve_pattern(content, r'/[a-zA-Z0-9\-_./:]+\.md', 'PATH')

        # Preserve HTML tags
        content = self.preserve_pattern(content, r'<[^>]+>', 'HTML')

        # Preserve GitBook syntax
        content = self.preserve_pattern(content, r'{%[^%]*%}', 'GITBOOK')

        # Preserve image syntax
        content = self.preserve_pattern(content, r'!\[[^\]]*\]\([^\)]+\)', 'IMAGE')

        # Preserve markdown links
        content = self.preserve_pattern(content, r'\[[^\]]+\]\([^\)]+\)', 'LINK')

        return content

    def restore_all(self, content: str) -> str:
        """Restore all preserved content"""
        for placeholder, original in sorted(self.preserved_items.items(), reverse=True):
            content = content.replace(placeholder, original)
        return content


class KoreanTranslator:
    """Translate markdown content to Korean using Claude API"""

    def __init__(self):
        api_key = os.environ.get('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-3-5-sonnet-20241022"
        self.rate_limit_delay = 0.5  # seconds between API calls

    def translate_content(self, content: str, file_path: str = "") -> str:
        """Translate markdown content to Korean"""
        preserv = MarkdownPreserver()

        # Preserve all non-translatable content
        preserved_content = preserv.preserve_all(content)

        # Create translation prompt
        system_prompt = """You are a technical documentation translator. Translate the following markdown content from English to Korean.

Translation rules:
1. Keep all placeholders (like __CODE_*, __URL_*, etc.) exactly as they are - DO NOT translate them
2. Keep technical terms, product names, and company names in English (e.g., Airtable, OpenAI, Redis, API, LLM)
3. Translate markdown headings, descriptions, and narrative text
4. Preserve all markdown syntax (##, *, -, >, etc.)
5. Preserve formatting and structure
6. Keep line breaks and paragraph structure intact
7. If you see placeholders, do not translate or modify them in any way

Return ONLY the translated content without any explanation or additional text."""

        user_prompt = f"""Please translate the following markdown content to Korean:

{preserved_content}"""

        try:
            print(f"  Translating {file_path}...", end=" ", flush=True)

            message = self.client.messages.create(
                model=self.model,
                max_tokens=8192,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt
                    }
                ]
            )

            translated = message.content[0].text

            # Restore preserved content
            translated = preserv.restore_all(translated)

            print("✓")
            return translated

        except Exception as e:
            print(f"✗ (Error: {str(e)[:50]})")
            raise


def translate_file(source_path: str, target_path: str, translator: KoreanTranslator) -> bool:
    """Translate a single file"""
    try:
        # Read source file
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Translate
        translated_content = translator.translate_content(content, str(source_path))

        # Create target directory if needed
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        # Write translated file
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True

    except Exception as e:
        print(f"    Error: {e}")
        return False


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

    print("=" * 70)
    print("Flowise Documentation Translator (English → Korean)")
    print("=" * 70)
    print(f"Source: {source_base}")
    print(f"Target: {target_base}")
    print(f"Files to translate: {len(files_to_translate)}\n")

    # Initialize translator
    try:
        translator = KoreanTranslator()
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    successful = 0
    failed = 0
    failed_files = []

    # Translate files
    for i, file_path in enumerate(files_to_translate, 1):
        source_file = source_base / file_path
        target_file = target_base / file_path

        # Check if source exists
        if not source_file.exists():
            print(f"[{i:2d}/{len(files_to_translate)}] ✗ {file_path} (not found)")
            failed += 1
            failed_files.append(file_path)
            continue

        # Translate
        print(f"[{i:2d}/{len(files_to_translate)}] {file_path}...", end=" ", flush=True)
        try:
            if translate_file(str(source_file), str(target_file), translator):
                print("✓")
                successful += 1
                time.sleep(0.2)  # Small delay between requests
            else:
                print("✗")
                failed += 1
                failed_files.append(file_path)
        except Exception as e:
            print(f"✗ ({str(e)[:40]})")
            failed += 1
            failed_files.append(file_path)

    # Print summary
    print("\n" + "=" * 70)
    print("Translation Summary")
    print("=" * 70)
    print(f"Total files: {len(files_to_translate)}")
    print(f"Successful:  {successful}")
    print(f"Failed:      {failed}")
    print(f"Success rate: {successful/len(files_to_translate)*100:.1f}%")

    if failed_files:
        print(f"\nFailed files:")
        for file_path in failed_files:
            print(f"  - {file_path}")

    # Verify translated files
    print(f"\nVerifying translated files in {target_base}:")
    ko_files = list(target_base.glob('**/*.md'))
    print(f"Total Korean files: {len(ko_files)}")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
