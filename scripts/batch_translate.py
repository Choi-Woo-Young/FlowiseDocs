#!/usr/bin/env python3
"""
Batch translate all English markdown files to Korean.
Uses Claude API for efficient translation with batching.
Preserves code blocks, URLs, and technical terms in English.
"""

import os
import re
import sys
import json
from pathlib import Path
from typing import Tuple, Dict, List
import time

try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

EN_BASE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en")
KO_BASE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko")

# Technical terms that must stay in English
PRESERVE_PATTERNS = [
    r"\bFlowise\b",
    r"\bOpenAI\b",
    r"\bLangChain\b",
    r"\bPinecone\b",
    r"\bRedis\b",
    r"\bMongoDB\b",
    r"\bPostgres\b",
    r"\bDocker\b",
    r"\bKubernetes\b",
    r"\bAWS\b",
    r"\bGCP\b",
    r"\bAzure\b",
    r"\bAPI\b",
    r"\bJSON\b",
    r"\bSQL\b",
    r"\bRAG\b",
    r"\bLLM\b",
    r"\bVectorStore\b",
    r"\bEmbedding\b",
    r"\bNode\b",
    r"\bAgent\b",
    r"\bTool\b",
    r"\bRetriever\b",
    r"\bPrompt\b",
    r"\bChain\b",
    r"\bMemory\b",
    r"\bChat\b",
]


class ContentPreserver:
    """Preserves code blocks, URLs, and technical terms."""

    def __init__(self):
        self.code_blocks: Dict[str, str] = {}
        self.urls: Dict[str, str] = {}
        self.terms: Dict[str, str] = {}
        self.counters = {"code": 0, "url": 0, "term": 0}

    def preserve(self, content: str) -> str:
        """Preserve all special content."""
        # Preserve code blocks first (multiline)
        content = self._preserve_code_blocks(content)
        # Then URLs
        content = self._preserve_urls(content)
        # Then technical terms
        content = self._preserve_terms(content)
        return content

    def restore(self, content: str) -> str:
        """Restore all preserved content."""
        # Restore in reverse order
        for placeholder, term in self.terms.items():
            content = content.replace(placeholder, term)
        for placeholder, url in self.urls.items():
            content = content.replace(placeholder, url)
        for placeholder, block in self.code_blocks.items():
            content = content.replace(placeholder, block)
        return content

    def _preserve_code_blocks(self, content: str) -> str:
        """Preserve code blocks."""
        pattern = r"```[\w]*\n(.*?)\n```"
        counter = 0

        def replacer(match):
            nonlocal counter
            placeholder = f"__CODE_{counter}__"
            self.code_blocks[placeholder] = match.group(0)
            counter += 1
            return placeholder

        return re.sub(pattern, replacer, content, flags=re.DOTALL)

    def _preserve_urls(self, content: str) -> str:
        """Preserve URLs."""
        # Skip URLs that are already in code or placeholders
        pattern = r"(?<!`)(?:https?://[^\s\)]+|www\.[^\s\)]+)(?!`)"
        counter = 0

        def replacer(match):
            nonlocal counter
            placeholder = f"__URL_{counter}__"
            self.urls[placeholder] = match.group(0)
            counter += 1
            return placeholder

        return re.sub(pattern, replacer, content)

    def _preserve_terms(self, content: str) -> str:
        """Preserve technical terms."""
        counter = 0

        for pattern in PRESERVE_PATTERNS:
            def replacer(match):
                nonlocal counter
                placeholder = f"__TERM_{counter}__"
                self.terms[placeholder] = match.group(0)
                counter += 1
                return placeholder

            content = re.sub(pattern, replacer, content)

        return content


