#!/usr/bin/env python3
"""
Translate 43 Flowise documentation files from English to Korean using Claude API.
Handles code blocks, URLs, and technical terms preservation.
"""

import os
import sys
import re
import json
from pathlib import Path
from datetime import datetime
import anthropic

# The exact 43 files to translate
FILES_TO_TRANSLATE = [
    "integrations/langchain/memory/buffer-memory.md",
    "integrations/langchain/memory/buffer-window-memory.md",
    "integrations/langchain/memory/conversation-summary-buffer-memory.md",
    "integrations/langchain/memory/conversation-summary-memory.md",
    "integrations/langchain/memory/dynamodb-chat-memory.md",
    "integrations/langchain/memory/mem0-memory.md",
    "integrations/langchain/memory/mongodb-atlas-chat-memory.md",
    "integrations/langchain/memory/redis-backed-chat-memory.md",
    "integrations/langchain/memory/upstash-redis-backed-chat-memory.md",
    "integrations/langchain/memory/zep-memory.md",
    "integrations/langchain/moderation/openai-moderation.md",
    "integrations/langchain/moderation/simple-prompt-moderation.md",
    "integrations/langchain/output-parsers/advanced-structured-output-parser.md",
    "integrations/langchain/output-parsers/csv-output-parser.md",
    "integrations/langchain/output-parsers/custom-list-output-parser.md",
    "integrations/langchain/output-parsers/structured-output-parser.md",
    "integrations/langchain/prompts/chat-prompt-template.md",
    "integrations/langchain/prompts/few-shot-prompt-template.md",
    "integrations/langchain/prompts/prompt-template.md",
    "integrations/langchain/README.md",
    "integrations/langchain/record-managers.md",
    "integrations/langchain/retrievers/cohere-rerank-retriever.md",
    "integrations/langchain/retrievers/custom-retriever.md",
    "integrations/langchain/retrievers/embeddings-filter-retriever.md",
    "integrations/langchain/retrievers/extract-metadata-retriever.md",
    "integrations/langchain/retrievers/hyde-retriever.md",
    "integrations/langchain/retrievers/llm-filter-retriever.md",
    "integrations/langchain/retrievers/multi-query-retriever.md",
    "integrations/langchain/retrievers/page.md",
    "integrations/langchain/retrievers/prompt-retriever.md",
    "integrations/langchain/retrievers/reciprocal-rank-fusion-retriever.md",
    "integrations/langchain/retrievers/similarity-score-threshold-retriever.md",
    "integrations/langchain/retrievers/vector-store-retriever.md",
    "integrations/langchain/text-splitters/character-text-splitter.md",
    "integrations/langchain/text-splitters/code-text-splitter.md",
    "integrations/langchain/text-splitters/html-to-markdown-text-splitter.md",
    "integrations/langchain/text-splitters/markdown-text-splitter.md",
    "integrations/langchain/text-splitters/recursive-character-text-splitter.md",
    "integrations/langchain/text-splitters/token-text-splitter.md",
    "integrations/langchain/tools/bravesearch-api.md",
    "integrations/langchain/tools/browserless-mcp.md",
    "integrations/langchain/tools/calculator.md",
    "integrations/langchain/tools/chain-tool.md",
]

class ContentPreserver:
    """Preserve code blocks, URLs, and special content during translation"""

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

        # Code blocks with language specification
        content = self.preserve(content, r'```[a-z]*\n[\s\S]*?```', 'CODE')

        # HTML pre tags with code
        content = self.preserve(content, r'<pre[^>]*>[\s\S]*?</pre>', 'HTMLPRE')

        # Inline code
        content = self.preserve(content, r'`[^`\n]+`', 'INLINE')

        # URLs
        content = self.preserve(content, r'https?://[^\s\)>\]]+', 'URL')

        # HTML tags
        content = self.preserve(content, r'<[^>]+>', 'HTML')

        # GitBook syntax
        content = self.preserve(content, r'{%[^%]*%}', 'GITBOOK')

        # Images
        content = self.preserve(content, r'!\[[^\]]*\]\([^\)]+\)', 'IMAGE')

        # Markdown links (preserve entire link)
        content = self.preserve(content, r'\[[^\]]+\]\([^\)]+\)', 'LINK')

        return content

    def restore(self, content: str) -> str:
        """Restore preserved content"""
        for placeholder, original in self.preserved.items():
            content = content.replace(placeholder, original)
        return content


