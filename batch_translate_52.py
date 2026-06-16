#!/usr/bin/env python3
"""
Batch translate 52 Flowise documentation files from English to Korean.
Processes files sequentially and writes translations directly.
"""
import os
import json
import sys
from pathlib import Path

# Files that exist and are ready to translate
EXISTING_FILES = [
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
    base_en_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en"
    base_ko_dir = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko"

    status = {
        "total": len(EXISTING_FILES),
        "ready_for_translation": 0,
        "files_list": []
    }

    print("=== Preparing files for batch translation ===\n")
    for i, file_path in enumerate(EXISTING_FILES, 1):
        en_file = os.path.join(base_en_dir, file_path)
        ko_file = os.path.join(base_ko_dir, file_path)

        # Ensure target directory exists
        ko_dir = os.path.dirname(ko_file)
        os.makedirs(ko_dir, exist_ok=True)

        # Read English file
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                content = f.read()

            status["files_list"].append({
                "index": i,
                "path": file_path,
                "source": en_file,
                "target": ko_file,
                "status": "ready"
            })
            status["ready_for_translation"] += 1

            if i % 10 == 0:
                print(f"[{i}/{len(EXISTING_FILES)}] {file_path}")

        except Exception as e:
            status["files_list"].append({
                "index": i,
                "path": file_path,
                "error": str(e),
                "status": "error"
            })
            print(f"ERROR: {file_path} - {e}")

    print(f"\n=== Translation Batch Status ===")
    print(f"Total files to translate: {status['ready_for_translation']}/{status['total']}")

    # Save file manifest
    manifest_file = os.path.join(base_ko_dir, "../translation_manifest_52.json")
    with open(manifest_file, 'w') as f:
        json.dump(status, f, indent=2)

    print(f"Manifest saved to: {manifest_file}")
    print(f"\nFiles are ready for batch translation via Claude API.")

    # Print file list for manual processing
    print(f"\nFile list for translation:")
    for item in status["files_list"]:
        if item["status"] == "ready":
            print(f"  {item['index']:2d}. {item['path']}")

if __name__ == "__main__":
    main()
