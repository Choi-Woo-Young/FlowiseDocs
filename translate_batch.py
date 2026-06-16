#!/usr/bin/env python3
"""
Batch Korean Translation for Flowise Documentation (63 files)
Using Claude API with proper authentication
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from datetime import datetime

def get_anthropic_client():
    """Get Anthropic client with proper authentication."""
    try:
        from anthropic import Anthropic

        # Try to get API key from environment
        api_key = os.environ.get('ANTHROPIC_API_KEY')

        if api_key:
            return Anthropic(api_key=api_key)
        else:
            # Try to use from default authentication
            return Anthropic()
    except ImportError:
        print("ERROR: anthropic module not installed")
        sys.exit(1)

# Configuration
EN_DIR = Path("en")
KO_DIR = Path("ko")

# 63 files to translate
FILES_TO_TRANSLATE = [
    "integrations/langchain/document-loaders/README.md",
    "integrations/langchain/document-loaders/airtable.md",
    "integrations/langchain/document-loaders/api-loader.md",
    "integrations/langchain/document-loaders/apify-website-content-crawler.md",
    "integrations/langchain/document-loaders/bravesearch-api.md",
    "integrations/langchain/document-loaders/confluence.md",
    "integrations/langchain/document-loaders/directory-loader.md",
    "integrations/langchain/document-loaders/github-repository-loader.md",
    "integrations/langchain/document-loaders/github.md",
    "integrations/langchain/document-loaders/google-drive-loader.md",
    "integrations/langchain/document-loaders/json-loader.md",
    "integrations/langchain/document-loaders/notion-database-loader.md",
    "integrations/langchain/document-loaders/pdf-file.md",
    "integrations/langchain/document-loaders/s3-directory-loader.md",
    "integrations/langchain/document-loaders/s3-file-loader.md",
    "integrations/langchain/document-loaders/searchapi-for-web-search.md",
    "integrations/langchain/document-loaders/sitemap-loader.md",
    "integrations/langchain/document-loaders/web-scraper.md",
    "integrations/langchain/document-loaders/xlsx-file.md",
    "integrations/langchain/embeddings/anthropic-embeddings.md",
    "integrations/langchain/embeddings/azure-openai-embeddings.md",
    "integrations/langchain/embeddings/bedrock-embeddings.md",
    "integrations/langchain/embeddings/cohere-embeddings.md",
    "integrations/langchain/embeddings/google-generativeai-embeddings.md",
    "integrations/langchain/embeddings/googlegenerativeai-embeddings.md",
    "integrations/langchain/embeddings/googlevertexai-embeddings.md",
    "integrations/langchain/embeddings/groq-embeddings.md",
    "integrations/langchain/embeddings/huggingface-inference-embeddings.md",
    "integrations/langchain/embeddings/huggingface-hub-inference-api-embeddings.md",
    "integrations/langchain/embeddings/localai-embeddings.md",
    "integrations/langchain/embeddings/mistralai-embeddings.md",
    "integrations/langchain/embeddings/ollama-embeddings.md",
    "integrations/langchain/embeddings/openai-embeddings-custom.md",
    "integrations/langchain/embeddings/openai-embeddings.md",
    "integrations/langchain/embeddings/README.md",
    "integrations/langchain/embeddings/togetherai-embedding.md",
    "integrations/langchain/embeddings/voyageai-embeddings.md",
    "integrations/langchain/llms/README.md",
    "integrations/langchain/llms/ai21.md",
    "integrations/langchain/llms/aleph-alpha.md",
    "integrations/langchain/llms/anthropic.md",
    "integrations/langchain/llms/aws-bedrock.md",
    "integrations/langchain/llms/azure-openai.md",
    "integrations/langchain/llms/cohere.md",
    "integrations/langchain/llms/googlevertex-ai.md",
    "integrations/langchain/llms/google-vertexai.md",
    "integrations/langchain/llms/groq.md",
    "integrations/langchain/llms/huggingface-inference.md",
    "integrations/langchain/llms/huggingface-llm.md",
    "integrations/langchain/llms/ibm-watsonx.md",
    "integrations/langchain/llms/localai.md",
    "integrations/langchain/llms/mistral-ai.md",
    "integrations/langchain/llms/nlp-cloud.md",
    "integrations/langchain/llms/ollama.md",
    "integrations/langchain/llms/openai.md",
    "integrations/langchain/llms/openrouter.md",
    "integrations/langchain/llms/petals.md",
    "integrations/langchain/llms/replicate.md",
    "integrations/langchain/llms/semafore-ai.md",
    "integrations/langchain/llms/together.md",
    "integrations/litellm/README.md",
    "migration-guide/README.md",
    "migration-guide/cloud-migration.md",
]

class FileTranslator:
    """Translates files to Korean."""

    def __init__(self):
        self.client = get_anthropic_client()
        self.model = "claude-opus-4-8"
        self.completed = []
        self.failed = []
        self.skipped = []

    def extract_code_blocks(self, text):
        """Extract code blocks to preserve them."""
        placeholders = {}
        code_pattern = re.compile(r'```[\s\S]*?```', re.MULTILINE)

        for i, match in enumerate(code_pattern.finditer(text)):
            placeholder = f"<<<CODE_BLOCK_{i}>>>"
            placeholders[placeholder] = match.group(0)

        for placeholder, code in placeholders.items():
            text = text.replace(code, placeholder, 1)

        return text, placeholders

    def restore_code_blocks(self, text, placeholders):
        """Restore code blocks."""
        for placeholder, code in placeholders.items():
            text = text.replace(placeholder, code)
        return text

    def translate_text(self, text):
        """Translate text to Korean."""
        if not text.strip():
            return text

        # Extract code blocks
        text_without_code, code_blocks = self.extract_code_blocks(text)

        if not text_without_code.strip():
            return self.restore_code_blocks(text, code_blocks)

        # Translation prompt
        prompt = f"""You are a professional Korean translator specializing in technical documentation.
