#!/usr/bin/env python3
"""
Translate all 126 Flowise documentation files from English to Korean
Uses Anthropic API to translate while preserving code blocks, URLs, and technical terms.

Usage:
    export ANTHROPIC_API_KEY="sk-..."
    python3 translate_all_126.py

This script:
- Reads English files from en/ directory
- Translates narrative text to Korean
- Preserves code blocks, URLs, and technical terms
- Writes translated files to ko/ directory
- Tracks progress with JSON status file
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime

# Import Anthropic
try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: Please install anthropic: pip install anthropic")
    sys.exit(1)

# Configuration
EN_DIR = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en")
KO_DIR = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko")
STATUS_FILE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/.translation_complete_status.json")

# List of all files that exist and need translation (101 files verified to exist)
ALL_FILES = [
    "migration-guide/v1.3.0-migration-guide.md",
    "migration-guide/v1.4.3-migration-guide.md",
    "migration-guide/v2.1.4-migration-guide.md",
    "text-splitters/charater-text-splitter.md",
    "tutorials/README.md",
    "tutorials/customer-support.md",
    "tutorials/deep-research.md",
    "tutorials/human-in-the-loop.md",
    "tutorials/interacting-with-api.md",
    "tutorials/sql-agent.md",
    "tutorials/tools-and-mcp.md",
    "use-cases/README.md",
    "use-cases/interacting-with-api.md",
    "use-cases/multiple-documents-qna.md",
    "use-cases/sql-qna.md",
    "use-cases/upserting-data.md",
    "use-cases/web-scrape-qna.md",
    "use-cases/webhook-tool.md",
    "using-flowise/README.md",
    "integrations/langchain/agents/airtable-agent.md",
    "integrations/langchain/agents/conversational-agent.md",
    "integrations/langchain/agents/conversational-retrieval-agent.md",
    "integrations/langchain/agents/mistralai-tool-agent.md",
    "integrations/langchain/agents/openai-function-agent.md",
    "integrations/langchain/agents/openai-tool-agent.md",
    "integrations/langchain/agents/react-agent-chat.md",
    "integrations/langchain/agents/react-agent-llm.md",
    "integrations/langchain/agents/tool-agent.md",
    "integrations/langchain/agents/xml-agent.md",
    "integrations/langchain/cache/in-memory-cache.md",
    "integrations/langchain/cache/inmemory-embedding-cache.md",
    "integrations/langchain/cache/momento-cache.md",
    "integrations/langchain/cache/redis-cache.md",
    "integrations/langchain/cache/redis-embeddings-cache.md",
    "integrations/langchain/cache/upstash-redis-cache.md",
    "integrations/langchain/chains/conversation-chain.md",
    "integrations/langchain/chains/conversational-retrieval-qa-chain.md",
    "integrations/langchain/chains/get-api-chain.md",
    "integrations/langchain/chains/llm-chain.md",
    "integrations/langchain/chains/multi-prompt-chain.md",
    "integrations/langchain/chains/multi-retrieval-qa-chain.md",
    "integrations/langchain/chains/openapi-chain.md",
    "integrations/langchain/chains/post-api-chain.md",
    "integrations/langchain/chains/retrieval-qa-chain.md",
    "integrations/langchain/chains/sql-database-chain.md",
    "integrations/langchain/chains/vectordb-qa-chain.md",
    "integrations/langchain/chat-models/aws-chatbedrock.md",
    "integrations/langchain/chat-models/azure-chatopenai-1.md",
    "integrations/langchain/chat-models/chat-fireworks.md",
    "integrations/langchain/chat-models/chat-sambanova.md",
    "integrations/langchain/chat-models/chatanthropic.md",
    "integrations/langchain/chat-models/chatcohere.md",
    "integrations/langchain/chat-models/chatcometapi.md",
    "integrations/langchain/chat-models/chathuggingface.md",
    "integrations/langchain/chat-models/google-vertexai.md",
    "integrations/langchain/chat-models/groqchat.md",
    "integrations/langchain/chat-models/ibm-watsonx.md",
    "integrations/langchain/chat-models/mistral-ai.md",
    "integrations/langchain/chat-models/nvidia-nim.md",
    "integrations/langchain/moderation/README.md",
    "integrations/langchain/moderation/openai-moderation.md",
    "integrations/langchain/moderation/simple-prompt-moderation.md",
    "integrations/langchain/output-parsers/README.md",
    "integrations/langchain/output-parsers/advanced-structured-output-parser.md",
    "integrations/langchain/output-parsers/csv-output-parser.md",
    "integrations/langchain/output-parsers/custom-list-output-parser.md",
    "integrations/langchain/output-parsers/structured-output-parser.md",
    "integrations/langchain/prompts/README.md",
    "integrations/langchain/prompts/chat-prompt-template.md",
    "integrations/langchain/prompts/few-shot-prompt-template.md",
    "integrations/langchain/prompts/prompt-template.md",
    "integrations/langchain/record-managers.md",
    "integrations/langchain/retrievers/README.md",
    "integrations/langchain/retrievers/cohere-rerank-retriever.md",
    "integrations/langchain/retrievers/custom-retriever.md",
    "integrations/langchain/retrievers/embeddings-filter-retriever.md",
    "integrations/langchain/text-splitters/README.md",
    "integrations/langchain/text-splitters/character-text-splitter.md",
    "integrations/langchain/text-splitters/html-to-markdown-text-splitter.md",
    "integrations/langchain/text-splitters/recursive-character-text-splitter.md",
    "integrations/langchain/tools/README.md",
    "integrations/langchain/tools/custom-tool.md",
    "integrations/langchain/tools/python-interpreter.md",
    "integrations/langchain/tools/read-file.md",
    "integrations/langchain/tools/serper.md",
    "integrations/langchain/tools/tavily-ai.md",
    "integrations/langchain/tools/write-file.md",
    "integrations/langchain/vector-stores/README.md",
    "integrations/langchain/vector-stores/chroma.md",
    "integrations/langchain/vector-stores/faiss.md",
    "integrations/langchain/vector-stores/milvus.md",
    "integrations/langchain/vector-stores/mongodb-atlas.md",
    "integrations/langchain/vector-stores/pinecone.md",
    "integrations/langchain/vector-stores/postgres.md",
    "integrations/langchain/vector-stores/qdrant.md",
    "integrations/langchain/vector-stores/supabase.md",
    "integrations/langchain/vector-stores/vectara.md",
    "integrations/langchain/vector-stores/weaviate.md",
    "integrations/utilities/loop-controller.md",
    "integrations/utilities/search-api.md",
    "integrations/utilities/webhook.md",
    "integrations/3rd-party-platform-integration/README.md",
    "integrations/3rd-party-platform-integration/streamlit.md",
    "integrations/3rd-party-platform-integration/zapier-zaps.md",
]

def load_status() -> Dict:
    """Load translation progress status"""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"completed": [], "failed": [], "skipped": []}

def save_status(status: Dict):
    """Save translation progress status"""
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)

def split_markdown(content: str) -> Tuple[str, str, str]:
    """Split markdown into frontmatter, code blocks, and narrative"""
    frontmatter = ""

    # Extract YAML frontmatter
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1].strip()
            content = parts[2].lstrip("\n")

    # Extract code blocks
    code_blocks = {}
    code_pattern = r'```[\s\S]*?```'
    for i, match in enumerate(re.finditer(code_pattern, content)):
        placeholder = f"__CODE_BLOCK_{i}__"
        code_blocks[placeholder] = match.group(0)

    # Replace with placeholders
    narrative = content
    for placeholder, code in code_blocks.items():
        narrative = narrative.replace(code, placeholder)

    return frontmatter, json.dumps(code_blocks, ensure_ascii=False), narrative

def restore_markdown(frontmatter: str, code_blocks_json: str, narrative: str) -> str:
    """Restore markdown from components"""
    code_blocks = json.loads(code_blocks_json)

    result = narrative
    for placeholder, code in code_blocks.items():
        result = result.replace(placeholder, code)

    if frontmatter.strip():
        return "---\n" + frontmatter + "\n---\n" + result
    return result

def translate_narrative(client: Anthropic, narrative: str, code_blocks_json: str) -> str:
    """Translate narrative to Korean using Claude"""
    if not narrative.strip():
        return narrative

    code_blocks = json.loads(code_blocks_json)
    placeholders = list(code_blocks.keys()) if code_blocks else []

    prompt = f"""Translate this markdown content to Korean. Follow these rules:

