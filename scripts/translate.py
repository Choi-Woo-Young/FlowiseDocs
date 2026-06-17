#!/usr/bin/env python3
"""
Translate Flowise documentation files from English to Korean
Preserves code blocks, URLs, technical terms, and HTML tags
Uses Claude API for high-quality translations
"""

import os
import sys
import re
import json
import time
from pathlib import Path
from typing import Tuple, List, Dict

# Try to import required libraries
try:
    import anthropic
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


class TranslationPreserver:
    """Preserves code blocks and technical content during translation"""

    def __init__(self):
        self.code_blocks = {}
        self.code_block_counter = 0
        self.url_blocks = {}
        self.url_block_counter = 0
        self.yaml_blocks = {}
        self.yaml_block_counter = 0

    def preserve_code_blocks(self, content: str) -> str:
        """Replace code blocks with placeholders"""
        # Match fenced code blocks (``` ... ```)
        pattern = r'```[\s\S]*?```'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__CODE_BLOCK_{self.code_block_counter}__"
            self.code_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.code_block_counter += 1

        # Match inline code (`...`)
        pattern = r'`[^`]+`'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__INLINE_CODE_{self.code_block_counter}__"
            self.code_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.code_block_counter += 1

        return content

    def preserve_urls(self, content: str) -> str:
        """Replace URLs and special links with placeholders"""
        # Match URLs
        pattern = r'https?://[^\s)]+|www\.[^\s)]+'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__URL_{self.url_block_counter}__"
            self.url_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.url_block_counter += 1

        # Match file paths
        pattern = r'/[a-zA-Z0-9\-_./]+\.md'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__PATH_{self.url_block_counter}__"
            self.url_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.url_block_counter += 1

        return content

    def preserve_yaml_frontmatter(self, content: str) -> Tuple[str, str]:
        """Extract and preserve YAML frontmatter"""
        if content.startswith('---'):
            # Find the closing ---
            match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
            if match:
                yaml_block = match.group(0)
                rest = content[len(yaml_block):]
                placeholder = f"__YAML_BLOCK_{self.yaml_block_counter}__"
                self.yaml_blocks[placeholder] = yaml_block
                self.yaml_block_counter += 1
                return rest, placeholder

        return content, None

    def preserve_html_tags(self, content: str) -> str:
        """Replace HTML tags and special markdown elements with placeholders"""
        # Match HTML tags
        pattern = r'<[^>]+>'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__HTML_{self.code_block_counter}__"
            self.code_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.code_block_counter += 1

        # Match special GitBook syntax
        pattern = r'{%[^%]+%}'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__GITBOOK_{self.code_block_counter}__"
            self.code_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.code_block_counter += 1

        # Match ![...](...)
        pattern = r'!\[[^\]]*\]\([^\)]+\)'
        matches = re.finditer(pattern, content)

        for match in matches:
            placeholder = f"__IMAGE_{self.code_block_counter}__"
            self.code_blocks[placeholder] = match.group(0)
            content = content.replace(match.group(0), placeholder, 1)
            self.code_block_counter += 1

        return content

    def restore_preserved_content(self, content: str) -> str:
        """Restore all preserved content"""
        # Restore YAML blocks
        for placeholder, original in self.yaml_blocks.items():
            content = placeholder + '\n' + content if content.startswith('\n') else placeholder + '\n' + content
            # More careful restoration

        # Restore code blocks, URLs, and HTML
        all_preserved = {**self.code_blocks, **self.url_blocks}
        for placeholder, original in all_preserved.items():
            content = content.replace(placeholder, original)

        return content


class TranslationService:
    """Handle translation using available services"""

    def __init__(self):
        """Initialize translation service with Claude API"""
        self.client = None
        self.model = "claude-3-5-sonnet-20241022"
        self.request_count = 0
        self.last_request_time = 0
        self.min_delay = 0.1  # Minimum delay between requests (seconds)

        if HAS_ANTHROPIC:
            try:
                api_key = os.environ.get('ANTHROPIC_API_KEY')
                if api_key:
                    self.client = anthropic.Anthropic(api_key=api_key)
            except Exception as e:
                print(f"Failed to initialize Anthropic client: {e}", file=sys.stderr)

    def translate_text(self, text: str) -> str:
        """Translate text to Korean using Claude API"""
        if not text or not text.strip():
            return text

        if not self.client:
            print("Warning: Anthropic client not available, returning original text", file=sys.stderr)
            return text

        # Rate limiting
        elapsed = time.time() - self.last_request_time
        if elapsed < self.min_delay:
            time.sleep(self.min_delay - elapsed)

        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": f"""Translate the following English text to Korean.
