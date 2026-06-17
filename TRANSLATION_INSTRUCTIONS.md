# Flowise Documentation Translation Instructions

## Overview
The `translate_to_korean.py` script will translate all 103 English markdown files from the `en/` directory to Korean in the `ko/` directory.

## Prerequisites
1. Python 3.7 or higher
2. Anthropic SDK installed: `pip install anthropic`
3. Valid ANTHROPIC_API_KEY

## Steps to Run

### 1. Get Your Anthropic API Key
- Visit: https://console.anthropic.com
- Create an API key or use an existing one
- Copy your API key

### 2. Set the Environment Variable
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Replace `your-api-key-here` with your actual API key.

### 3. Run the Translation Script
```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 translate_to_korean.py
```

## What the Script Does
- Finds all markdown files in the `en/` directory (recursively)
- Preserves code blocks (both block and inline code)
- Keeps technical terms in English (API, LLM, RAG, Node, etc.)
- Maintains all markdown formatting
- Creates translated files in the `ko/` directory with the same structure
- Reports success/failure for each file
- Provides a summary at the end

## Expected Output Format
```
[1/103] path/to/file.md ✓
[2/103] path/to/file.md ✓
...
[103/103] path/to/file.md ✓

================================================================================
Translation Summary:
================================================================================
Successfully translated: 103
Failed:                  0
Skipped:                 0
Total processed:         103

================================================================================
✓ All translations completed successfully!
  103 files translated to Korean

최종 배치 3 완료: 103개
```

## Troubleshooting

### Error: ANTHROPIC_API_KEY environment variable not set
- Make sure you've set the environment variable before running the script
- Check: `echo $ANTHROPIC_API_KEY`
- If empty, run the export command again

### Error: anthropic SDK not installed
```bash
pip install anthropic
```

### API Rate Limiting
If you encounter rate limiting errors, the script will retry automatically.

## Additional Notes
- The script uses Claude 3.5 Sonnet model for translations
- Each file is processed sequentially
- Large files may take longer to translate
- The script preserves all markdown formatting and structure
