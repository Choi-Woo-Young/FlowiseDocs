#!/usr/bin/env python3
"""
Batch translate 55 Flowise documentation files from English to Korean.
Processes files sequentially using Claude API.
"""
import os
import json
import sys
import re
from pathlib import Path
from datetime import datetime

try:
    import anthropic
except ImportError:
    print("Installing anthropic package...")
    os.system("pip install anthropic -q")
    import anthropic

# Files to translate (batch 3)
FILES_TO_TRANSLATE = [
    "integrations/langchain/tools/pipedream-mcp-user-guide-1.md",
    "integrations/langchain/tools/pipedream-mcp-user-guide.md",
    "integrations/langchain/tools/python-interpreter.md",
    "integrations/langchain/tools/read-file.md",
    "integrations/langchain/tools/README.md",
    "integrations/langchain/tools/request-get.md",
    "integrations/langchain/tools/request-post.md",
    "integrations/langchain/tools/retriever-tool.md",
    "integrations/langchain/tools/searchapi.md",
    "integrations/langchain/tools/searxng.md",
    "integrations/langchain/tools/serper.md",
    "integrations/langchain/tools/serpapi.md",
    "integrations/langchain/tools/slack.md",
    "integrations/langchain/tools/sql-database-chain.md",
    "integrations/langchain/tools/vectara-rag.md",
    "integrations/langchain/tools/weather.md",
    "integrations/langchain/vector-stores/README.md",
    "integrations/langchain/vector-stores/astra-db.md",
    "integrations/langchain/vector-stores/faiss.md",
    "integrations/langchain/vector-stores/milvus.md",
    "integrations/langchain/vector-stores/mongodb-atlas.md",
    "integrations/langchain/vector-stores/neo4j.md",
    "integrations/langchain/vector-stores/pinecone.md",
    "integrations/langchain/vector-stores/postgres.md",
    "integrations/langchain/vector-stores/qdrant.md",
    "integrations/langchain/vector-stores/supabase.md",
    "integrations/langchain/vector-stores/vespa.md",
    "integrations/langchain/vector-stores/weaviate.md",
    "integrations/langchain/vector-stores/zcxvf.md",
    "configuration/deployment/aws.md",
    "configuration/deployment/azure.md",
    "configuration/deployment/digital-ocean.md",
    "configuration/deployment/gcp.md",
    "configuration/deployment/heroku.md",
    "configuration/deployment/huggingface.md",
    "configuration/deployment/railway.md",
    "configuration/deployment/render.md",
    "configuration/deployment/replit.md",
    "configuration/deployment/vercel.md",
    "configuration/deployment/README.md",
    "api-reference/README.md",
    "api-reference/assistants.md",
    "api-reference/attachments.md",
    "api-reference/chat-message.md",
    "api-reference/chatflows.md",
    "api-reference/predictions.md",
    "api-reference/tool-use.md",
    "api-reference/uploads.md",
    "using-flowise/agentflowv1.md",
    "using-flowise/agentflowv2.md",
    "using-flowise/document-stores.md",
]


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            return parts[1], parts[2]
    return None, content


def parse_frontmatter(frontmatter_str):
    """Parse YAML-like frontmatter into a dictionary."""
    frontmatter = {}
    if not frontmatter_str:
        return frontmatter

    for line in frontmatter_str.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip().strip('"\'')
    return frontmatter


def build_frontmatter(frontmatter_dict):
    """Build frontmatter string from dictionary."""
    if not frontmatter_dict:
        return ""

    lines = []
    for key, value in frontmatter_dict.items():
        if value:
            lines.append(f'{key}: "{value}"')
    return "\n".join(lines)


def preserve_code_blocks(content):
    """Extract code blocks and replace with placeholders."""
    code_blocks = []
    pattern = r'```[\s\S]*?```'

    def replace_block(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks) - 1}__"

    content = re.sub(pattern, replace_block, content)
    return content, code_blocks


def restore_code_blocks(content, code_blocks):
    """Restore code blocks from placeholders."""
    for i, block in enumerate(code_blocks):
        content = content.replace(f"__CODE_BLOCK_{i}__", block)
    return content


def preserve_urls(content):
    """Replace URLs with placeholders."""
    urls = []
    pattern = r'https?://[^\s\)\]\}\|]*'

    def replace_url(match):
        urls.append(match.group(0))
        return f"__URL_{len(urls) - 1}__"

    content = re.sub(pattern, replace_url, content)
    return content, urls


