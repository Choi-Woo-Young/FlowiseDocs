#!/usr/bin/env python3
"""
Korean Translation for Flowise Documentation - Final Batch (126 files)
======================================================================

This script translates 126 Flowise documentation files from English to Korean.
It preserves code blocks, URLs, technical terms, and markdown formatting.

Usage:
    export ANTHROPIC_API_KEY="sk-..."
    python3 translate_final_batch.py

Features:
- Translates narrative text to fluent Korean
- Preserves code blocks, URLs, and technical terms in English
- Maintains markdown formatting exactly
- Progress tracking with JSON status file
- Resume capability for interrupted runs
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from typing import Dict, Tuple, List
from datetime import datetime

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic module not installed")
    print("Install it with: pip install anthropic")
    sys.exit(1)

# Configuration
EN_DIR = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en")
KO_DIR = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko")
STATUS_FILE = Path("/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/.translation_batch_final.json")

# All files to translate (126 files)
FILES_TO_TRANSLATE = [
    # Batch 3 (63 files)
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
    # Batch 4 (63 files)
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

# Files that may not exist - will be skipped
OPTIONAL_FILES = {
    "integrations/langchain/retrievers/llama-index-retriever.md",
    "integrations/langchain/retrievers/tavily-search-retriever.md",
    "integrations/langchain/text-splitters/charater-text-splitter.md",
    "integrations/langchain/text-splitters/markdown-header-text-splitter.md",
    "integrations/langchain/tools/bing-search.md",
    "integrations/langchain/tools/duckduckgo-search.md",
    "integrations/langchain/tools/google-search.md",
    "integrations/langchain/tools/jina-reader.md",
    "integrations/langchain/tools/metaphor-search.md",
    "integrations/langchain/tools/request.md",
    "integrations/langchain/vector-stores/airtable.md",
    "integrations/langchain/vector-stores/mongo-db-atlas.md",
    "integrations/langchain/vector-stores/myscale.md",
    "integrations/3rd-party-platform-integration/flowise-on-vercel.md",
    "integrations/3rd-party-platform-integration/flowise-on-bubble.md",
    "integrations/3rd-party-platform-integration/flowise-on-zapier.md",
    "integrations/3rd-party-platform-integration/firecrawl.md",
    "integrations/3rd-party-platform-integration/pipedream.md",
    "integrations/3rd-party-platform-integration/n8n.md",
    "integrations/3rd-party-platform-integration/make-formerly-integromat.md",
    "integrations/3rd-party-platform-integration/discord-chatbot.md",
    "integrations/3rd-party-platform-integration/slack-chatbot.md",
    "integrations/3rd-party-platform-integration/telegram-chatbot.md",
    "integrations/3rd-party-platform-integration/telegram-bot-with-streaming.md",
    "integrations/3rd-party-platform-integration/telegram-bot-with-streaming-2.md",
    "integrations/3rd-party-platform-integration/whatsapp-chatbot.md",
}

def load_status() -> Dict:
    """Load translation status from file"""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {"completed": [], "failed": [], "skipped": [], "start_time": datetime.now().isoformat()}

def save_status(status: Dict):
    """Save translation status to file"""
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)

def split_markdown(content: str) -> Tuple[str, str, str]:
    """
    Split markdown into frontmatter, code blocks placeholder, and narrative.
    Returns: (frontmatter, code_blocks_json, narrative)
    """
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

    # Replace code blocks with placeholders
    narrative = content
    for placeholder, code in code_blocks.items():
        narrative = narrative.replace(code, placeholder)

    return frontmatter, json.dumps(code_blocks, ensure_ascii=False), narrative

def restore_markdown(frontmatter: str, code_blocks_json: str, narrative: str) -> str:
    """Restore markdown from separated parts"""
    code_blocks = json.loads(code_blocks_json)

    # Restore code blocks
    result = narrative
    for placeholder, code in code_blocks.items():
        result = result.replace(placeholder, code)

    # Restore frontmatter
    if frontmatter.strip():
        return "---\n" + frontmatter + "\n---\n" + result
    return result

def translate_narrative(client: Anthropic, narrative: str, code_blocks_json: str) -> str:
    """Use Claude to translate narrative text to Korean"""
    if not narrative.strip():
        return narrative

    code_blocks = json.loads(code_blocks_json)

    prompt = f"""Translate this markdown content to Korean. Follow these rules strictly:

