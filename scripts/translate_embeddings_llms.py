#!/usr/bin/env python3
"""
Translate Embeddings and LLMs files from English to Korean
Processes 21 embeddings files + 8 llms files (29 total)
"""

import os
import sys
import re
from pathlib import Path
from typing import Tuple, Optional, List
import anthropic

# Configuration
EN_DIR = Path(__file__).parent / "en"
KO_DIR = Path(__file__).parent / "ko"

# The files to translate: embeddings (21) + llms (8)
EMBEDDINGS_FILES = [
    "integrations/langchain/embeddings/aws-bedrock-embeddings.md",
    "integrations/langchain/embeddings/azure-openai-embeddings.md",
    "integrations/langchain/embeddings/cohere-embeddings.md",
    "integrations/langchain/embeddings/googlegenerativeai-embeddings.md",
    "integrations/langchain/embeddings/googlevertexai-embeddings.md",
    "integrations/langchain/embeddings/huggingface-inference-embeddings.md",
    "integrations/langchain/embeddings/localai-embeddings.md",
    "integrations/langchain/embeddings/mistralai-embeddings.md",
    "integrations/langchain/embeddings/ollama-embeddings.md",
    "integrations/langchain/embeddings/openai-embeddings-custom.md",
    "integrations/langchain/embeddings/openai-embeddings.md",
    "integrations/langchain/embeddings/togetherai-embedding.md",
    "integrations/langchain/embeddings/voyageai-embeddings.md",
]

LLMS_FILES = [
    "integrations/langchain/llms/aws-bedrock.md",
    "integrations/langchain/llms/azure-openai.md",
    "integrations/langchain/llms/cohere.md",
    "integrations/langchain/llms/googlevertex-ai.md",
    "integrations/langchain/llms/huggingface-inference.md",
    "integrations/langchain/llms/ollama.md",
    "integrations/langchain/llms/openai.md",
    "integrations/langchain/llms/replicate.md",
]

FILES_TO_TRANSLATE = EMBEDDINGS_FILES + LLMS_FILES

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

def process_files(client: anthropic.Anthropic) -> Tuple[int, int, List[Tuple[str, str]]]:
    """Process the files and create Korean translations."""

    print(f"Processing {len(FILES_TO_TRANSLATE)} files")
    print(f"  Embeddings: {len(EMBEDDINGS_FILES)}")
    print(f"  LLMs: {len(LLMS_FILES)}")
    print(f"Source: {EN_DIR}")
    print(f"Target: {KO_DIR}")
    print(f"\nStarting translation...\n")

    successful = 0
    failed = 0
    failed_files = []

    for idx, rel_path in enumerate(FILES_TO_TRANSLATE, 1):
        try:
            en_file = EN_DIR / rel_path
            ko_file = KO_DIR / rel_path

            # Show progress
            status = f"[{idx:2d}/{len(FILES_TO_TRANSLATE)}] {rel_path}"
            print(status, end="", flush=True)

            # Check if English file exists
            if not en_file.exists():
                print(f" ✗ (EN file not found)")
                failed += 1
                failed_files.append((rel_path, "EN file not found"))
                continue

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

            print(" OK")
            successful += 1

        except Exception as e:
            failed += 1
            error_msg = str(e)[:80]
            failed_files.append((rel_path, error_msg))
            print(f" FAIL ({error_msg})")

    # Print summary
    print(f"\n{'='*80}")
    print(f"Translation Summary:")
    print(f"{'='*80}")
    print(f"Successfully translated: {successful}")
    print(f"Failed:                  {failed}")
    print(f"Total processed:         {successful + failed}")

    if failed_files and failed <= 20:
        print(f"\nFailed files:")
        for file_path, error in failed_files:
            print(f"  - {file_path}: {error}")

    return successful, failed, failed_files

def main():
    # Initialize Anthropic client
    try:
        client = anthropic.Anthropic()
    except Exception as e:
        print("Error: Could not initialize Anthropic client")
        print("Make sure ANTHROPIC_API_KEY is set in your environment")
        print(f"Details: {e}")
        sys.exit(1)

    # Check directories
    if not EN_DIR.exists():
        print(f"Error: English directory not found: {EN_DIR}")
        sys.exit(1)

    if not KO_DIR.exists():
        KO_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Created Korean directory: {KO_DIR}\n")

    # Process the files
    successful, failed, failed_files = process_files(client)

    print(f"\n{'='*80}")
    if failed == 0:
        print(f"SUCCESS: All {successful} files translated to Korean!")
        return 0
    else:
        print(f"COMPLETED with {failed} error(s)")
        print(f"  {successful} files translated successfully")
        return 1

if __name__ == "__main__":
    sys.exit(main())