class Translator:
    """Handles translation using Claude API."""

    def __init__(self):
        if not HAS_ANTHROPIC:
            raise ImportError("anthropic package required")
        self.client = anthropic.Anthropic()

    def translate(self, text: str, filename: str = "") -> str:
        """Translate text using Claude."""
        prompt = f"""Translate the following English markdown text to Korean (한국어).

Rules:
1. Keep markdown formatting exactly as is
2. Do NOT translate code blocks (they contain __CODE_X__ placeholders)
3. Do NOT translate URLs (they contain __URL_X__ placeholders)
4. Do NOT translate technical terms (they contain __TERM_X__ placeholders)
5. Preserve all special characters and formatting
6. Keep numbers, dates, and technical abbreviations as-is
7. Translate only the natural language content

{f"File: {filename}" if filename else ""}

English text:
{text}

Provide only the translated Korean text, no explanations:"""

        message = self.client.messages.create(
            model="claude-opus-4-1-20250805",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return message.content[0].text.strip()


def extract_frontmatter(content: str) -> Tuple[str, str]:
    """Extract YAML frontmatter."""
    if content.startswith("---"):
        try:
            end_index = content.index("---", 3)
            frontmatter = content[:end_index + 3]
            body = content[end_index + 3:].lstrip("\n")
            return frontmatter, body
        except ValueError:
            pass
    return "", content


def translate_file(en_path: Path, translator: Translator) -> str:
    """Translate a single file."""
    with open(en_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter (keep as-is)
    frontmatter, body = extract_frontmatter(content)

    # Preserve special content
    preserver = ContentPreserver()
    body = preserver.preserve(body)

    # Translate
    try:
        translated_body = translator.translate(body, en_path.name)
    except Exception as e:
        print(f"Translation error for {en_path.name}: {e}")
        raise

    # Restore preserved content
    translated_body = preserver.restore(translated_body)

    # Combine with frontmatter
    if frontmatter:
        result = frontmatter + "\n" + translated_body
    else:
        result = translated_body

    return result


def main():
    """Main translation process."""
    if not HAS_ANTHROPIC:
        print("Error: Install anthropic package with: pip install anthropic")
        sys.exit(1)

    # Verify source directory
    if not EN_BASE.exists():
        print(f"Error: Source directory not found: {EN_BASE}")
        sys.exit(1)

    # Create target directory
    KO_BASE.mkdir(parents=True, exist_ok=True)

    # Find all markdown files
    en_files = sorted(EN_BASE.rglob("*.md"))
    print(f"Found {len(en_files)} markdown files to translate\n")

    if not en_files:
        print("No markdown files found!")
        sys.exit(1)

    # Show first few files
    print("Sample files to translate:")
    for f in en_files[:5]:
        print(f"  - {f.relative_to(EN_BASE)}")
    print(f"  ... and {len(en_files) - 5} more\n")

    # Confirm
    response = input(f"Continue with translation? (y/n): ").strip().lower()
    if response != 'y':
        print("Cancelled.")
        sys.exit(0)

    # Initialize translator
    translator = Translator()

    # Process files
    success = 0
    failed = 0
    start_time = time.time()

    for i, en_file in enumerate(en_files, 1):
        try:
            # Calculate relative path
            rel_path = en_file.relative_to(EN_BASE)
            ko_file = KO_BASE / rel_path

            # Create directory
            ko_file.parent.mkdir(parents=True, exist_ok=True)

            # Translate
            translated_content = translate_file(en_file, translator)

            # Write
            with open(ko_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            elapsed = time.time() - start_time
            rate = (i / elapsed) if elapsed > 0 else 0
            print(f"[{i:3d}/{len(en_files)}] ({rate:.1f} files/min) {rel_path}")
            success += 1

            # Rate limit: ~1 second per file to avoid API throttling
            if i < len(en_files):
                time.sleep(0.5)

        except Exception as e:
            print(f"[{i:3d}/{len(en_files)}] ERROR: {en_file.name}")
            print(f"       {str(e)[:100]}")
            failed += 1

    # Summary
    elapsed = time.time() - start_time
    print(f"\n=== Translation Summary ===")
    print(f"Successfully translated: {success} files")
    print(f"Failed: {failed} files")
    print(f"Time elapsed: {elapsed:.1f} seconds")
    print(f"Target directory: {KO_BASE}")


if __name__ == "__main__":
    main()