TRANSLATION RULES:
1. Translate ALL narrative text, descriptions, headings, and instructions to FLUENT KOREAN
2. PRESERVE these placeholders exactly (do NOT translate): {', '.join(code_blocks.keys()) if code_blocks else 'none'}
3. PRESERVE all URLs, links, file paths, and API endpoints
4. PRESERVE technical terms in English: API, LLM, RAG, Node, Agent, Tool, Chain, Flow, JSON, XML, HTML, OpenAI, Claude, Anthropic, Flowise, etc.
5. PRESERVE markdown formatting (headers #, lists, bold **, italic *, code backticks, tables, etc.)
6. Keep the exact same structure and line breaks
7. Translate table headers and content to Korean
8. Keep image alt text as is (but translate captions)
9. Preserve all links in their original form [text](url)

CONTENT TO TRANSLATE:

{narrative}

IMPORTANT: Return ONLY the translated Korean content. Do not add explanations or comments."""

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text

def translate_file(client: Anthropic, en_path: Path, ko_path: Path) -> bool:
    """Translate a single file from English to Korean"""
    try:
        # Read source file
        with open(en_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split into components
        frontmatter, code_blocks_json, narrative = split_markdown(content)

        # Translate narrative
        translated_narrative = translate_narrative(client, narrative, code_blocks_json)

        # Restore complete content
        translated_content = restore_markdown(frontmatter, code_blocks_json, translated_narrative)

        # Create output directory
        ko_path.parent.mkdir(parents=True, exist_ok=True)

        # Write translated file
        with open(ko_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True
    except Exception as e:
        print(f"  ERROR: {str(e)}")
        return False

def main():
    # Check API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable is not set")
        print("\nTo set it:")
        print("  export ANTHROPIC_API_KEY='sk-...'")
        sys.exit(1)

    # Initialize client
    client = Anthropic(api_key=api_key)

    # Load status
    status = load_status()

    # Build list of files to process
    files_to_process = []
    for file_path in FILES_TO_TRANSLATE:
        en_file = EN_DIR / file_path

        if file_path in status["completed"]:
            continue

        if not en_file.exists():
            if file_path not in OPTIONAL_FILES:
                print(f"WARNING: Source file not found: {file_path}")
            status["skipped"].append(file_path)
            continue

        files_to_process.append(file_path)

    total = len(files_to_process)
    print("\n" + "=" * 70)
    print("Flowise Documentation Korean Translation - Final Batch")
    print("=" * 70)
    print(f"Files to translate: {total}")
    print(f"Already completed: {len(status['completed'])}")
    print(f"Skipped (not found): {len(status['skipped'])}")
    print("-" * 70 + "\n")

    if total == 0:
        print("All files have been translated!")
        sys.exit(0)

    # Translate files
    completed = 0
    failed = 0

    for i, file_path in enumerate(files_to_process, 1):
        en_file = EN_DIR / file_path
        ko_file = KO_DIR / file_path

        print(f"[{i}/{total}] Translating {file_path}...", end=" ", flush=True)

        if translate_file(client, en_file, ko_file):
            print("✓")
            status["completed"].append(file_path)
            completed += 1
        else:
            print("✗")
            status["failed"].append(file_path)
            failed += 1

        # Save status after each file
        save_status(status)

        # Rate limiting
        time.sleep(0.5)

    # Final report
    print("\n" + "-" * 70)
    print("TRANSLATION SUMMARY")
    print("-" * 70)
    print(f"Completed: {completed}/{total}")
    print(f"Failed: {failed}/{total}")
    print(f"Skipped: {len(status['skipped'])}")
    print(f"Total: {len(status['completed']) + len(status['skipped']) + failed}")
    print(f"\nStatus saved to: {STATUS_FILE}")

    if failed > 0:
        print(f"\nFailed files ({len(status['failed'])}):")
        for f in status['failed']:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
