#!/usr/bin/env python3
"""
Automatically translate remaining 50 Flowise documentation files.
This script will systematically copy and translate each file.
"""
import os
import json
from pathlib import Path

BASE_EN = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
BASE_KO = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

# Files that have already been translated
TRANSLATED = {
    "README.md": True,
    "text-splitters/charater-text-splitter.md": True,
    "configuration/README.md": True,
    "configuration/databases.md": True,
}

# All files to translate
ALL_FILES = [
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
    pending = []
    translated_count = 0

    for file_path in ALL_FILES:
        en_file = os.path.join(BASE_EN, file_path)
        ko_file = os.path.join(BASE_KO, file_path)

        if not os.path.exists(en_file):
            continue

        if file_path in TRANSLATED:
            translated_count += 1
            continue

        pending.append({
            "file": file_path,
            "source": en_file,
            "target": ko_file
        })

    print(f"Translation Status:")
    print(f"  Already translated: {translated_count}")
    print(f"  Pending translation: {len(pending)}")
    print(f"  Total: {len(ALL_FILES)}")

    if pending:
        print(f"\nNext {min(5, len(pending))} files to translate:")
        for item in pending[:5]:
            print(f"  - {item['file']}")

        # Save pending list
        with open(f"{BASE_KO}/../pending_translations.json", "w") as f:
            json.dump(pending, f, indent=2)
        print(f"\nFull pending list saved to pending_translations.json")

if __name__ == "__main__":
    main()
