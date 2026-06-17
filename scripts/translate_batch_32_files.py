#!/usr/bin/env python3
"""
FlowiseDocs Batch 32 Translation Script
Translates 32 specific files from English to Korean using Claude API
"""

import os
import re
from pathlib import Path
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Base directory
BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/"

# List of 32 files to translate
FILES_TO_TRANSLATE = [
    "ko/integrations/langchain/document-loaders/puppeteer-web-scraper.md",
    "ko/integrations/langchain/document-loaders/s3-file-loader.md",
    "ko/integrations/langchain/document-loaders/searchapi-for-web-search.md",
    "ko/integrations/langchain/document-loaders/serpapi-for-web-search.md",
    "ko/integrations/langchain/document-loaders/spider-web-scraper-crawler.md",
    "ko/integrations/langchain/document-loaders/text-file.md",
    "ko/integrations/langchain/document-loaders/unstructured-file-loader.md",
    "ko/integrations/langchain/document-loaders/unstructured-folder-loader.md",
    "ko/integrations/langchain/embeddings/README.md",
    "ko/integrations/langchain/llms/README.md",
    "ko/integrations/langchain/memory/README.md",
    "ko/integrations/langchain/moderation/README.md",
    "ko/integrations/langchain/output-parsers/README.md",
    "ko/integrations/langchain/prompts/README.md",
    "ko/integrations/langchain/retrievers/README.md",
    "ko/integrations/langchain/text-splitters/README.md",
    "ko/integrations/langchain/tools/chatflow-tool.md",
    "ko/integrations/langchain/tools/custom-tool.md",
    "ko/integrations/langchain/tools/exa-search.md",
    "ko/integrations/langchain/tools/gmail.md",
    "ko/integrations/langchain/tools/google-calendar.md",
    "ko/integrations/langchain/tools/google-custom-search.md",
    "ko/integrations/langchain/tools/google-drive.md",
    "ko/integrations/langchain/tools/google-sheets.md",
    "ko/integrations/langchain/tools/microsoft-outlook.md",
    "ko/integrations/langchain/tools/microsoft-teams.md",
    "ko/integrations/langchain/tools/openapi-toolkit.md",
    "ko/integrations/langchain/tools/pipedream-mcp-user-guide-1.md",
    "ko/integrations/langchain/tools/pipedream-mcp-user-guide.md",
    "ko/integrations/langchain/tools/python-interpreter.md",
    "ko/integrations/langchain/tools/read-file.md",
    "ko/integrations/langchain/tools/README.md",
]

def extract_frontmatter(content):
    """Extract YAML frontmatter if it exists."""
    if not content.startswith("---"):
        return None, content

    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        frontmatter = match.group(1)
        body = content[match.end():]
        return frontmatter, body
    return None, content

def preserve_code_blocks(content):
    """Extract code blocks to preserve them."""
    code_blocks = []

    def replace_code_block(match):
        code_blocks.append(match.group(0))
        return f"<<<CODE_BLOCK_{len(code_blocks)-1}>>>"

    # Match both ``` and ~~~ code blocks
    content = re.sub(r'```[\s\S]*?```', replace_code_block, content)
    content = re.sub(r'~~~[\s\S]*?~~~', replace_code_block, content)

    return content, code_blocks

def restore_code_blocks(content, code_blocks):
    """Restore code blocks."""
    for i, block in enumerate(code_blocks):
        content = content.replace(f"<<<CODE_BLOCK_{i}>>>", block)
    return content