Translate the following English markdown to Korean (한국어).

CRITICAL RULES:
1. Translate ALL narrative, instructional text to Korean
2. PRESERVE in English ONLY:
   - Code variable/function/command names
   - API names and acronyms: API, LLM, RAG, JSON, REST, HTTP, HTTPS, GraphQL, XML, HTML
   - Product names: OpenAI, Groq, Anthropic, Claude, Flowise, Cohere, Mistral, Replicate
   - System components: Agent, Flow, Node, Tool, Canvas, Agentflow, Chatflow, Retriever
   - Provider names: AWS, Azure, Google, Bedrock, Vertex AI, HuggingFace, Ollama, LocalAI
3. Keep all markdown formatting (##, **, *,  [], (), etc)
4. Keep all HTML tags
5. Do NOT add, remove, or change content - only translate

Text to translate:
{text_without_code}

Provide ONLY the translated text, no explanations."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[{"role": "user", "content": prompt}]
            )

            translated = message.content[0].text
            translated = self.restore_code_blocks(translated, code_blocks)
            return translated

        except Exception as e:
            raise Exception(f"Translation failed: {str(e)[:100]}")

    def translate_file(self, rel_path):
        """Translate a single file."""
        en_file = EN_DIR / rel_path
        ko_file = KO_DIR / rel_path

        # Check source exists
        if not en_file.exists():
            self.skipped.append(rel_path)
            return None

        try:
            # Read English
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Translate
            translated = self.translate_text(content)

            # Ensure directory exists
            ko_file.parent.mkdir(parents=True, exist_ok=True)

            # Write Korean
            with open(ko_file, 'w', encoding='utf-8') as f:
                f.write(translated)

            self.completed.append(rel_path)
            return True

        except Exception as e:
            print(f"      ERROR: {str(e)[:80]}")
            self.failed.append(rel_path)
            return False

    def run(self):
        """Run translation."""
        total = len(FILES_TO_TRANSLATE)

        print(f"Translating {total} files...")
        print("=" * 70)

        for i, rel_path in enumerate(FILES_TO_TRANSLATE, 1):
            print(f"[{i}/{total}] {rel_path}...", end=" ", flush=True)

            try:
                result = self.translate_file(rel_path)
                if result is True:
                    print("✓")
                elif result is False:
                    print("✗")
                else:
                    print("⊘")
            except Exception as e:
                print(f"ERROR: {str(e)[:40]}")
                self.failed.append(rel_path)

            # Rate limiting
            if i % 5 == 0 and i < total:
                time.sleep(2)

        # Summary
        print("=" * 70)
        print(f"\nTranslation Summary:")
        print(f"  Completed: {len(self.completed)}/63")
        print(f"  Failed: {len(self.failed)}")
        print(f"  Skipped: {len(self.skipped)}")

        if self.failed:
            print(f"\nFailed files:")
            for f in self.failed:
                print(f"  - {f}")

if __name__ == "__main__":
    translator = FileTranslator()
    translator.run()