def translate_with_claude(text: str, file_path: str) -> str:
    """Translate text to Korean using Claude API"""

    if not text.strip():
        return text

    # Create client - automatically reads ANTHROPIC_API_KEY from environment
    try:
        client = anthropic.Anthropic()
    except Exception as e:
        # Try to get API key from environment more explicitly
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not set in environment")
        client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are a professional translator. Translate the following Flowise documentation from English to Korean.

TRANSLATION RULES:
1. Translate titles, body text, and tables to Korean
2. Keep code blocks unchanged (they are already marked with placeholders)
3. Keep image paths and URLs unchanged
4. Keep technical terms in English: Flowise, API, LLM, Node, LocalAI, ChatLocalAI, Docker, Python, JavaScript, HTTP, REST, JSON, etc.
5. Keep placeholder markers unchanged (like __PRESERVE_* markers)
6. Preserve all Markdown structure and HTML tags
7. Maintain the original formatting and line breaks
8. Only translate plain English text, not code or URLs

File: {file_path}

Text to translate:
{text}

Translate to Korean while following all the rules above. Return only the translated text without any explanation."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def translate_file(source_path: str, target_path: str) -> tuple:
    """Translate a markdown file"""
    try:
        # Read source
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Preserve special content
        preserver = ContentPreserver()
        preserved_content = preserver.preserve_all(content)

        # Translate with Claude
        translated_content = translate_with_claude(preserved_content, Path(source_path).name)

        # Restore preserved content
        translated_content = preserver.restore(translated_content)

        # Create target directory
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        # Write translated file
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True, f"✓ {Path(source_path).name}"

    except Exception as e:
        return False, f"✗ {Path(source_path).name}: {str(e)[:60]}"


def main():
    """Main translation script"""
    base_en_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
    base_ko_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

    print("=" * 80)
    print("Flowise Documentation Translator (English → Korean)")
    print("=" * 80)
    print(f"Total files to translate: {len(FILES_TO_TRANSLATE)}")
    print()

    successful = 0
    failed = 0
    failed_files = []

    for i, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        source_path = os.path.join(base_en_dir, file_path)
        target_path = os.path.join(base_ko_dir, file_path)

        print(f"[{i:2d}/{len(FILES_TO_TRANSLATE)}] Translating {Path(file_path).name}...", end=" ")

        success, message = translate_file(source_path, target_path)

        if success:
            print(message)
            successful += 1
        else:
            print(message)
            failed += 1
            failed_files.append(file_path)

    print()
    print("=" * 80)
    print("TRANSLATION SUMMARY")
    print("=" * 80)
    print(f"Total files requested:  {len(FILES_TO_TRANSLATE)}")
    print(f"Successfully translated: {successful}")
    print(f"Failed:                  {failed}")
    print(f"Success rate: {(successful/len(FILES_TO_TRANSLATE)*100):.1f}%")

    if failed_files:
        print()
        print("Failed files:")
        for f in failed_files:
            print(f"  - {f}")

    # Save status
    status = {
        "timestamp": datetime.now().isoformat(),
        "total": len(FILES_TO_TRANSLATE),
        "successful": successful,
        "failed": failed,
        "files": FILES_TO_TRANSLATE
    }

    status_file = os.path.join(base_ko_dir, "../translation_status_43.json")
    with open(status_file, 'w') as f:
        json.dump(status, f, indent=2)

    print()
    print(f"Translation status saved to: {status_file}")
    print()

    return successful


if __name__ == "__main__":
    successful = main()
    print(f"FINAL COUNT: {successful} files successfully translated")
    sys.exit(0 if successful == len(FILES_TO_TRANSLATE) else 1)
