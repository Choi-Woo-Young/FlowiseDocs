#!/usr/bin/env python3
"""
Flowise Documentation Korean Translation Tool
Translates markdown files from English to Korean using Anthropic Claude API
"""

import os
import json
import sys
import time
import argparse
from pathlib import Path
from typing import Tuple

try:
    import requests
except ImportError:
    print("Error: requests library not found. Install with: pip install requests")
    sys.exit(1)

# Configuration
API_ENDPOINT = "https://api.anthropic.com/v1/messages"
MODEL = "claude-opus-4-1-20250805"

TRANSLATION_PROMPT = """You are a professional translator specializing in technical documentation for Flowise, an open-source LLM orchestration platform. Your task is to translate English markdown content to Korean while following these rules:

TRANSLATION RULES:
1. Translate all titles, headings, body text, and table content to Korean
2. Keep code blocks completely unchanged (do not translate code inside code blocks)
3. Keep image paths and URLs unchanged
4. Translate link text, but keep the actual URLs unchanged
5. Keep these technical terms in ENGLISH (do not translate):
   - Flowise, API, LLM, RAG, Agent, Flow, OpenAI, Azure, Docker, GitHub, HTTP, REST, JSON, YAML
   - Python, Node.js, JavaScript, TypeScript, React, Vue
   - Kubernetes, AWS, GCP, EC2, S3
   - SQL, MongoDB, Redis, PostgreSQL, MySQL, Pinecone, Weaviate, Chroma, Milvus
   - LlamaIndex, Langchain, OpenAI API, GPT-4, ChatGPT
   - Node, Express, Next.js, FastAPI, Flask
   - Any environment variables, configuration keys, and command-line flags
   - Any product names and service names (e.g., Supabase, Firebase, Vercel)
6. Preserve all Markdown/HTML structure exactly:
   - Keep all heading levels (#, ##, ###, etc.)
   - Preserve all lists, tables, code blocks
   - Keep all links and images intact
   - Preserve YAML frontmatter structure
7. Translate YAML frontmatter metadata (especially description field) to Korean
8. Use formal, professional Korean tone appropriate for technical documentation
9. Ensure readability and clarity in Korean
10. Return ONLY the translated markdown content without any explanations or commentary

ENGLISH CONTENT TO TRANSLATE:
"""

# Default files to translate
DEFAULT_FILES = [
    "ko/integrations/llamaindex/README.md",
    "ko/integrations/README.md",
    "ko/text-splitters/charater-text-splitter.md",
    "ko/migration-guide/v1.4.3-migration-guide.md",
    "ko/migration-guide/v2.1.4-migration-guide.md",
    "ko/migration-guide/v1.3.0-migration-guide.md",
    "ko/use-cases/multiple-documents-qna.md",
    "ko/use-cases/web-scrape-qna.md",
    "ko/use-cases/sql-qna.md",
    "ko/use-cases/README.md",
    "ko/use-cases/webhook-tool.md",
    "ko/use-cases/interacting-with-api.md",
    "ko/use-cases/upserting-data.md",
    "ko/using-flowise/agentflowv1/README.md",
    "ko/using-flowise/analytics/langfuse.md",
    "ko/integrations/utilities/README.md",
    "ko/integrations/llamaindex/vector-stores/README.md",
]