RULES:
1. Translate ALL narrative text, descriptions, and instructions to fluent Korean
2. PRESERVE these placeholders EXACTLY (do NOT translate): {', '.join(placeholders) if placeholders else 'none'}
3. PRESERVE all URLs, links, and file paths
4. PRESERVE technical terms in English: API, LLM, RAG, Node, Agent, Tool, Flow, JSON, XML, HTML, OpenAI, Claude, Anthropic, Flowise, etc.
5. PRESERVE markdown formatting (headers #, bold **, lists, tables, etc.)
6. Keep exact structure and line breaks
7. Translate table content to Korean
8. Keep image alt text as-is

CONTENT:

{narrative}

Return ONLY the translated Korean text."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

def translate_file(client: Anthropic, en_path: Path, ko_path: Path) -> bool:
    """Translate a single file"""
    try:
        # Read English file
        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split content
        frontmatter, code_blocks_json, narrative = split_markdown(content)

        # Translate
        translated_narrative = translate_narrative(client, narrative, code_blocks_json)

        # Restore
        translated = restore_markdown(frontmatter, code_blocks_json, translated_narrative)

        # Write to Korean directory
        ko_path.parent.mkdir(parents=True, exist_ok=True)
        with open(ko_path, 'w', encoding='utf-8') as f:
            f.write(translated)

        return True
    except Exception as e:
        print(f"    Error: {e}")
        return False

def main():
    # Check API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set")
        print("\nSet it with:")
        print("  export ANTHROPIC_API_KEY='sk-...'")
        sys.exit(1)

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load status
    status = load_status()

    # Prepare file list
    to_process = [f for f in ALL_FILES if f not in status["completed"] and (EN_DIR / f).exists()]

    print("\n" + "=" * 80)
    print("Flowise Documentation Korean Translation - Final Batch (126 files)")
    print("=" * 80)
    print(f"Total files to process: {len(to_process)}")
    print(f"Already completed: {len(status['completed'])}")
    print(f"Failed: {len(status['failed'])}")
    print("-" * 80 + "\n")

    if not to_process:
        print("All files completed!")
        return

    # Translate each file
    for i, file_path in enumerate(to_process, 1):
        en_file = EN_DIR / file_path
        ko_file = KO_DIR / file_path

        print(f"[{i}/{len(to_process)}] {file_path}...", end=" ", flush=True)

        if translate_file(client, en_file, ko_file):
            print("✓")
            status["completed"].append(file_path)
        else:
            print("✗")
            status["failed"].append(file_path)

        save_status(status)
        time.sleep(0.3)  # Rate limiting

    # Summary
    print("\n" + "-" * 80)
    print("TRANSLATION COMPLETE")
    print("-" * 80)
    print(f"Completed: {len(status['completed'])}")
    print(f"Failed: {len(status['failed'])}")
    print(f"Status: {STATUS_FILE}")

if __name__ == "__main__":
    main()
