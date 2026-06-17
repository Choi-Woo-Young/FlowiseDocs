#!/usr/bin/env python3
"""
Translate all English markdown files to Korean.
Keeps code blocks, URLs, and technical terms in English.
"""

import os
import re
import sys
from pathlib import Path
from typing import Tuple

# Try to use Claude API for translation
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False
    print("Warning: anthropic package not found. Install with: pip install anthropic")

EN_BASE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en")
KO_BASE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko")


def extract_frontmatter(content: str) -> Tuple[str, str]:
    """Extract YAML frontmatter from markdown content."""
    if content.startswith("---"):
        try:
            end_index = content.index("---", 3)
            frontmatter = content[:end_index + 3]
            body = content[end_index + 3:].lstrip("\n")
            return frontmatter, body
        except ValueError:
            pass
    return "", content


def preserve_code_blocks(content: str) -> Tuple[str, dict]:
    """Extract code blocks and preserve them."""
    code_blocks = {}
    counter = 0

    # Pattern for code blocks with or without language specification
    pattern = r"```[\w]*\n.*?\n```"

    for match in re.finditer(pattern, content, re.DOTALL):
        placeholder = f"__CODE_BLOCK_{counter}__"
        code_blocks[placeholder] = match.group(0)
        counter += 1

    # Replace code blocks with placeholders
    for placeholder, block in code_blocks.items():
        content = content.replace(block, placeholder)

    return content, code_blocks


def preserve_urls(content: str) -> Tuple[str, dict]:
    """Extract URLs and preserve them."""
    urls = {}
    counter = 0

    # Pattern for URLs in markdown links and plain URLs
    pattern = r"(?:https?://[^\s\)]+|www\.[^\s\)]+)"

    for match in re.finditer(pattern, content):
        placeholder = f"__URL_{counter}__"
        urls[placeholder] = match.group(0)
        counter += 1

    # Replace URLs with placeholders
    for placeholder, url in urls.items():
        content = content.replace(url, placeholder)

    return content, urls


def preserve_technical_terms(content: str) -> Tuple[str, dict]:
    """Extract technical terms/product names and preserve them."""
    terms = {}
    counter = 0

    # Common technical terms that should stay in English
    technical_patterns = [
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

    for pattern in technical_patterns:
        for match in re.finditer(pattern, content):
            placeholder = f"__TERM_{counter}__"
            terms[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            counter += 1

    return content, terms


def translate_with_claude(text: str) -> str:
    """Translate text using Claude API."""
    if not HAS_ANTHROPIC:
        print("Error: anthropic package required for translation")
        sys.exit(1)

    client = anthropic.Anthropic()

    prompt = f"""Translate the following English text to Korean (한국어).
Keep the markdown formatting intact.
Do NOT translate code blocks, URLs, technical terms, or product names.
Preserve all special characters and formatting.

English text:
{text}

Provide only the translated Korean text, nothing else."""

    message = client.messages.create(
        model="claude-opus-4-1-20250805",
        max_tokens=4096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


def restore_preserved_content(
    content: str,
    code_blocks: dict,
    urls: dict,
    terms: dict
) -> str:
    """Restore code blocks, URLs, and technical terms."""
    # Restore in reverse order of extraction to avoid conflicts
    for placeholder, block in code_blocks.items():
        content = content.replace(placeholder, block)

    for placeholder, url in urls.items():
        content = content.replace(placeholder, url)

    for placeholder, term in terms.items():
        content = content.replace(placeholder, term)

    return content


def translate_file(en_path: Path) -> str:
    """Translate a single markdown file."""
    print(f"Reading: {en_path}")

    with open(en_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract and preserve frontmatter
    frontmatter, body = extract_frontmatter(content)

    # Extract and preserve special content
    body, code_blocks = preserve_code_blocks(body)
    body, urls = preserve_urls(body)
    body, terms = preserve_technical_terms(body)

    # Translate the main content
    print(f"Translating content from {en_path.name}...")
    translated_body = translate_with_claude(body)

    # Restore preserved content
    translated_body = restore_preserved_content(
        translated_body,
        code_blocks,
        urls,
        terms
    )

    # Combine frontmatter and translated body
    result = frontmatter + "\n" + translated_body if frontmatter else translated_body

    return result


def main():
    """Main translation function."""
    # Verify source directory exists
    if not EN_BASE.exists():
        print(f"Error: Source directory not found: {EN_BASE}")
        sys.exit(1)

    # Create target directory
    KO_BASE.mkdir(parents=True, exist_ok=True)

    # Count files
    en_files = list(EN_BASE.rglob("*.md"))
    print(f"Found {len(en_files)} files to translate\n")

    if not en_files:
        print("No markdown files found!")
        sys.exit(1)

    # Ask for confirmation
    response = input(f"Ready to translate {len(en_files)} files. Continue? (y/n): ")
    if response.lower() != 'y':
        print("Cancelled.")
        sys.exit(0)

    # Translate each file
    success_count = 0
    error_count = 0

    for i, en_file in enumerate(sorted(en_files), 1):
        try:
            # Calculate relative path
            rel_path = en_file.relative_to(EN_BASE)
            ko_file = KO_BASE / rel_path

            # Create directory structure
            ko_file.parent.mkdir(parents=True, exist_ok=True)

            # Translate
            translated_content = translate_file(en_file)

            # Write translated file
            with open(ko_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print(f"[{i}/{len(en_files)}] Saved: {ko_file}")
            success_count += 1

        except Exception as e:
            print(f"[{i}/{len(en_files)}] ERROR processing {en_file}: {e}")
            error_count += 1

    # Summary
    print(f"\n=== Translation Complete ===")
    print(f"Successfully translated: {success_count} files")
    print(f"Errors: {error_count} files")
    print(f"Target directory: {KO_BASE}")


if __name__ == "__main__":
    main()
