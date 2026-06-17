#!/usr/bin/env python3
"""
Check translation status for Flowise documentation
"""

from pathlib import Path
import json

EN_DIR = Path("en")
KO_DIR = Path("ko")

# Get all files
en_files = sorted(EN_DIR.rglob("*.md"))
ko_files = sorted(KO_DIR.rglob("*.md"))

# Create mappings
en_paths = {str(f.relative_to(EN_DIR)) for f in en_files}
ko_paths = {str(f.relative_to(KO_DIR)) for f in ko_files}

# Find missing translations
missing = en_paths - ko_paths
translated = en_paths & ko_paths

print(f"Total English files: {len(en_files)}")
print(f"Total Korean files: {len(ko_files)}")
print(f"Translated: {len(translated)}")
print(f"Missing translations: {len(missing)}")
print(f"Translation progress: {len(translated)}/{len(en_files)} ({100*len(translated)/len(en_files):.1f}%)")

if missing:
    print(f"\nMissing translations ({len(missing)}):")
    for f in sorted(missing)[:20]:
        print(f"  - {f}")
    if len(missing) > 20:
        print(f"  ... and {len(missing) - 20} more")
