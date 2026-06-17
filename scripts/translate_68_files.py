#!/usr/bin/env python3
"""
Translate 68 Flowise documentation files from English to Korean.
"""
import os
import anthropic
import json
from pathlib import Path

# Initialize Anthropic client
client = anthropic.Anthropic()

# Files to translate (exact paths from user)
FILES_TO_TRANSLATE = [
    "README.md",
    "text-splitters/charater-text-splitter.md",
    "configuration/README.md",
    "configuration/databases.md",
    "configuration/environment-variables.md",
    "configuration/rate-limit.md",
    "configuration/running-flowise-behind-company-proxy.md",
    "configuration/running-flowise-using-queue.md",
    "configuration/running-in-production.md",
    "configuration/sso.md",
    "configuration/authorization/README.md",
    "configuration/authorization/app-level.md",
    "configuration/authorization/chatflow-level.md",
    "configuration/deployment/README.md",
    "configuration/deployment/aws.md",
    "configuration/deployment/azure.md",
    "configuration/deployment/digital-ocean.md",
    "configuration/deployment/gcp.md",
    "configuration/deployment/hugging-face.md",
    "configuration/deployment/railway.md",
    "configuration/deployment/render.md",
    "configuration/deployment/replit.md",
    "configuration/deployment/sealos.md",
    "configuration/deployment/zeabur.md",
    "contributing/README.md",
    "contributing/building-node.md",
    "migration-guide/README.md",
    "migration-guide/cloud-migration.md",
    "migration-guide/v1.3.0-migration-guide.md",
    "migration-guide/v1.4.3-migration-guide.md",
    "migration-guide/v2.1.4-migration-guide.md",
    "integrations/README.md",
    "integrations/3rd-party-platform-integration/README.md",
    "integrations/3rd-party-platform-integration/discord-chatbot.md",
    "integrations/3rd-party-platform-integration/firecrawl.md",
    "integrations/3rd-party-platform-integration/flowise-on-bubble.md",
    "integrations/3rd-party-platform-integration/flowise-on-vercel.md",
    "integrations/3rd-party-platform-integration/flowise-on-zapier.md",
    "integrations/3rd-party-platform-integration/make-formerly-integromat.md",
    "integrations/3rd-party-platform-integration/n8n.md",
    "integrations/3rd-party-platform-integration/notion-api.md",
    "integrations/3rd-party-platform-integration/pipedream.md",
    "integrations/3rd-party-platform-integration/slack-chatbot.md",
    "integrations/3rd-party-platform-integration/telegram-bot-with-streaming-2.md",
    "integrations/3rd-party-platform-integration/telegram-bot-with-streaming.md",
    "integrations/3rd-party-platform-integration/telegram-chatbot.md",
    "integrations/3rd-party-platform-integration/whatsapp-chatbot.md",
    "integrations/3rd-party-platform-integration/wix-chatbot.md",
    "integrations/3rd-party-platform-integration/wordpress-chatbot.md",
    "integrations/langchain/README.md",
    "integrations/langchain/agents/README.md",
    "integrations/langchain/agents/openai-assistant/README.md",
    "integrations/langchain/agents/openai-assistant/threads.md",
    "integrations/langchain/cache/README.md",
    "integrations/langchain/chains/README.md",
    "integrations/langchain/chains/vectara-chain.md",
    "integrations/langchain/chat-models/README.md",
    "integrations/langchain/chat-models/google-ai.md",
    "integrations/langchain/document-loaders/README.md",
    "integrations/langchain/moderation/README.md",
    "integrations/langchain/moderation/openai-moderation.md",
    "integrations/langchain/moderation/simple-prompt-moderation.md",
    "integrations/langchain/output-parsers/README.md",
    "integrations/langchain/prompts/README.md",
    "integrations/langchain/retrievers/README.md",
    "integrations/langchain/text-splitters/README.md",
    "integrations/langchain/tools/README.md",
    "integrations/langchain/vector-stores/README.md",
]

def translate_file(content):
    """Translate English content to Korean using Claude."""
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": f"""Translate the following Flowise documentation from English to Korean.

TRANSLATION RULES:
1. Translate all text content to Korean
2. Keep code blocks as-is (do not translate)
3. Keep paths, URLs, and technical terms in English
4. Preserve markdown formatting exactly
5. Maintain all links and references

Content to translate:
{content}"""
            }
        ]
    )
    return message.content[0].text

def main():
    base_en_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
    base_ko_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

    # Create status tracking
    status = {
        "total": len(FILES_TO_TRANSLATE),
        "completed": 0,
        "failed": [],
        "skipped": []
    }

    for file_path in FILES_TO_TRANSLATE:
        en_file = os.path.join(base_en_dir, file_path)
        ko_file = os.path.join(base_ko_dir, file_path)

        print(f"Processing: {file_path}")

        # Check if source file exists
        if not os.path.exists(en_file):
            print(f"  ✗ Source file not found: {en_file}")
            status["skipped"].append(file_path)
            continue

        # Read English content
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                en_content = f.read()
        except Exception as e:
            print(f"  ✗ Error reading source: {e}")
            status["failed"].append({"file": file_path, "error": str(e)})
            continue

        # Translate content
        try:
            ko_content = translate_file(en_content)
        except Exception as e:
            print(f"  ✗ Translation error: {e}")
            status["failed"].append({"file": file_path, "error": str(e)})
            continue

        # Create target directory if needed
        ko_dir = os.path.dirname(ko_file)
        os.makedirs(ko_dir, exist_ok=True)

        # Write Korean content
        try:
            with open(ko_file, 'w', encoding='utf-8') as f:
                f.write(ko_content)
            print(f"  ✓ Translated: {file_path}")
            status["completed"] += 1
        except Exception as e:
            print(f"  ✗ Error writing target: {e}")
            status["failed"].append({"file": file_path, "error": str(e)})

    # Save status
    status_file = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/.translation_status_68.json"
    with open(status_file, 'w') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)

    print(f"\n=== Translation Summary ===")
    print(f"Total files: {status['total']}")
    print(f"Completed: {status['completed']}")
    print(f"Failed: {len(status['failed'])}")
    print(f"Skipped: {len(status['skipped'])}")

    if status["failed"]:
        print(f"\nFailed files:")
        for item in status["failed"]:
            print(f"  - {item['file']}: {item['error']}")

    if status["skipped"]:
        print(f"\nSkipped files:")
        for item in status["skipped"]:
            print(f"  - {item}")

if __name__ == "__main__":
    main()
