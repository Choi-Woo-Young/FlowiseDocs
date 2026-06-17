#!/usr/bin/env python3
"""
Translate Flowise batch 2 (57 files) from English to Korean
Files are already in ko/ directory but contain English content
"""

import os
import sys
import re
from pathlib import Path
from typing import Tuple, Optional, List
import anthropic

# Technical terms that should NOT be translated
TECHNICAL_TERMS = {
    'API', 'LLM', 'RAG', 'Node', 'Agent', 'Tool', 'Flowise', 'JSON', 'HTTP', 'REST',
    'CLI', 'SDK', 'Docker', 'Kubernetes', 'AWS', 'Azure', 'GCP', 'OCI',
    'Redis', 'PostgreSQL', 'MongoDB', 'MySQL', 'Postgres', 'SQLite', 'Elasticsearch',
    'Cassandra', 'DynamoDB', 's3', 'GCS', 'Blob',
    'JavaScript', 'TypeScript', 'Python', 'Node.js', 'Express', 'React', 'Vue', 'Angular',
    'FastAPI', 'Django', 'Flask', 'Spring', 'Boot', 'Gradle',
    'OpenAI', 'Anthropic', 'Claude', 'GPT', 'LLAMA', 'Gemini', 'Vertex', 'Bedrock',
    'Vector', 'Embedding', 'Langchain', 'LlamaIndex', 'Hugging', 'Face', 'HuggingFace',
    'BullMQ', 'Kafka', 'RabbitMQ', 'Pub/Sub', 'Topic', 'Queue', 'Message', 'Consumer',
    'SSE', 'WebSocket', 'Webhook', 'OAuth', 'JWT', 'CORS', 'SSL', 'TLS', 'HTTP2',
    'GraphQL', 'SAML', 'LDAP', 'gRPC',
    'Container', 'Image', 'Volume', 'Network', 'Service', 'Pod', 'Deployment', 'Ingress',
    'LoadBalancer', 'StatefulSet', 'DaemonSet', 'CronJob', 'ConfigMap', 'Secret',
    'PersistentVolume', 'StorageClass', 'Registry',
    'GitHub', 'GitLab', 'Bitbucket', 'Git', 'Branch', 'Commit', 'Pull', 'Request',
    'Merge', 'Rebase', 'Tag', 'Release', 'Fork',
    'npm', 'yarn', 'pnpm', 'bun', 'pip', 'poetry', 'cargo', 'maven',
    'VSCode', 'WebStorm', 'IntelliJ', 'Sublime', 'Vim', 'IDE', 'Terminal', 'Console',
    'bash', 'zsh', 'sh', 'powershell', 'cmd',
    'flow', 'workflow', 'canvas', 'node', 'edge', 'connection', 'endpoint', 'component',
    'integration', 'input', 'output', 'parameter', 'property', 'attribute', 'handler',
    'callback', 'promise', 'async', 'await',
    'Schema', 'Table', 'Row', 'Column', 'Index', 'Query', 'Transaction', 'ACID', 'CAP',
    'Serialization', 'Deserialization', 'Parser', 'Formatter',
    'Deployment', 'Environment', 'Production', 'Staging', 'Development', 'CI', 'CD',
    'Pipeline', 'Build', 'Test', 'Release', 'Rollback', 'Version', 'Scaling',
    'request', 'response', 'status', 'code', 'header', 'body', 'payload', 'stream',
    'event', 'hook', 'middleware', 'plugin', 'extension', 'adapter',
    'function', 'method', 'property', 'class', 'interface', 'type', 'implementation',
    'inheritance', 'polymorphism', 'encapsulation', 'abstraction', 'object', 'instance',
    'prototype', 'closure', 'scope', 'variable', 'constant', 'parameter', 'argument',
    'pattern', 'strategy', 'factory', 'singleton', 'observer', 'decorator', 'builder',
    'adapter', 'proxy', 'state', 'iterator', 'template', 'composite', 'bridge',
    'path', 'directory', 'folder', 'file', 'filename', 'extension', 'repository',
    'module', 'package', 'library', 'dependency', 'version', 'Model', 'Chat', 'Memory',
    'Cohere', 'Mem0', 'Zep', 'Upstash', 'DynamoDB', 'MongoDB', 'Atlas', 'Retriever',
    'Rerank', 'HYDE', 'Reciprocal', 'Rank', 'Fusion', 'Similarity', 'Threshold', 'Filter',
    'Splitter', 'Character', 'Recursive', 'Token', 'HTML', 'Markdown', 'Parser',
    'BraveSearch', 'Browserless', 'MCP', 'Calculator', 'ChatFlow', 'Custom', 'Exa',
    'Gmail', 'Google', 'Calendar', 'Drive', 'Sheets', 'Custom', 'Search', 'Microsoft',
    'Outlook', 'Teams', 'OpenAPI', 'Toolkit', 'Summary', 'Chat', 'Memory', 'Message',
    'Storage', 'Retrieval', 'ID', 'Key', 'LLM', 'Default', 'Display', 'Name', 'Type',
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

    # Handle inline code (single backticks)
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

def build_technical_terms_str(max_items: int = 200) -> str:
    """Build a comma-separated string of technical terms."""
    terms_list = sorted(list(TECHNICAL_TERMS))
    return ", ".join(terms_list[:max_items])

def translate_content(client: anthropic.Anthropic, content: str) -> Optional[str]:
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
8. Use formal, professional Korean tone

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

def process_batch_2_files(client: anthropic.Anthropic) -> Tuple[int, int]:
    """Process the 57 batch 2 files."""

    # Read file list from /tmp/batch_2_files.txt
    with open('/tmp/batch_2_files.txt', 'r') as f:
        files = [line.strip() for line in f if line.strip()]

    files = files[:57]  # Exactly 57 files

    print(f"Processing {len(files)} batch 2 files")
    print(f"Starting translation...\n")

    successful = 0
    failed = 0

    for idx, file_path in enumerate(files, 1):
        try:
            if not os.path.exists(file_path):
                print(f"[{idx:2d}/{len(files)}] {Path(file_path).name} ✗ (file not found)")
                failed += 1
                continue

            # Show progress
            status = f"[{idx:2d}/{len(files)}] {Path(file_path).name}"
            print(status, end="", flush=True)

            # Read file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Translate content
            translated_content = translate_content(client, content)

            if translated_content is None:
                raise Exception("Translation returned None")

            # Write translated content back
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print(" ✓")
            successful += 1

        except Exception as e:
            failed += 1
            error_msg = str(e)[:80]
            print(f" ✗ ({error_msg})")

    # Print summary
    print(f"\n{'='*80}")
    print(f"배치 2 완료: {successful}개 파일")
    print(f"{'='*80}")

    return successful, failed

def main():
    # Initialize Anthropic client
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set")
        print("\nTo use this script, set your API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key-here'")
        print("\nThen run: python3 translate_batch_2_ko.py")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    # Process the batch 2 files
    successful, failed = process_batch_2_files(client)

    if failed == 0:
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
