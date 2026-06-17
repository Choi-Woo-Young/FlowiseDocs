#!/usr/bin/env python3
"""
Batch translation script for Flowise documentation using Anthropic API
Translates markdown files from English to Korean while preserving code blocks and technical terms
"""

import os
import json
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

class MarkdownTranslator:
    """Translate markdown files from English to Korean using Anthropic API"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('ANTHROPIC_API_KEY')
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        self.api_url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-opus-4-1-20250805"
        self.translated_count = 0
        self.skipped_count = 0
        self.failed_count = 0
        self.failed_files = []

    @staticmethod
    def is_korean_file(content: str) -> bool:
        """Check if content already contains Korean characters"""
        return any('가' <= char <= '힯' for char in content)

    @staticmethod
    def is_empty_file(content: str) -> bool:
        """Check if file is empty or only whitespace"""
        return not content.strip()

    def translate_content(self, content: str) -> str:
        """Translate markdown content using Anthropic API"""

        prompt = f"""You are a professional translator specializing in technical documentation. Translate the following markdown file from English to Korean.

Translation Rules:
1. Translate all titles, headings, body text, table content to Korean
2. Keep code blocks (```...```) unchanged - do not translate code
3. Keep image paths and URLs unchanged, but translate link text
4. Keep technical terms in English: Flowise, API, LLM, RAG, Agent, Flow, OpenAI, Azure, Docker, GitHub, HTTP, REST, JSON, YAML, Python, Node.js, JavaScript, TypeScript, React, Vue, Kubernetes, AWS, GCP, SQL, MongoDB, Redis, PostgreSQL, MySQL, etc.
5. Preserve all markdown structure, indentation, and formatting exactly
6. Translate YAML frontmatter metadata (description field) to Korean
7. Keep file paths, domain names, configuration values, and command-line examples unchanged

Output ONLY the translated markdown content without any explanation.

File to translate:

{content}"""

        payload = {
            "model": self.model,
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            result = subprocess.run(
                ['curl', '-s', '-X', 'POST',
                 self.api_url,
                 '-H', 'Content-Type: application/json',
                 '-H', f'x-api-key: {self.api_key}',
                 '-d', json.dumps(payload)],
                capture_output=True,
                text=True,
                timeout=60
            )

            response = json.loads(result.stdout)

            if 'error' in response:
                raise Exception(f"API Error: {response['error']}")

            if 'content' not in response or not response['content']:
                raise Exception("No content in API response")

            return response['content'][0]['text']

        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse API response: {str(e)}")
        except subprocess.TimeoutExpired:
            raise Exception("API request timed out")

    def translate_file(self, file_path: str) -> bool:
        """Translate a single markdown file"""

        file_path = Path(file_path)

        if not file_path.exists():
            print(f"❌ File not found: {file_path}")
            self.failed_count += 1
            self.failed_files.append((str(file_path), "File not found"))
            return False

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Skip empty files
            if self.is_empty_file(content):
                print(f"⊘  Skipped (empty): {file_path.name}")
                self.skipped_count += 1
                return True

            # Skip already Korean files
            if self.is_korean_file(content):
                print(f"⊘  Skipped (already Korean): {file_path.name}")
                self.skipped_count += 1
                return True

            print(f"⏳ Translating: {file_path.name}...", end=" ", flush=True)

            # Translate content
            translated_content = self.translate_content(content)

            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            print("✓")
            self.translated_count += 1
            return True

        except Exception as e:
            print(f"❌")
            print(f"  Error: {str(e)}")
            self.failed_count += 1
            self.failed_files.append((str(file_path), str(e)))
            return False

    def translate_files(self, file_paths: List[str]) -> None:
        """Translate multiple files"""

        print(f"\n{'='*60}")
        print(f"Starting batch translation: {len(file_paths)} files")
        print(f"{'='*60}\n")

        for i, file_path in enumerate(file_paths, 1):
            print(f"[{i}/{len(file_paths)}] ", end="")
            self.translate_file(file_path)

        self.print_summary()

    def print_summary(self) -> None:
        """Print translation summary"""

        total = self.translated_count + self.skipped_count + self.failed_count

        print(f"\n{'='*60}")
        print(f"Translation Summary")
        print(f"{'='*60}")
        print(f"✓ Translated: {self.translated_count}")
        print(f"⊘ Skipped:    {self.skipped_count}")
        print(f"❌ Failed:     {self.failed_count}")
        print(f"Total:       {total}")
        print(f"{'='*60}")

        if self.failed_files:
            print(f"\nFailed files:")
            for file_path, error in self.failed_files:
                print(f"  - {file_path}")
                print(f"    {error}")

def main():
    # Define files to translate
    files_to_translate = [
        "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko/integrations/litellm/README.md",
    ]

    try:
        translator = MarkdownTranslator()
        translator.translate_files(files_to_translate)

        # Return exit code based on failures
        sys.exit(0 if translator.failed_count == 0 else 1)

    except ValueError as e:
        print(f"Error: {str(e)}")
        print("\nPlease set the ANTHROPIC_API_KEY environment variable:")
        print("export ANTHROPIC_API_KEY='your-api-key-here'")
        sys.exit(1)

if __name__ == '__main__':
    main()
