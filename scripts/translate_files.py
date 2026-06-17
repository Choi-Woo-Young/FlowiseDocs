#!/usr/bin/env python3
"""
Translate FlowiseDocs markdown files from English to Korean
Preserves code blocks, URLs, image paths, HTML tags, and technical terms
"""

import os
import re
import sys
from pathlib import Path
from typing import Tuple, List
import json

try:
    from anthropic import Anthropic
except ImportError:
    print("Error: anthropic package not installed. Install with: pip install anthropic")
    sys.exit(1)

# Configuration
BASE_EN_PATH = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en/integrations/langchain/"
BASE_KO_PATH = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko/integrations/langchain/"

# Files to translate
FILES_TO_TRANSLATE = {
    "memory": [
        "buffer-memory.md",
        "buffer-window-memory.md",
        "conversation-summary-buffer-memory.md",
        "conversation-summary-memory.md",
        "dynamodb-chat-memory.md",
        "mem0-memory.md",
        "mongodb-atlas-chat-memory.md",
        "redis-backed-chat-memory.md",
        "upstash-redis-backed-chat-memory.md",
        "zep-memory.md",
    ],
    "moderation": [
        "openai-moderation.md",
        "simple-prompt-moderation.md",
    ],
    "output-parsers": [
        "advanced-structured-output-parser.md",
        "csv-output-parser.md",
        "custom-list-output-parser.md",
        "structured-output-parser.md",
    ],
    "prompts": [
        "chat-prompt-template.md",
        "few-shot-prompt-template.md",
        "prompt-template.md",
    ],
    "": [  # Root level files
        "README.md",
        "record-managers.md",
    ],
    "retrievers": [
        "cohere-rerank-retriever.md",
        "custom-retriever.md",
        "embeddings-filter-retriever.md",
        "extract-metadata-retriever.md",
        "hyde-retriever.md",
        "llm-filter-retriever.md",
        "multi-query-retriever.md",
        "page.md",
        "prompt-retriever.md",
        "reciprocal-rank-fusion-retriever.md",
        "similarity-score-threshold-retriever.md",
        "vector-store-retriever.md",
    ],
    "text-splitters": [
        "character-text-splitter.md",
        "code-text-splitter.md",
        "html-to-markdown-text-splitter.md",
        "markdown-text-splitter.md",
        "recursive-character-text-splitter.md",
        "token-text-splitter.md",
    ],
    "tools": [
        "bravesearch-api.md",
        "browserless-mcp.md",
        "calculator.md",
        "chain-tool.md",
    ],
}

