#!/usr/bin/env python3
"""
FlowiseDocs Batch 6 Translation Script
Translates 42 files from English to Korean using Claude API
"""

import os
import re
from pathlib import Path
from anthropic import Anthropic

# Initialize Anthropic client - it will use ANTHROPIC_API_KEY env var if available
# or ~/.anthropic-config if set up
client = Anthropic()

# Base directory
BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/"

# List of 42 files to translate
FILES_TO_TRANSLATE = [
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
    "ko/integrations/langchain/tools/tavily-ai.md",
    "ko/integrations/langchain/tools/web-browser.md",
    "ko/integrations/langchain/tools/write-file.md",
    "ko/integrations/langchain/vector-stores/chroma.md",
    "ko/integrations/langchain/vector-stores/couchbase.md",
    "ko/integrations/langchain/vector-stores/elastic.md",
    "ko/integrations/langchain/vector-stores/in-memory-vector-store.md",
    "ko/integrations/langchain/vector-stores/opensearch.md",
    "ko/integrations/langchain/vector-stores/redis.md",
    "ko/integrations/langchain/vector-stores/singlestore.md",
    "ko/integrations/langchain/vector-stores/upstash-vector.md",
    "ko/integrations/langchain/vector-stores/zep-collection-cloud.md",
    "ko/integrations/langchain/vector-stores/zep-collection-open-source.md",
    "ko/integrations/litellm/README.md",
    "ko/integrations/llamaindex/README.md",
    "ko/integrations/llamaindex/vector-stores/README.md",
    "ko/integrations/README.md",
    "ko/integrations/utilities/README.md",
    "ko/migration-guide/v1.3.0-migration-guide.md",
    "ko/migration-guide/v1.4.3-migration-guide.md",
    "ko/migration-guide/v2.1.4-migration-guide.md",
    "ko/text-splitters/charater-text-splitter.md",
    "ko/use-cases/interacting-with-api.md",
    "ko/use-cases/multiple-documents-qna.md",
    "ko/use-cases/README.md",
    "ko/use-cases/sql-qna.md",
    "ko/use-cases/upserting-data.md",
    "ko/use-cases/web-scrape-qna.md",
    "ko/use-cases/webhook-tool.md",
    "ko/using-flowise/agentflowv1/README.md",
    "ko/using-flowise/analytics/langfuse.md",
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

def translate_content(text, retries=3):
    """Translate content using Claude API with retry logic."""
    if not text.strip():
        return text

    translation_prompt = """You are a Korean translator for technical documentation. Translate the following English text to Korean following these rules:

1. Translate all regular text to Korean
2. Keep code blocks exactly as-is
3. Keep URLs and file paths unchanged
4. Keep these English technical terms unchanged: Flowise, API, LLM, Node, JavaScript, Python, RAG, Vector Store, Agent, ChatGPT, OpenAI, Langchain, LlamaIndex, Claude, Anthropic, JSON, YAML, HTTP, REST, SQL, NoSQL, MongoDB, PostgreSQL, Redis, Pinecone, Chroma, Vector, Embedding, Token, Prompt, Response, Model, Parameter, Configuration, Integration, Webhook, Authentication, OAuth, API Key, Environment Variable, Deployment, Production, Development, Testing, Framework, Library, Package, Module, Function, Class, Method, Object, Array, String, Number, Boolean, Date, Time, Timezone, Locale, Language, Culture, Encoding, Format, Protocol, Server, Client, Request, Response, Database, Collection, Document, Index, Query, Search, Filter, Sort, Pagination, Rate Limit, Timeout, Retry, Error, Exception, Warning, Debug, Log, Trace, Profile, Monitor, Alert, Metric, Analytics, Dashboard, Report, Export, Import, Upload, Download, Stream, Queue, Task, Job, Workflow, Pipeline, Chain, Tool, Plugin, Extension, Middleware, Wrapper, Provider, Service, Endpoint, Route, Handler, Middleware, Hook, Event, Listener, Callback, Promise, Async, Await, Synchronous, Asynchronous, Concurrent, Parallel, Sequential, Recursive, Iterator, Generator, Decorator, Context, Scope, Variable, Constant, Type, Interface, Abstract, Concrete, Inheritance, Polymorphism, Encapsulation, Abstraction, SOLID, Design Pattern, Architecture, Microservice, Monolith, Scalability, Performance, Optimization, Caching, Compression, Serialization, Deserialization, Validation, Sanitization, Security, Encryption, Decryption, Hash, Signature, Certificate, SSL, TLS, SSH, VPN, Firewall, Proxy, Gateway, Load Balancer, Container, Docker, Kubernetes, Cluster, Node, Pod, Service, Ingress, Storage, Volume, PersistentVolume, Namespace, Label, Annotation, ConfigMap, Secret, StatefulSet, DaemonSet, Job, CronJob, HPA, VPA, PDB, NetworkPolicy, RBAC, ServiceAccount, Role, RoleBinding, ClusterRole, ClusterRoleBinding
5. Preserve all Markdown structure and formatting (headers, lists, links, images, etc.)
6. Maintain the same line breaks and paragraph structure

Here is the text to translate:

{text}

Provide only the translated Korean text without any explanations or comments."""

    for attempt in range(retries):
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
            if attempt < retries - 1:
                print(f"  Retry {attempt + 1}/{retries - 1} - {str(e)[:80]}")
            else:
                print(f"  Translation failed after {retries} attempts: {e}")
                return text

def translate_file(file_path):
    """Translate a single file."""
    full_path = os.path.join(BASE_DIR, file_path)

    if not os.path.exists(full_path):
        print(f"[SKIP] File not found: {file_path}")
        return False

    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()

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

        # Write back
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

        return True
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False

def main():
    """Main translation function."""
    total_files = len(FILES_TO_TRANSLATE)
    translated_count = 0

    print(f"Starting batch 6 translation of {total_files} files...")
    print()

    for index, file_path in enumerate(FILES_TO_TRANSLATE, 1):
        filename = os.path.basename(file_path)
        if translate_file(file_path):
            print(f"[{index}/{total_files}] {filename} → translated")
            translated_count += 1
        else:
            print(f"[{index}/{total_files}] {filename} → FAILED")

    print()
    print(f"배치 6 완료: {translated_count}개 파일")

if __name__ == "__main__":
    main()
