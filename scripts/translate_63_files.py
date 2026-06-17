#!/usr/bin/env python3
"""
Specialized Korean Translation for 63 Flowise Documentation Files
==================================================================

This script translates exactly 63 specific files from en/ to ko/ directory.

Usage:
    export ANTHROPIC_API_KEY="sk-..."
    python3 translate_63_files.py
"""

import os
import re
import sys
import json
import time
from pathlib import Path
from datetime import datetime

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: anthropic module not installed. Run: pip install anthropic")
    sys.exit(1)

# Configuration
EN_DIR = Path("en")
KO_DIR = Path("ko")
STATUS_FILE = Path(".translation_status_63.json")

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

class KoreanTranslator:
    """Handles Korean translation of markdown files."""

    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        self.client = Anthropic(api_key=self.api_key)
        self.model = "claude-3-5-sonnet-20241022"
        self.load_status()

    def load_status(self):
        """Load translation status from previous runs."""
        if STATUS_FILE.exists():
            with open(STATUS_FILE, 'r', encoding='utf-8') as f:
                self.status = json.load(f)
        else:
            self.status = {
                'start_time': datetime.now().isoformat(),
                'completed_files': [],
                'failed_files': [],
                'skipped_files': []
            }

    def save_status(self):
        """Save translation status."""
        with open(STATUS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.status, f, indent=2, ensure_ascii=False)

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
        """Restore code blocks to the text."""
        for placeholder, code in placeholders.items():
            text = text.replace(placeholder, code)
        return text

    def translate_text(self, text):
        """Translate English text to Korean using Claude."""
        if not text.strip():
            return text

        # Extract and protect code blocks
        text_without_code, code_placeholders = self.extract_code_blocks(text)

        if not text_without_code.strip():
            # Only code blocks, return as-is
            return self.restore_code_blocks(text, code_placeholders)

        # Create translation prompt
        prompt = f"""You are a professional translator specializing in technical documentation.
Translate the following English markdown to Korean (한국어).

CRITICAL RULES:
1. Translate ALL narrative text, instructions, and descriptions to fluent, natural Korean
2. PRESERVE in English ONLY:
   - Code variable names, function names, command names
   - API names and technical acronyms: API, LLM, RAG, JSON, REST, HTTP, HTTPS, GraphQL, XML, HTML
   - Product names: OpenAI, Groq, Anthropic, Claude, Flowise, FlowiseDocs, GPT, Cohere, Mistral, Together, Replicate
   - System component names: Agent, Flow, Node, Tool, Canvas, Agentflow, Chatflow, Retriever, Document Store, Vector Database
   - Provider names: AWS, Azure, Google, Bedrock, Vertex AI, HuggingFace, Ollama, LocalAI, Petals
3. NO English text should remain in descriptions (except items above)
4. Preserve ALL markdown formatting exactly: headers, bold, italics, lists, links, code blocks
5. Preserve all HTML tags and figure captions
6. Use formal, professional Korean technical terminology
7. Do NOT add, remove, or modify any content - only translate
8. Translate parameter descriptions, configuration options, and usage instructions

Text to translate:
{text_without_code}

Provide ONLY the translated text, with no explanations or markdown code fences."""

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4096,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            translated = message.content[0].text

            # Restore code blocks
            translated = self.restore_code_blocks(translated, code_placeholders)

            return translated

        except Exception as e:
            print(f"    Translation error: {str(e)[:80]}")
            raise

    def process_file(self, rel_path):
        """Process a single file for translation."""
        # Check if already processed
        if rel_path in self.status['completed_files']:
            return None  # Already done
        if rel_path in self.status['failed_files']:
            return False  # Previously failed

        en_path = EN_DIR / rel_path
        ko_path = KO_DIR / rel_path

        # Verify English source exists
        if not en_path.exists():
            self.status['skipped_files'].append(rel_path)
            return None  # No source

        try:
            # Read English source
            with open(en_path, 'r', encoding='utf-8') as f:
                en_content = f.read()

            # Translate
            ko_content = self.translate_text(en_content)

            # Ensure directory exists
            ko_path.parent.mkdir(parents=True, exist_ok=True)

            # Write Korean translation
            with open(ko_path, 'w', encoding='utf-8') as f:
                f.write(ko_content)

            self.status['completed_files'].append(rel_path)
            return True

        except Exception as e:
            print(f"      ERROR: {str(e)[:60]}")
            self.status['failed_files'].append(rel_path)
            return False

    def run(self):
        """Run translation process for the 63 specific files."""
        # Filter files that need processing
        files_to_process = [
            f for f in FILES_TO_TRANSLATE
            if f not in self.status['completed_files']
            and f not in self.status['skipped_files']
        ]

        total = len(files_to_process)
        if total == 0:
            print("All 63 files have been processed!")
            print(f"Completed: {len(self.status['completed_files'])}")
            print(f"Failed: {len(self.status['failed_files'])}")
            print(f"Skipped: {len(self.status['skipped_files'])}")
            return

        print(f"\nStarting translation of {total} files (out of 63 total)...")
        print(f"Previously completed: {len(self.status['completed_files'])}")
        print("=" * 70)

        start_time = time.time()
        success_count = 0

        for i, rel_path in enumerate(files_to_process, 1):
            print(f"[{i}/{total}] {rel_path}...", end=" ", flush=True)

            try:
                result = self.process_file(rel_path)
                if result is True:
                    print("✓")
                    success_count += 1
                elif result is False:
                    print("✗")
                else:
                    print("⊘")  # Skipped

            except Exception as e:
                print(f"ERROR: {str(e)[:40]}")

            # Rate limiting to avoid API throttling
            if i % 5 == 0 and i < total:
                time.sleep(1)

            # Save status periodically
            if i % 10 == 0:
                self.save_status()

        # Final save
        self.save_status()

        elapsed = time.time() - start_time
        print("=" * 70)
        print(f"\nTranslation Complete!")
        print(f"  Time: {elapsed:.1f} seconds")
        print(f"  Completed this run: {success_count}/{total}")
        print(f"  Total completed: {len(self.status['completed_files'])}/63")
        print(f"  Failed: {len(self.status['failed_files'])}")
        print(f"  Skipped: {len(self.status['skipped_files'])}")


def main():
    """Main entry point."""
    try:
        translator = KoreanTranslator()
        translator.run()

    except KeyError as e:
        print(f"ERROR: {e}")
        print("\nPlease set ANTHROPIC_API_KEY environment variable:")
        print("  export ANTHROPIC_API_KEY='sk-...'")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
