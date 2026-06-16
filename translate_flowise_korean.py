#!/usr/bin/env python3
"""
Comprehensive Korean Translation Framework for Flowise Documentation
====================================================================

This script automatically translates English markdown files from the en/ directory
to proper Korean in the ko/ directory, using the Anthropic API.

Features:
- Preserves code blocks and inline code exactly
- Keeps product names (OpenAI, Anthropic, Flowise, etc.) in English
- Translates all narrative, instructional, and descriptive text to fluent Korean
- Maintains all markdown formatting
- Processes files in batches with proper rate limiting

Usage:
    export ANTHROPIC_API_KEY="sk-..."
    python3 translate_flowise_korean.py

Status Files:
- Creates .translation_status.json to track progress
- Can resume from interrupted runs
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
STATUS_FILE = Path(".translation_status.json")

# Technical terms to preserve in English
PRESERVE_TERMS = {
    "API", "LLM", "RAG", "JSON", "HTML", "XML", "REST", "GraphQL", "HTTP", "HTTPS",
    "OpenAI", "Groq", "Anthropic", "Claude", "Flowise", "FlowiseDocs", "GPT",
    "Node", "Agent", "Tool", "Flow", "Canvas", "Start", "Loop", "Iteration",
    "Agentflow", "Chatflow", "agentflow",
    "Document Store", "Vector Database", "LLM", "Retriever",
}

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
   - API names and technical acronyms: API, LLM, RAG, JSON, REST, HTTP, HTTPS, GraphQL
   - Product names: OpenAI, Groq, Anthropic, Claude, Flowise, FlowiseDocs, GPT
   - System component names: Agent, Flow, Node, Tool, Canvas, Agentflow, Chatflow, Retriever
3. NO English text should remain in descriptions (except items above)
4. Preserve ALL markdown formatting exactly: headers, bold, italics, lists, links, code blocks
5. Preserve all HTML tags and figure captions
6. Use formal, professional Korean technical terminology
7. Do NOT add, remove, or modify any content - only translate

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
    
    def get_en_source(self, ko_path):
        """Find corresponding English source file."""
        rel_path = ko_path.relative_to(KO_DIR)
        en_path = EN_DIR / rel_path
        return en_path if en_path.exists() else None
    
    def process_file(self, ko_path):
        """Process a single file for translation."""
        rel_path = str(ko_path.relative_to(KO_DIR))
        
        # Check if already processed
        if rel_path in self.status['completed_files']:
            return None  # Already done
        if rel_path in self.status['failed_files']:
            return False  # Previously failed
        
        # Find English source
        en_path = self.get_en_source(ko_path)
        if not en_path:
            self.status['skipped_files'].append(rel_path)
            return None  # No source
        
        try:
            # Read English source
            with open(en_path, 'r', encoding='utf-8') as f:
                en_content = f.read()
            
            # Translate
            ko_content = self.translate_text(en_content)
            
            # Write Korean translation
            with open(ko_path, 'w', encoding='utf-8') as f:
                f.write(ko_content)
            
            self.status['completed_files'].append(rel_path)
            return True
        
        except Exception as e:
            print(f"      ERROR: {str(e)[:60]}")
            self.status['failed_files'].append(rel_path)
            return False
    
    def run(self, file_limit=None):
        """Run translation process."""
        # Get all Korean markdown files
        ko_files = sorted(KO_DIR.rglob("*.md"))
        
        # Filter out already processed
        files_to_process = [
            f for f in ko_files
            if str(f.relative_to(KO_DIR)) not in self.status['completed_files']
            and str(f.relative_to(KO_DIR)) not in self.status['skipped_files']
        ]
        
        if file_limit:
            files_to_process = files_to_process[:file_limit]
        
        total = len(files_to_process)
        if total == 0:
            print("No files to process.")
            return
        
        print(f"\nStarting translation of {total} files...")
        print(f"Previously completed: {len(self.status['completed_files'])}")
        print("=" * 70)
        
        start_time = time.time()
        success_count = 0
        
        for i, ko_file in enumerate(files_to_process, 1):
            rel_path = ko_file.relative_to(KO_DIR)
            print(f"[{i}/{total}] {rel_path}...", end=" ", flush=True)
            
            try:
                result = self.process_file(ko_file)
                if result is True:
                    print("✓")
                    success_count += 1
                elif result is False:
                    print("✗")
                else:
                    print("⊘")  # Skipped
            
            except Exception as e:
                print(f"ERROR: {str(e)[:40]}")
            
            # Rate limiting
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
        print(f"  Completed: {success_count}/{total}")
        print(f"  Total completed: {len(self.status['completed_files'])}")
        print(f"  Failed: {len(self.status['failed_files'])}")
        print(f"  Skipped: {len(self.status['skipped_files'])}")


def main():
    """Main entry point."""
    try:
        translator = KoreanTranslator()
        
        # Check for command-line arguments
        file_limit = None
        if len(sys.argv) > 1:
            try:
                file_limit = int(sys.argv[1])
                print(f"Limiting to {file_limit} files")
            except ValueError:
                print(f"Invalid file limit: {sys.argv[1]}")
        
        translator.run(file_limit=file_limit)
    
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
