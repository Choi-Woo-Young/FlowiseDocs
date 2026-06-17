#!/usr/bin/env python3
"""
FlowiseDocs Batch 3 Comprehensive Translation Script
Translates remaining 54 files from English to Korean using Claude API
"""

import os
import re
import sys
import time
from pathlib import Path
from anthropic import Anthropic

# Initialize Anthropic client
client = Anthropic()

# Base directory
BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko/integrations/langchain/"

# List of 54 files to translate
FILES_TO_TRANSLATE = [
    # README files (9)
    "llms/README.md",
    "memory/README.md",
    "moderation/README.md",
    "output-parsers/README.md",
    "prompts/README.md",
    "retrievers/README.md",
    "text-splitters/README.md",
    "tools/README.md",
    "vector-stores/README.md",
    # Tools files (26)
    "tools/chatflow-tool.md",
    "tools/custom-tool.md",
    "tools/exa-search.md",
    "tools/gmail.md",
    "tools/google-calendar.md",
    "tools/google-custom-search.md",
    "tools/google-drive.md",
    "tools/google-sheets.md",
    "tools/microsoft-outlook.md",
    "tools/microsoft-teams.md",
    "tools/openapi-toolkit.md",
    "tools/pipedream-mcp-user-guide-1.md",
    "tools/pipedream-mcp-user-guide.md",
    "tools/python-interpreter.md",
    "tools/read-file.md",
    "tools/request-get.md",
    "tools/request-post.md",
    "tools/retriever-tool.md",
    "tools/searchapi.md",
    "tools/searxng.md",
    "tools/serp-api.md",
    "tools/serper.md",
    "tools/tavily-ai.md",
    "tools/web-browser.md",
    "tools/write-file.md",
    # Vector-stores files (20)
    "vector-stores/astradb.md",
    "vector-stores/chroma.md",
    "vector-stores/couchbase.md",
    "vector-stores/elastic.md",
    "vector-stores/faiss.md",
    "vector-stores/in-memory-vector-store.md",
    "vector-stores/milvus.md",
    "vector-stores/mongodb-atlas.md",
    "vector-stores/opensearch.md",
    "vector-stores/pinecone.md",
    "vector-stores/postgres.md",
    "vector-stores/qdrant.md",
    "vector-stores/redis.md",
    "vector-stores/singlestore.md",
    "vector-stores/supabase.md",
    "vector-stores/upstash-vector.md",
    "vector-stores/vectara.md",
    "vector-stores/weaviate.md",
    "vector-stores/zep-collection-cloud.md",
    "vector-stores/zep-collection-open-source.md",
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
2. Keep code blocks exactly as-is (they are marked as <<<CODE_BLOCK_N>>>)
3. Keep URLs and file paths unchanged
4. Keep these English technical terms unchanged: Flowise, API, LLM, Node, JavaScript, Python, RAG, Vector Store, Agent, ChatGPT, OpenAI, Langchain, LlamaIndex, Claude, Anthropic, JSON, YAML, HTTP, REST, SQL, NoSQL, MongoDB, PostgreSQL, Redis, Pinecone, Chroma, Vector, Embedding, Token, Prompt, Response, Model, Parameter, Configuration, Integration, Webhook, Authentication, OAuth, API Key, Environment Variable, Deployment, Production, Development, Testing, Framework, Library, Package, Module, Function, Class, Method, Object, Array, String, Number, Boolean, Date, Time, Timezone, Locale, Language, Culture, Encoding, Format, Protocol, Server, Client, Request, Response, Database, Collection, Document, Index, Query, Search, Filter, Sort, Pagination, Rate Limit, Timeout, Retry, Error, Exception, Warning, Debug, Log, Trace, Profile, Monitor, Alert, Metric, Analytics, Dashboard, Report, Export, Import, Upload, Download, Stream, Queue, Task, Job, Workflow, Pipeline, Chain, Tool, Plugin, Extension, Middleware, Wrapper, Provider, Service, Endpoint, Route, Handler, Hook, Event, Listener, Callback, Promise, Async, Await, Synchronous, Asynchronous, Concurrent, Parallel, Sequential, Recursive, Iterator, Generator, Decorator, Context, Scope, Variable, Constant, Type, Interface, Abstract, Concrete, Inheritance, Polymorphism, Encapsulation, Abstraction, SOLID, Design Pattern, Architecture, Microservice, Monolith, Scalability, Performance, Optimization, Caching, Compression, Serialization, Deserialization, Validation, Sanitization, Security, Encryption, Decryption, Hash, Signature, Certificate, SSL, TLS, SSH, VPN, Firewall, Proxy, Gateway, Load Balancer, Container, Docker, Kubernetes, Cluster, Node, Pod, Service, Ingress, Storage, Volume, PersistentVolume, Namespace, Label, Annotation, ConfigMap, Secret, StatefulSet, DaemonSet, Job, CronJob, HPA, VPA, PDB, NetworkPolicy, RBAC, ServiceAccount, Role, RoleBinding, ClusterRole, ClusterRoleBinding, Exa, Gmail, Google, Microsoft, Outlook, Teams, Tavily, OpenAPI, Zep, Couchbase, Elasticsearch, Redis, SingleStore, Upstash, Chroma, LiteLLM, LlamaIndex, Notion, Linear, Asana, GitHub, Slack, Pinecone, Weaviate, Milvus, FAISS, Qdrant, Cosmos, AWS, Bedrock, Azure, Cohere, HuggingFace, Ollama, Replicate, GraphQL, TypeScript, Scala, Java, Go, Rust, C++, C#, PHP, Ruby, Swift, Kotlin, R, MATLAB
5. Preserve all Markdown structure and formatting (headers, lists, links, images, tables, etc.)
6. Maintain the same line breaks and paragraph structure
7. Translate table headers and content
8. Translate image captions and descriptions

Here is the text to translate:

{text}

Provide only the translated Korean text without any explanations or comments."""

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": translation_prompt.format(text=text)}
            ]
        )
        return message.content[0].text
    except Exception as e:
        print(f"    API Error: {str(e)[:100]}")
        return None

def translate_file(file_path):
    """Translate a single file."""
    full_path = os.path.join(BASE_DIR, file_path)

    if not os.path.exists(full_path):
        return False, "File not found"

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract frontmatter
        frontmatter, body = extract_frontmatter(content)

        # Preserve code blocks
        body_without_code, code_blocks = preserve_code_blocks(body)

        # Translate the body
        translated_body = translate_content(body_without_code)
        
        if translated_body is None:
            return False, "Translation failed"

        # Restore code blocks
        translated_body = restore_code_blocks(translated_body, code_blocks)

        # Reconstruct the file
        if frontmatter:
            translated_content = f"---\n{frontmatter}\n---\n{translated_body}"
        else:
            translated_content = translated_body

        # Write back
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True, "Translated"

    except Exception as e:
        return False, f"Error: {str(e)[:50]}"

def contains_korean(text):
    """Check if text contains Korean characters."""
    return bool(re.search(r'[가-힯]', text))

def main():
    """Main translation function."""
    total_files = len(FILES_TO_TRANSLATE)
    translated_count = 0
    failed_files = []

    print(f"배치 3 시작: {total_files}개 파일 번역 중...\n")

    for index, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        filename = os.path.basename(file_path)
        success, message = translate_file(file_path)
        
        if success:
            print(f"[{index:2d}/{total_files}] {filename:40s} ✓ {message}")
            translated_count += 1
        else:
            print(f"[{index:2d}/{total_files}] {filename:40s} ✗ {message}")
            failed_files.append(file_path)
        
        # Add a small delay to avoid rate limiting
        if index < total_files:
            time.sleep(0.5)

    print()
    print(f"{'='*70}")
    print(f"배치 3 완료: {translated_count}/{total_files}개 파일 번역됨")
    if failed_files:
        print(f"\n실패한 파일 ({len(failed_files)}개):")
        for f in failed_files:
            print(f"  - {f}")
    print(f"{'='*70}")

if __name__ == "__main__":
    main()
