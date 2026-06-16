#!/usr/bin/env python3
"""
Flowise Documentation Translator
Translates all English markdown files to Korean using the Anthropic API

Usage:
    python3 translate_to_korean.py

Requirements:
    - ANTHROPIC_API_KEY environment variable set
    - anthropic SDK installed: pip install anthropic
"""

import os
import sys
import re
from pathlib import Path
from typing import Tuple, Optional
import anthropic

# Configuration
EN_DIR = Path(__file__).parent / "en"
KO_DIR = Path(__file__).parent / "ko"

# Technical terms that should NOT be translated
TECHNICAL_TERMS = {
    # Core concepts
    'API', 'LLM', 'RAG', 'Node', 'Agent', 'Tool', 'Flowise', 'JSON', 'HTTP', 'REST',
    'CLI', 'SDK', 'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'OCI',

    # Databases & Storage
    'Redis', 'PostgreSQL', 'MongoDB', 'MySQL', 'Postgres', 'SQLite', 'Elasticsearch',
    'Cassandra', 'DynamoDB', 's3', 'GCS', 'Blob',

    # Languages & Frameworks
    'JavaScript', 'TypeScript', 'Python', 'Node.js', 'Express', 'React', 'Vue', 'Angular',
    'FastAPI', 'Django', 'Flask', 'Spring', 'Boot', 'Gradle',

    # AI/ML Services
    'OpenAI', 'Anthropic', 'Claude', 'GPT', 'LLAMA', 'Gemini', 'Vertex', 'Bedrock',
    'Vector', 'Embedding', 'Langchain', 'LlamaIndex', 'Hugging', 'Face', 'HuggingFace',

    # Queue & Messaging
    'BullMQ', 'Kafka', 'RabbitMQ', 'Pub/Sub', 'Topic', 'Queue', 'Message', 'Consumer',

    # Communication
    'SSE', 'WebSocket', 'Webhook', 'OAuth', 'JWT', 'CORS', 'SSL', 'TLS', 'HTTP2',
    'GraphQL', 'SAML', 'LDAP', 'gRPC',

    # Infrastructure
    'Container', 'Image', 'Volume', 'Network', 'Service', 'Pod', 'Deployment', 'Ingress',
    'LoadBalancer', 'StatefulSet', 'DaemonSet', 'CronJob', 'ConfigMap', 'Secret',
    'PersistentVolume', 'StorageClass', 'Registry',

    # Version Control
    'GitHub', 'GitLab', 'Bitbucket', 'Git', 'Branch', 'Commit', 'Pull', 'Request',
    'Merge', 'Rebase', 'Tag', 'Release', 'Fork',

    # Package Managers
    'npm', 'yarn', 'pnpm', 'bun', 'pip', 'poetry', 'cargo', 'maven',

    # Tools & IDEs
    'VSCode', 'WebStorm', 'IntelliJ', 'Sublime', 'Vim', 'IDE', 'Terminal', 'Console',
    'bash', 'zsh', 'sh', 'powershell', 'cmd',

    # Flowise-specific
    'flow', 'workflow', 'canvas', 'node', 'edge', 'connection', 'endpoint', 'component',
    'integration', 'input', 'output', 'parameter', 'property', 'attribute', 'handler',
    'callback', 'promise', 'async', 'await',

    # Data & Serialization
    'Schema', 'Table', 'Row', 'Column', 'Index', 'Query', 'Transaction', 'ACID', 'CAP',
    'Serialization', 'Deserialization', 'Parser', 'Formatter',

    # Deployment & Operations
    'Deployment', 'Environment', 'Production', 'Staging', 'Development', 'CI', 'CD',
    'Pipeline', 'Build', 'Test', 'Release', 'Rollback', 'Version', 'Scaling',

    # Request/Response
    'request', 'response', 'status', 'code', 'header', 'body', 'payload', 'stream',
    'event', 'hook', 'middleware', 'plugin', 'extension', 'adapter',

    # Code Structure
    'function', 'method', 'property', 'class', 'interface', 'type', 'implementation',
    'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'object', 'instance',
    'prototype', 'closure', 'scope', 'variable', 'constant', 'parameter', 'argument',

    # Design Patterns
    'pattern', 'strategy', 'factory', 'singleton', 'observer', 'decorator', 'builder',
    'adapter', 'proxy', 'state', 'iterator', 'template', 'composite', 'bridge',

    # File & Path Related
    'path', 'directory', 'folder', 'file', 'filename', 'extension', 'repository',
    'module', 'package', 'library', 'dependency', 'version',
}

def extract_code_blocks(content: str) -> Tuple[str, dict]:
    """Extract code blocks from markdown to preserve them."""
    code_blocks = {}
    counter = 0

    # Match all code blocks (triple backticks)
    pattern = r'```(?:[a-zA-Z0-9_\-+]*\n)?(.*?)```'

    def replace_code(match):
        nonlocal counter
        placeholder = f"__CODE_BLOCK_{counter}__"
        code_blocks[placeholder] = match.group(0)
        counter += 1
        return placeholder

    content_without_code = re.sub(pattern, replace_code, content, flags=re.DOTALL)

    # Handle inline code (single backticks) - be careful with URLs
    pattern_inline = r'(?<![:/])`([^`\n]+)`(?!(?:[a-zA-Z0-9]|/))'

    def replace_inline_code(match):
        nonlocal counter
        placeholder = f"__INLINE_CODE_{counter}__"
        code_blocks[placeholder] = match.group(0)
        counter += 1
        return placeholder

    content_without_code = re.sub(pattern_inline, replace_inline_code, content_without_code)

    return content_without_code, code_blocks

