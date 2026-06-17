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

# Files to translate (43 files total)
FILES_TO_TRANSLATE = [
    "integrations/langchain/chat-models/chatlocalai.md",
    "integrations/langchain/chat-models/chatollama.md",
    "integrations/langchain/chat-models/chattogetherai.md",
    "integrations/langchain/chat-models/google-ai.md",
    "integrations/langchain/chat-models/ibm-watsonx.md",
    "integrations/langchain/chat-models/mistral-ai.md",
    "integrations/langchain/chat-models/nvidia-nim.md",
    "integrations/langchain/document-loaders/apify-website-content-crawler.md",
    "integrations/langchain/document-loaders/bravesearch-api.md",
    "integrations/langchain/document-loaders/cheerio-web-scraper.md",
    "integrations/langchain/document-loaders/confluence.md",
    "integrations/langchain/document-loaders/csv-file.md",
    "integrations/langchain/document-loaders/custom-document-loader.md",
    "integrations/langchain/document-loaders/document-store.md",
    "integrations/langchain/document-loaders/docx-file.md",
    "integrations/langchain/document-loaders/epub-file.md",
    "integrations/langchain/document-loaders/figma.md",
    "integrations/langchain/document-loaders/file-loader.md",
    "integrations/langchain/document-loaders/firecrawl.md",
    "integrations/langchain/document-loaders/folder.md",
    "integrations/langchain/document-loaders/gitbook.md",
    "integrations/langchain/document-loaders/github.md",
    "integrations/langchain/document-loaders/google-drive.md",
    "integrations/langchain/document-loaders/google-sheets.md",
    "integrations/langchain/document-loaders/jira.md",
    "integrations/langchain/document-loaders/json-file.md",
    "integrations/langchain/document-loaders/jsonlines.md",
    "integrations/langchain/document-loaders/microsoft-excel.md",
    "integrations/langchain/document-loaders/microsoft-powerpoint.md",
    "integrations/langchain/document-loaders/microsoft-word.md",
    "integrations/langchain/document-loaders/notion.md",
    "integrations/langchain/document-loaders/oxylabs.md",
    "integrations/langchain/document-loaders/pdf-file.md",
    "integrations/langchain/document-loaders/plain-text.md",
    "integrations/langchain/document-loaders/playwright-web-scraper.md",
    "integrations/langchain/document-loaders/puppeteer-web-scraper.md",
    "integrations/langchain/document-loaders/s3-file-loader.md",
    "integrations/langchain/document-loaders/searchapi-for-web-search.md",
    "integrations/langchain/document-loaders/serpapi-for-web-search.md",
    "integrations/langchain/document-loaders/spider-web-scraper-crawler.md",
    "integrations/langchain/document-loaders/text-file.md",
    "integrations/langchain/document-loaders/unstructured-file-loader.md",
    "integrations/langchain/document-loaders/unstructured-folder-loader.md",
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

    client = anthropic.Anthropic()

    prompt = f"""You are a professional translator. Translate the following Flowise documentation from English to Korean.

TRANSLATION RULES:
1. Translate titles, body text, and tables to Korean
2. Keep code blocks unchanged (they are already marked with placeholders)
3. Keep image paths and URLs unchanged
4. Keep technical terms in English: Flowise, API, LLM, Node, LocalAI, ChatLocalAI, Docker, etc.
5. Keep placeholder markers unchanged (like __PRESERVE_* markers)
6. Preserve all Markdown structure and HTML tags
7. Maintain the original formatting and line breaks
8. Only translate plain English text, not code or URLs

File: {file_path}

Text to translate:
{text}

Translate to Korean while following all the rules above. Return only the translated text without any explanation."""

    message = client.messages.create(
        model="claude-opus-4-1-20250805",
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
    print("Using Claude API with proper content preservation")
    print("=" * 80)
    print(f"Source: {base_en_dir}")
    print(f"Target: {base_ko_dir}")
    print(f"Files to translate: {len(FILES_TO_TRANSLATE)}\n")

    successful = 0
    failed = 0
    failed_files = []
    skipped = 0

    for i, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        source_file = os.path.join(base_en_dir, file_path)
        target_file = os.path.join(base_ko_dir, file_path)

        if not os.path.exists(source_file):
            print(f"[{i:2d}/{len(FILES_TO_TRANSLATE)}] ⊘ {Path(source_file).name} (source not found)")
            skipped += 1
            continue

        print(f"[{i:2d}/{len(FILES_TO_TRANSLATE)}] Translating {Path(source_file).name}...", end=" ")
        sys.stdout.flush()

        success, message = translate_file(source_file, target_file)

        if success:
            print(message)
            successful += 1
        else:
            print(message)
            failed += 1
            failed_files.append((file_path, message))

    # Summary
    print("\n" + "=" * 80)
    print("TRANSLATION SUMMARY")
    print("=" * 80)
    print(f"Total files requested:  {len(FILES_TO_TRANSLATE)}")
    print(f"Successfully translated: {successful}")
    print(f"Failed:                  {failed}")
    print(f"Skipped (not found):     {skipped}")
    print(f"Success rate: {successful/len(FILES_TO_TRANSLATE)*100:.1f}%")

    if failed_files:
        print(f"\nFailed files ({len(failed_files)}):")
        for file_path, error in failed_files:
            print(f"  - {file_path}")
            print(f"    Error: {error}")

    # Save translation status
    status_file = os.path.join(base_ko_dir, "..", "translation_status_43.json")
    with open(status_file, 'w', encoding='utf-8') as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "total": len(FILES_TO_TRANSLATE),
            "successful": successful,
            "failed": failed,
            "skipped": skipped,
            "success_rate": f"{successful/len(FILES_TO_TRANSLATE)*100:.1f}%",
            "failed_files": [f[0] for f in failed_files]
        }, f, indent=2, ensure_ascii=False)

    print(f"\nTranslation status saved to: {status_file}")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
