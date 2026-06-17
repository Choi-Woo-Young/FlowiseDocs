#!/usr/bin/env python3
"""
Translate Flowise documentation files from English to Korean using Claude.
Efficiently processes files and handles both existing and newly-to-be-created files.
"""
import os
import sys
import json
from pathlib import Path
from datetime import datetime

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

def main():
    base_en_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
    base_ko_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

    # Scan for actual existing files
    print("Scanning for existing files...")
    existing_files = []
    missing_files = []

    for file_path in FILES_TO_TRANSLATE:
        en_file = os.path.join(base_en_dir, file_path)
        if os.path.exists(en_file):
            existing_files.append(file_path)
        else:
            missing_files.append(file_path)

    print(f"Found {len(existing_files)} existing files")
    print(f"Found {len(missing_files)} missing files")

    if missing_files:
        print(f"\nMissing files (will skip):")
        for f in missing_files[:10]:
            print(f"  - {f}")
        if len(missing_files) > 10:
            print(f"  ... and {len(missing_files) - 10} more")

    # Output summary
    print(f"\n=== File Availability Summary ===")
    print(f"Total requested: {len(FILES_TO_TRANSLATE)}")
    print(f"Existing & ready to translate: {len(existing_files)}")
    print(f"Missing from source: {len(missing_files)}")
    print(f"Translation ready: {len(existing_files) > 0}")

    # Save list of files to translate
    with open(f"{base_ko_dir}/../files_to_translate.json", "w") as f:
        json.dump({
            "existing": existing_files,
            "missing": missing_files,
            "total_existing": len(existing_files),
            "timestamp": datetime.now().isoformat()
        }, f, indent=2)

    # Return count for main process
    return len(existing_files), len(missing_files)

if __name__ == "__main__":
    existing, missing = main()
    print(f"\nReady to translate {existing} files")