def restore_code_blocks(content: str, code_blocks: dict) -> str:
    """Restore code blocks back into the translated content."""
    for placeholder, code in code_blocks.items():
        content = content.replace(placeholder, code)
    return content

def build_technical_terms_str(max_items: int = 150) -> str:
    """Build a comma-separated string of technical terms."""
    terms_list = sorted(list(TECHNICAL_TERMS))
    return ", ".join(terms_list[:max_items])

def translate_content(client: anthropic.Anthropic, content: str, file_path: str) -> Optional[str]:
    """Translate English markdown content to Korean using Claude API."""

    # Extract code blocks first
    content_without_code, code_blocks = extract_code_blocks(content)

    # Build technical terms preservation instruction
    tech_terms_str = build_technical_terms_str()

    translation_prompt = f"""You are a professional Korean translator specializing in technical documentation.

Translate the following English technical documentation to Korean.

CRITICAL RULES:
1. Translate ALL non-code text to Korean (headings, paragraphs, lists, table cells, captions)
2. PRESERVE these technical terms in English: {tech_terms_str}
3. Preserve ALL markdown formatting exactly (# ## ###, -, *, **, [text](url), |, ```, etc.)
4. Keep URLs and file paths unchanged
5. For links [text](url): translate text only, keep URL unchanged
6. Keep placeholder markers __CODE_BLOCK_0__ as-is
7. For tables: translate content, keep table structure unchanged

Content to translate:
---
{content_without_code}
---

Provide ONLY the translated content. No explanations."""

    # Call Claude API with streaming
    translated = ""
    try:
        with client.messages.stream(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4000,
            messages=[
                {
                    "role": "user",
                    "content": translation_prompt
                }
            ]
        ) as stream:
            for text in stream.text_stream:
                translated += text

        # Restore code blocks
        translated = restore_code_blocks(translated, code_blocks)
        return translated

    except Exception as e:
        print(f"  API Error: {str(e)[:100]}")
        return None

def process_files(client: anthropic.Anthropic) -> Tuple[int, int, int]:
    """Process all English markdown files and create Korean translations."""

    # Get all English markdown files
    all_files = sorted(EN_DIR.rglob("*.md"))

    print(f"Found {len(all_files)} markdown files to process")
    print(f"Source: {EN_DIR}")
    print(f"Target: {KO_DIR}")
    print(f"\nStarting translation...\n")

    successful = 0
    failed = 0
    skipped = 0
    failed_files = []

    for idx, en_file in enumerate(all_files, 1):
        try:
            rel_path = en_file.relative_to(EN_DIR)
            ko_file = KO_DIR / rel_path

            # Skip .gitbook directory
            if '.gitbook' in en_file.parts:
                skipped += 1
                continue

            # Show progress
            status = f"[{idx}/{len(all_files)}] {rel_path}"
            print(status, end="", flush=True)

            # Read English file
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Translate content
            translated_content = translate_content(client, content, str(en_file))

            if translated_content is None:
                raise Exception("Translation returned None")

            # Create directory if it doesn't exist
            ko_file.parent.mkdir(parents=True, exist_ok=True)

            # Write translated content
            with open(ko_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print(" ✓")
            successful += 1

        except Exception as e:
            failed += 1
            error_msg = str(e)[:80]
            failed_files.append((str(rel_path), error_msg))
            print(f" ✗ ({error_msg})")

    # Print summary
    print(f"\n{'='*80}")
    print(f"Translation Summary:")
    print(f"{'='*80}")
    print(f"Successfully translated: {successful}")
    print(f"Failed:                  {failed}")
    print(f"Skipped:                 {skipped}")
    print(f"Total processed:         {successful + failed + skipped}")

    if failed_files and failed <= 10:
        print(f"\nFailed files:")
        for file_path, error in failed_files:
            print(f"  - {file_path}: {error}")

    return successful, failed, skipped

def main():
    # Initialize Anthropic client
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("\nTo use this script, set your API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("\nThen run: python3 translate_to_korean.py")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Check directories
    if not EN_DIR.exists():
        print(f"Error: English directory not found: {EN_DIR}")
        sys.exit(1)

    if not KO_DIR.exists():
        KO_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created Korean directory: {KO_DIR}\n")

    # Process all files
    successful, failed, skipped = process_files(client)

    print(f"\n{'='*80}")
    if failed == 0:
        print("✓ All translations completed successfully!")
        print(f"  {successful} files translated to Korean")
        return 0
    else:
        print(f"⚠ Translation completed with {failed} error(s)")
        print(f"  {successful} files translated successfully")
        return 1

if __name__ == "__main__":
    sys.exit(main())