def restore_urls(content, urls):
    """Restore URLs from placeholders."""
    for i, url in enumerate(urls):
        content = content.replace(f"__URL_{i}__", url)
    return content


def translate_with_claude(text, client):
    """Translate text using Claude API."""
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"""Please translate the following markdown content from English to Korean.

IMPORTANT RULES:
1. Keep code blocks exactly as-is (including ```code``` markers)
2. Keep URLs unchanged
3. Keep image paths like .gitbook/assets/... unchanged
4. Keep technical terms in English (Flowise, API, RAG, LLM, Node, OAuth, etc)
5. Keep HTML tags structure unchanged, only translate alt text
6. Translate all headings, body text, and table contents to Korean
7. Preserve frontmatter structure, only translate description values
8. For __URL_N__ and __CODE_BLOCK_N__ placeholders, keep them as-is during translation

CONTENT TO TRANSLATE:
{text}

TRANSLATED CONTENT (Korean):"""
            }
        ]
    )

    return message.content[0].text


def translate_file(en_path, ko_path, client):
    """Translate a single file from English to Korean."""
    try:
        # Read English file
        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract frontmatter
        frontmatter_str, body = extract_frontmatter(content)

        # Parse frontmatter
        frontmatter = parse_frontmatter(frontmatter_str)

        # Preserve code blocks and URLs
        body, code_blocks = preserve_code_blocks(body)
        body, urls = preserve_urls(body)

        # Combine for translation
        full_text = body
        if frontmatter_str:
            full_text = f"FRONTMATTER:\n{frontmatter_str}\n\nBODY:\n{body}"

        # Translate
        translated = translate_with_claude(full_text, client)

        # Process translated content
        if "FRONTMATTER:" in translated:
            parts = translated.split("BODY:", 1)
            if len(parts) == 2:
                translated_fm = parts[0].replace("FRONTMATTER:", "").strip()
                translated_body = parts[1].strip()
            else:
                translated_fm = frontmatter_str
                translated_body = translated
        else:
            translated_fm = frontmatter_str
            translated_body = translated

        # Restore code blocks and URLs
        translated_body = restore_code_blocks(translated_body, code_blocks)
        translated_body = restore_urls(translated_body, urls)

        # Rebuild content with frontmatter
        if translated_fm:
            final_content = f"---\n{translated_fm}\n---\n{translated_body}"
        else:
            final_content = translated_body

        # Ensure ko directory exists
        ko_dir = os.path.dirname(ko_path)
        os.makedirs(ko_dir, exist_ok=True)

        # Write Korean file
        with open(ko_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        return True, None

    except Exception as e:
        return False, str(e)


def main():
    """Main translation function."""
    base_en_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
    base_ko_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

    # Initialize Anthropic client
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    status = {
        "batch": 3,
        "timestamp": datetime.now().isoformat(),
        "total": len(FILES_TO_TRANSLATE),
        "translated": 0,
        "failed": 0,
        "files": []
    }

    print(f"=== Batch 3 Translation (55 files) ===\n")

    for i, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        en_file = os.path.join(base_en_dir, file_path)
        ko_file = os.path.join(base_ko_dir, file_path)

        # Check if English file exists
        if not os.path.exists(en_file):
            status["files"].append({
                "index": i,
                "path": file_path,
                "status": "skipped",
                "reason": "English file not found"
            })
            print(f"[{i:2d}/{len(FILES_TO_TRANSLATE)}] SKIP: {file_path} (source not found)")
            continue

        # Translate file
        print(f"[{i:2d}/{len(FILES_TO_TRANSLATE)}] TRANSLATING: {file_path}...", end=" ", flush=True)
        success, error = translate_file(en_file, ko_file, client)

        if success:
            status["translated"] += 1
            status["files"].append({
                "index": i,
                "path": file_path,
                "status": "translated"
            })
            print("✓")
        else:
            status["failed"] += 1
            status["files"].append({
                "index": i,
                "path": file_path,
                "status": "error",
                "error": error
            })
            print(f"✗ ({error})")

    # Save status
    status_file = os.path.join(base_ko_dir, "../.translation_status_batch3.json")
    with open(status_file, 'w') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)

    # Print summary
    print(f"\n=== Translation Summary ===")
    print(f"배치 3 완료: {status['translated']}개 파일")
    print(f"Failed: {status['failed']}")
    print(f"Total: {status['total']}")

    if status['translated'] > 0:
        print(f"\nStatus saved to: {status_file}")

    return status['translated']


if __name__ == "__main__":
    translated_count = main()
    sys.exit(0 if translated_count > 0 else 1)