class KoreanTranslator:
    """Handles translation of markdown files to Korean using Anthropic API"""

    def __init__(self, api_key: str, base_path: str = "."):
        """Initialize translator with API key and base path"""
        self.api_key = api_key
        self.base_path = Path(base_path)
        self.success_count = 0
        self.failed_count = 0
        self.results = []

        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    def translate_file(self, file_path: str) -> Tuple[bool, str]:
        """
        Translate a single markdown file

        Args:
            file_path: Path to the markdown file

        Returns:
            Tuple of (success: bool, message: str)
        """
        full_path = self.base_path / file_path

        if not full_path.exists():
            return False, f"File not found: {full_path}"

        try:
            # Read the file
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Create the request payload
            payload = {
                "model": MODEL,
                "max_tokens": 4096,
                "messages": [
                    {
                        "role": "user",
                        "content": TRANSLATION_PROMPT + content
                    }
                ]
            }

            # Make the API request
            headers = {
                "x-api-key": self.api_key,
                "Content-Type": "application/json"
            }

            response = requests.post(API_ENDPOINT, json=payload, headers=headers, timeout=60)

            if response.status_code != 200:
                error_text = response.text
                try:
                    error_data = response.json()
                    error_msg = error_data.get('error', {}).get('message', error_text)
                except:
                    error_msg = error_text
                return False, f"API error {response.status_code}: {error_msg}"

            response_data = response.json()

            if "error" in response_data:
                return False, f"API error: {response_data['error'].get('message', 'Unknown error')}"

            # Extract the translated content
            if not response_data.get("content"):
                return False, "No content in API response"

            translated_content = response_data["content"][0]["text"]

            # Write the translated content back to file
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            return True, "Successfully translated"

        except requests.exceptions.Timeout:
            return False, "API request timed out"
        except requests.exceptions.RequestException as e:
            return False, f"Request error: {str(e)}"
        except Exception as e:
            return False, f"Error: {str(e)}"

    def translate_files(self, files: list, delay: float = 2.0) -> dict:
        """
        Translate multiple files with rate limiting

        Args:
            files: List of file paths to translate
            delay: Delay between API calls in seconds

        Returns:
            Dictionary with summary statistics
        """
        total = len(files)
        print(f"Starting translation of {total} files...")
        print(f"Using model: {MODEL}")
        print("")

        for i, file_path in enumerate(files, 1):
            file_name = Path(file_path).name
            print(f"[{i}/{total}] {file_name}...", end=" ", flush=True)

            success, message = self.translate_file(file_path)

            if success:
                print("✓")
                self.success_count += 1
                self.results.append((file_path, True, message))
            else:
                print(f"✗ ({message})")
                self.failed_count += 1
                self.results.append((file_path, False, message))

            # Rate limiting: delay between requests
            if i < total:
                time.sleep(delay)

        return self.get_summary()

    def get_summary(self) -> dict:
        """Get translation summary"""
        return {
            "total": self.success_count + self.failed_count,
            "success": self.success_count,
            "failed": self.failed_count,
            "results": self.results
        }

    def print_summary(self):
        """Print summary in Korean"""
        summary = self.get_summary()
        print("")
        print("=" * 50)
        print(f"최종 배치 완료: {summary['success']}개 파일 번역 완료")
        print(f"실패: {summary['failed']}개")
        print("=" * 50)

        if summary['failed'] > 0:
            print("\n실패한 파일:")
            for file_path, success, message in summary['results']:
                if not success:
                    print(f"  - {file_path}: {message}")


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Translate Flowise documentation to Korean",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Translate default files
  python translate_to_korean.py

  # Translate specific files
  python translate_to_korean.py ko/README.md ko/configuration/README.md

  # Set custom API key
  ANTHROPIC_API_KEY=your_key python translate_to_korean.py
"""
    )

    parser.add_argument(
        "files",
        nargs="*",
        help="Files to translate (uses default list if not provided)"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Delay between API calls in seconds (default: 2.0)"
    )

    parser.add_argument(
        "--base-path",
        default=".",
        help="Base path for file operations (default: current directory)"
    )

    args = parser.parse_args()

    # Get API key
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable is not set")
        print("")
        print("Please set your API key:")
        print("  export ANTHROPIC_API_KEY='your-api-key'")
        sys.exit(1)

    # Determine files to translate
    files = args.files if args.files else DEFAULT_FILES

    # Create translator and run
    try:
        translator = KoreanTranslator(api_key, base_path=args.base_path)
        translator.translate_files(files, delay=args.delay)
        translator.print_summary()

        # Exit with appropriate code
        sys.exit(0 if translator.failed_count == 0 else 1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\nTranslation interrupted by user")
        sys.exit(1)


if __name__ == "__main__":
    main()