class MarkdownTranslator:
    def __init__(self):
        """Initialize the translator with Anthropic client"""
        try:
            # The Anthropic client will automatically detect API key from environment
            # or raise an error if not found
            self.client = Anthropic()
            self.model = "claude-3-5-sonnet-20241022"
            self.translation_cache = {}
        except Exception as e:
            print(f"Error initializing Anthropic client: {e}")
            print("\nPlease set your API key:")
            print("  export ANTHROPIC_API_KEY='your-api-key'")
            raise

    def extract_code_blocks(self, text: str) -> Tuple[str, List[str]]:
        """Extract code blocks and return text with placeholders and code blocks"""
        code_blocks = []
        pattern = r"```[\s\S]*?```"

        def replace_code(match):
            code_blocks.append(match.group(0))
            return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

        text = re.sub(pattern, replace_code, text)
        return text, code_blocks

    def extract_html_tags(self, text: str) -> Tuple[str, List[str]]:
        """Extract HTML tags and return text with placeholders and tags"""
        html_tags = []
        # Match opening tags, closing tags, and self-closing tags
        pattern = r"<[^>]+>"

        def replace_html(match):
            html_tags.append(match.group(0))
            return f"__HTML_TAG_{len(html_tags) - 1}__"

        text = re.sub(pattern, replace_html, text)
        return text, html_tags

    def extract_links_and_images(self, text: str) -> Tuple[str, List[str]]:
        """Extract markdown links and image references"""
        links = []
        # Match markdown links [text](url) and images ![alt](url)
        pattern = r"\[([^\]]+)\]\(([^)]+)\)|!\[([^\]]*)\]\(([^)]+)\)"

        def replace_link(match):
            links.append(match.group(0))
            return f"__LINK_{len(links) - 1}__"

        text = re.sub(pattern, replace_link, text)
        return text, links

    def prepare_text_for_translation(self, markdown_text: str) -> dict:
        """Prepare markdown text by extracting preservable elements"""
        # Extract code blocks
        text, code_blocks = self.extract_code_blocks(markdown_text)

        # Extract HTML tags
        text, html_tags = self.extract_html_tags(text)

        # Extract links and images
        text, links = self.extract_links_and_images(text)

        return {
            "text": text,
            "code_blocks": code_blocks,
            "html_tags": html_tags,
            "links": links,
        }

    def restore_preserved_elements(self, translated_text: str, preserved: dict) -> str:
        """Restore code blocks, HTML tags, and links to translated text"""
        text = translated_text

        # Restore links
        for i, link in enumerate(preserved["links"]):
            text = text.replace(f"__LINK_{i}__", link)

        # Restore HTML tags
        for i, tag in enumerate(preserved["html_tags"]):
            text = text.replace(f"__HTML_TAG_{i}__", tag)

        # Restore code blocks
        for i, code in enumerate(preserved["code_blocks"]):
            text = text.replace(f"__CODE_BLOCK_{i}__", code)

        return text

    def translate_text(self, text: str) -> str:
        """Translate text to Korean using Claude API"""
        if not text.strip():
            return text

        # Check cache
        if text in self.translation_cache:
            return self.translation_cache[text]

        try:
            # Recreate client to ensure auth is fresh
            client = Anthropic()
            message = client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {
                        "role": "user",
                        "content": f"""Translate the following Markdown text from English to Korean.

IMPORTANT RULES:
1. Keep technical terms in English: API, LLM, Node, Python, JavaScript, HTTP, REST, JSON, CSV, etc.
2. Keep code block placeholders (__CODE_BLOCK_*__) unchanged
3. Keep link placeholders (__LINK_*__) unchanged
4. Keep HTML tag placeholders (__HTML_TAG_*__) unchanged
5. Preserve all Markdown formatting (headers, bold, italic, tables, etc.)
6. Do NOT translate parameter names, variable names, or configuration keys
7. Translate only the descriptive text and human-readable content
8. For table content: translate descriptions but keep parameter names in English

Text to translate:
{text}

Return ONLY the translated text, nothing else.""",
                    }
                ],
            )

            translated = message.content[0].text
            self.translation_cache[text] = translated
            return translated
        except Exception as e:
            print(f"Error translating text: {e}")
            return text

    def translate_markdown_file(self, en_path: str) -> str:
        """Translate a markdown file while preserving structure"""
        try:
            with open(en_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Prepare text by extracting preservable elements
            preserved = self.prepare_text_for_translation(content)

            # Translate the prepared text
            translated = self.translate_text(preserved["text"])

            # Restore preserved elements
            result = self.restore_preserved_elements(translated, preserved)

            return result
        except Exception as e:
            print(f"Error processing file {en_path}: {e}")
            return None

    def save_translated_file(self, ko_path: str, content: str) -> bool:
        """Save translated content to Korean file"""
        try:
            # Ensure directory exists
            ko_dir = os.path.dirname(ko_path)
            os.makedirs(ko_dir, exist_ok=True)

            with open(ko_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error saving file {ko_path}: {e}")
            return False


def main():
    """Main translation workflow"""
    print("FlowiseDocs Markdown Translator")
    print("=" * 50)

    # Initialize translator
    try:
        translator = MarkdownTranslator()
    except ValueError as e:
        print(f"Error: {e}")
        print("\nTo fix this, set your API key:")
        print("  export ANTHROPIC_API_KEY='your-key-here'")
        sys.exit(1)

    total_files = 0
    translated_files = 0
    failed_files = []

    # Iterate through all files to translate
    for category, files in FILES_TO_TRANSLATE.items():
        category_path = category if category else ""
        en_dir = os.path.join(BASE_EN_PATH, category_path) if category_path else BASE_EN_PATH
        ko_dir = os.path.join(BASE_KO_PATH, category_path) if category_path else BASE_KO_PATH

        for filename in files:
            total_files += 1
            en_file = os.path.join(en_dir, filename)
            ko_file = os.path.join(ko_dir, filename)

            print(f"\n[{total_files}/{sum(len(f) for f in FILES_TO_TRANSLATE.values())}] Translating: {category}/{filename}" if category else f"[{total_files}/{sum(len(f) for f in FILES_TO_TRANSLATE.values())}] Translating: {filename}")

            # Check if source file exists
            if not os.path.exists(en_file):
                print(f"  ERROR: Source file not found: {en_file}")
                failed_files.append(filename)
                continue

            # Translate file
            translated_content = translator.translate_markdown_file(en_file)

            if translated_content is None:
                print(f"  ERROR: Failed to translate")
                failed_files.append(filename)
                continue

            # Save translated file
            if translator.save_translated_file(ko_file, translated_content):
                print(f"  SUCCESS: Saved to {ko_file}")
                translated_files += 1
            else:
                print(f"  ERROR: Failed to save")
                failed_files.append(filename)

    # Summary
    print("\n" + "=" * 50)
    print(f"Translation Complete")
    print(f"Total files: {total_files}")
    print(f"Successfully translated: {translated_files}")
    print(f"Failed: {len(failed_files)}")

    if failed_files:
        print(f"\nFailed files:")
        for f in failed_files:
            print(f"  - {f}")

    return 0 if len(failed_files) == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