def translate_content(text):
    """Translate content using Claude API."""
    if not text.strip():
        return text

    translation_prompt = """You are a Korean translator for technical documentation. Translate the following English text to Korean following these rules:

1. Translate all regular text to Korean
2. Keep code blocks exactly as-is
3. Keep URLs and file paths unchanged
4. Keep these English technical terms unchanged: Flowise, API, LLM, Node, JavaScript, Python, RAG, Vector Store, Agent, ChatGPT, OpenAI, Langchain, LlamaIndex, Claude, Anthropic, JSON, YAML, HTTP, REST, SQL, NoSQL, MongoDB, PostgreSQL, Redis, Pinecone, Chroma, Vector, Embedding, Token, Prompt, Response, Model, Parameter, Configuration, Integration, Webhook, Authentication, OAuth, API Key, Environment Variable, Deployment, Production, Development, Testing, Framework, Library, Package, Module, Function, Class, Method, Object, Array, String, Number, Boolean, Date, Time, Timezone, Locale, Language, Culture, Encoding, Format, Protocol, Server, Client, Request, Response, Database, Collection, Document, Index, Query, Search, Filter, Sort, Pagination, Rate Limit, Timeout, Retry, Error, Exception, Warning, Debug, Log, Trace, Profile, Monitor, Alert, Metric, Analytics, Dashboard, Report, Export, Import, Upload, Download, Stream, Queue, Task, Job, Workflow, Pipeline, Chain, Tool, Plugin, Extension, Middleware, Wrapper, Provider, Service, Endpoint, Route, Handler, Hook, Event, Listener, Callback, Promise, Async, Await, Synchronous, Asynchronous, Concurrent, Parallel, Sequential, Recursive, Iterator, Generator, Decorator, Context, Scope, Variable, Constant, Type, Interface, Abstract, Concrete, Inheritance, Polymorphism, Encapsulation, Abstraction, SOLID, Design Pattern, Architecture, Microservice, Monolith, Scalability, Performance, Optimization, Caching, Compression, Serialization, Deserialization, Validation, Sanitization, Security, Encryption, Decryption, Hash, Signature, Certificate, SSL, TLS, SSH, VPN, Firewall, Proxy, Gateway, Load Balancer, Container, Docker, Kubernetes, Cluster, Node, Pod, Service, Ingress, Storage, Volume, PersistentVolume, Namespace, Label, Annotation, ConfigMap, Secret, StatefulSet, DaemonSet, Job, CronJob, HPA, VPA, PDB, NetworkPolicy, RBAC, ServiceAccount, Role, RoleBinding, ClusterRole, ClusterRoleBinding, Exa, Gmail, Google, Microsoft, Outlook, Teams, Tavily, OpenAPI, Zep, Couchbase, Elasticsearch, Redis, SingleStore, Upstash, Chroma, LiteLLM, LlamaIndex, Notion, Linear, Asana, GitHub, Slack, Pinecone, Weaviate, Milvus, FAISS, Qdrant, Cosmos, Puppeteer, S3, SearchAPI, SerpAPI, Spider, Unstructured, MCP, Pipedream, Exa Search, Python Interpreter
5. Preserve all Markdown structure and formatting (headers, lists, links, images, etc.)
6. Maintain the same line breaks and paragraph structure

Here is the text to translate:

{text}

Provide only the translated Korean text without any explanations or comments."""

    try:
        message = client.messages.create(
            model="claude-opus-4",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": translation_prompt.format(text=text)}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"  Error: {str(e)[:100]}")
        return text

def ensure_dir_exists(file_path):
    """Ensure directory exists for the file."""
    dir_path = os.path.dirname(file_path)
    os.makedirs(dir_path, exist_ok=True)

def translate_file(file_path):
    """Translate a single file."""
    full_path = os.path.join(BASE_DIR, file_path)

    # Ensure the directory exists
    ensure_dir_exists(full_path)

    # Check if source file exists, if not, create an empty placeholder
    source_file = full_path.replace("/ko/", "/en/")
    if not os.path.exists(full_path) and not os.path.exists(source_file):
        print(f"  Source file not found, creating placeholder")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write("")
        return False

    try:
        # Read the file (either existing Korean or create new)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # Try to read from English source
            if os.path.exists(source_file):
                with open(source_file, 'r', encoding='utf-8') as f:
                    content = f.read()
            else:
                content = ""

        if not content.strip():
            return False

        # Extract frontmatter
        frontmatter, body = extract_frontmatter(content)

        # Preserve code blocks
        body_without_code, code_blocks = preserve_code_blocks(body)

        # Translate the body
        translated_body = translate_content(body_without_code)

        # Restore code blocks
        translated_body = restore_code_blocks(translated_body, code_blocks)

        # Reconstruct the file
        if frontmatter:
            translated_content = f"---\n{frontmatter}\n---\n{translated_body}"
        else:
            translated_content = translated_body

        # Write back to Korean path
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True
    except Exception as e:
        print(f"  Error: {str(e)[:100]}")
        return False

def main():
    """Main translation function."""
    total_files = len(FILES_TO_TRANSLATE)
    translated_count = 0

    print(f"배치 1 시작: {total_files}개 파일 번역 중...\n")

    for index, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        filename = os.path.basename(file_path)
        if translate_file(file_path):
            print(f"[{index}/{total_files}] {filename} → translated")
            translated_count += 1
        else:
            print(f"[{index}/{total_files}] {filename} → FAILED")

    print()
    print(f"마지막 배치 1 완료: {translated_count}개")

if __name__ == "__main__":
    main()