Keep all code blocks, URLs, file paths, and technical terms in English.
Keep company/product names in English (e.g., Airtable, OpenAI, Redis).
Only translate descriptive and narrative text.
Return only the translated text without any explanation.

English text:
{text}"""
                    }
                ]
            )
            self.last_request_time = time.time()
            self.request_count += 1

            translated = message.content[0].text.strip()
            return translated

        except Exception as e:
            print(f"Translation error: {e}", file=sys.stderr)
            return text


class FileTranslator:
    """Translate documentation files"""

    def __init__(self, source_dir: str, target_dir: str):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)
        self.preserv = TranslationPreserver()
        self.translation_service = TranslationService()

    def translate_file(self, file_path: str) -> Tuple[bool, str]:
        """Translate a single markdown file"""
        try:
            source_file = self.source_dir / file_path

            if not source_file.exists():
                return False, f"File not found: {source_file}"

            # Read source file
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Process the file
            translated_content = self.process_file_content(content)

            # Create target directory if needed
            target_file = self.target_dir / file_path
            target_file.parent.mkdir(parents=True, exist_ok=True)

            # Write translated file
            with open(target_file, 'w', encoding='utf-8') as f:
                f.write(translated_content)

            return True, f"Translated: {file_path}"

        except Exception as e:
            return False, f"Error translating {file_path}: {str(e)}"

    def process_file_content(self, content: str) -> str:
        """Process and translate file content"""
        preserv = TranslationPreserver()

        # Handle YAML frontmatter
        rest_content, yaml_placeholder = preserv.preserve_yaml_frontmatter(content)

        # Preserve code blocks, URLs, HTML tags
        rest_content = preserv.preserve_code_blocks(rest_content)
        rest_content = preserv.preserve_urls(rest_content)
        rest_content = preserv.preserve_html_tags(rest_content)

        # Translate headings and regular text
        # Split by lines and translate
        lines = rest_content.split('\n')
        translated_lines = []

        for line in lines:
            translated_line = self.translate_line(line, preserv)
            translated_lines.append(translated_line)

        translated_content = '\n'.join(translated_lines)

        # Restore preserved content
        translated_content = preserv.restore_preserved_content(translated_content)

        # Restore YAML frontmatter if it existed
        if yaml_placeholder:
            yaml_block = preserv.yaml_blocks.get(yaml_placeholder, '')
            # Translate the description field in YAML
            yaml_block = self.translate_yaml_description(yaml_block, preserv)
            translated_content = yaml_block + translated_content

        return translated_content

    def translate_line(self, line: str, preserv: TranslationPreserver) -> str:
        """Translate a single line"""
        # Skip empty lines
        if not line.strip():
            return line

        # Skip lines that are all preserved content
        if all(placeholder in line for placeholder in preserv.code_blocks.keys()):
            return line

        # Translate headings (lines starting with #)
        if line.startswith('#'):
            match = re.match(r'^(#+\s+)(.+)$', line)
            if match:
                prefix = match.group(1)
                text = match.group(2)
                translated_text = self.translate_heading(text)
                return prefix + translated_text

        # Translate bullet points and list items
        if line.strip().startswith(('* ', '- ', '+ ')):
            match = re.match(r'^(\s*)([*\-+]\s+)(.+)$', line)
            if match:
                indent = match.group(1)
                marker = match.group(2)
                text = match.group(3)
                translated_text = self.translate_text(text)
                return indent + marker + translated_text

        # For other lines with preserved content, try to translate carefully
        if any(placeholder in line for placeholder in preserv.code_blocks.keys()):
            return line  # Don't translate lines with code

        # For numbered lists
        match = re.match(r'^(\s*)(\d+\.\s+)(.+)$', line)
        if match:
            indent = match.group(1)
            marker = match.group(2)
            text = match.group(3)
            translated_text = self.translate_text(text)
            return indent + marker + translated_text

        # Regular paragraph
        if line.strip() and not line.strip().startswith(('http', 'www', '#')):
            translated_line = self.translate_text(line.strip())
            # Preserve leading/trailing whitespace
            if line.startswith(' '):
                return ' ' + translated_line
            return translated_line

        return line

    def translate_heading(self, text: str) -> str:
        """Translate heading text"""
        if not text or not text.strip():
            return text

        try:
            translated = self.translation_service.translate_text(text)
            return translated if translated else text
        except Exception as e:
            print(f"Error translating heading: {e}", file=sys.stderr)
            return text

    def translate_text(self, text: str) -> str:
        """Translate regular text"""
        if not text or not text.strip():
            return text

        try:
            translated = self.translation_service.translate_text(text)
            return translated if translated else text
        except Exception as e:
            print(f"Error translating text: {e}", file=sys.stderr)
            return text

    def translate_yaml_description(self, yaml_block: str, preserv: TranslationPreserver) -> str:
        """Translate only the description field in YAML frontmatter"""
        # Match description field
        pattern = r'(description:\s*)(.+)'

        def replace_description(match):
            prefix = match.group(1)
            description = match.group(2)
            # Remove quotes if present
            description = description.strip('"\'')
            translated = self.translate_text(description)
            return f'{prefix}"{translated}"'

        yaml_block = re.sub(pattern, replace_description, yaml_block)
        return yaml_block


def main():
    """Main translation script"""
    source_dir = '/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en'
    target_dir = '/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko'

    files_to_translate = [
        'SUMMARY.md',
        'api-reference/chatflows.md',
        'api-reference/document-store.md',
        'api-reference/feedback.md',
        'api-reference/leads.md',
        'api-reference/ping.md',
        'api-reference/prediction.md',
        'api-reference/tools.md',
        'api-reference/upsert-history.md',
        'api-reference/variables.md',
        'api-reference/vector-upsert.md',
        'integrations/langchain/agents/airtable-agent.md',
        'integrations/langchain/agents/autogpt.md',
        'integrations/langchain/agents/babyagi.md',
        'integrations/langchain/agents/conversational-agent.md',
        'integrations/langchain/agents/conversational-retrieval-agent.md',
        'integrations/langchain/agents/mistralai-tool-agent.md',
        'integrations/langchain/agents/openai-assistant/threads.md',
        'integrations/langchain/agents/openai-function-agent.md',
        'integrations/langchain/agents/openai-tool-agent.md',
        'integrations/langchain/agents/react-agent-chat.md',
        'integrations/langchain/agents/react-agent-llm.md',
        'integrations/langchain/agents/tool-agent.md',
        'integrations/langchain/agents/xml-agent.md',
        'integrations/langchain/cache/in-memory-cache.md',
        'integrations/langchain/cache/inmemory-embedding-cache.md',
        'integrations/langchain/cache/momento-cache.md',
        'integrations/langchain/cache/redis-cache.md',
        'integrations/langchain/cache/redis-embeddings-cache.md',
        'integrations/langchain/cache/upstash-redis-cache.md',
        'integrations/langchain/chains/conversation-chain.md',
        'integrations/langchain/chains/conversational-retrieval-qa-chain.md',
        'integrations/langchain/chains/get-api-chain.md',
        'integrations/langchain/chains/llm-chain.md',
        'integrations/langchain/chains/multi-prompt-chain.md',
        'integrations/langchain/chains/multi-retrieval-qa-chain.md',
        'integrations/langchain/chains/openapi-chain.md',
        'integrations/langchain/chains/post-api-chain.md',
        'integrations/langchain/chains/retrieval-qa-chain.md',
        'integrations/langchain/chains/sql-database-chain.md',
        'integrations/langchain/chains/vectordb-qa-chain.md',
        'integrations/langchain/chat-models/aws-chatbedrock.md',
        'integrations/langchain/chat-models/azure-chatopenai-1.md',
        'integrations/langchain/chat-models/chat-fireworks.md',
        'integrations/langchain/chat-models/chat-sambanova.md',
        'integrations/langchain/chat-models/chatanthropic.md',
        'integrations/langchain/chat-models/chatcohere.md',
        'integrations/langchain/chat-models/chatcometapi.md',
        'integrations/langchain/chat-models/chathuggingface.md',
    ]

    translator = FileTranslator(source_dir, target_dir)

    successful = 0
    failed = 0
    errors = []

    print(f"Starting translation of {len(files_to_translate)} files...")
    print(f"Source: {source_dir}")
    print(f"Target: {target_dir}\n")

    for file_path in files_to_translate:
        success, message = translator.translate_file(file_path)
        if success:
            print(f"✓ {message}")
            successful += 1
        else:
            print(f"✗ {message}")
            errors.append(message)
            failed += 1

    print(f"\n{'='*60}")
    print(f"Translation Summary:")
    print(f"{'='*60}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {successful + failed}")

    if errors:
        print(f"\nErrors:")
        for error in errors:
            print(f"  - {error}")

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
