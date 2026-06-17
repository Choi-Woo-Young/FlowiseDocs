#!/usr/bin/env python3
"""
Verify that Korean translations are complete (not empty)
"""

from pathlib import Path
import os

EN_DIR = Path("en")
KO_DIR = Path("ko")

# Get all files
en_files = sorted(EN_DIR.rglob("*.md"))

# Verification
empty_files = []
valid_files = 0
size_mismatch = []

for en_file in en_files:
    rel_path = en_file.relative_to(EN_DIR)
    ko_file = KO_DIR / rel_path
    
    if not ko_file.exists():
        empty_files.append((str(rel_path), "Missing"))
        continue
    
    en_size = os.path.getsize(en_file)
    ko_size = os.path.getsize(ko_file)
    
    if ko_size == 0:
        empty_files.append((str(rel_path), "Empty"))
    elif ko_size < en_size * 0.5:  # Korean text is usually shorter, but not this short
        size_mismatch.append((str(rel_path), en_size, ko_size))
    else:
        valid_files += 1

print(f"Total files: {len(en_files)}")
print(f"Valid translations: {valid_files}")
print(f"Empty or missing: {len(empty_files)}")
print(f"Potential size mismatches: {len(size_mismatch)}")

if empty_files:
    print(f"\nEmpty or missing files:")
    for f, status in empty_files[:10]:
        print(f"  - {f} ({status})")

if size_mismatch:
    print(f"\nSize mismatch files (potential incomplete translations):")
    for f, en_size, ko_size in size_mismatch[:10]:
        print(f"  - {f} (EN: {en_size} bytes, KO: {ko_size} bytes)")

# Sample check - verify a few Korean files contain Korean characters
import random
print("\nSample verification of Korean content:")
sample_files = random.sample(list(en_files), min(5, len(en_files)))
for en_file in sample_files:
    rel_path = en_file.relative_to(EN_DIR)
    ko_file = KO_DIR / rel_path
    
    with open(ko_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for Korean characters (Hangul)
    has_korean = any('가' <= c <= '힯' for c in content)
    print(f"  {rel_path}: {'✓ Has Korean' if has_korean else '✗ No Korean'}")
