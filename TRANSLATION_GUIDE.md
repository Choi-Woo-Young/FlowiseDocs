# Flowise Documentation Translation Guide

## Overview

This guide explains how to translate the Flowise documentation from English to Korean using the provided translation script.

## Current Status

- **Total files**: 346 markdown files
- **English source**: `./en/` directory
- **Korean target**: `./ko/` directory
- **All 346 files have been copied to Korean folder but still contain English content**

## Files to Translate

The translation script will process all `.md` files in the following directories:

- `api-reference/` (16 files)
- `cli-reference/` (3 files)
- `configuration/` (12 files)
- `contributing/` (2 files)
- `getting-started/` (6 files)
- `integrations/` (150+ files)
- `migration-guide/` (7 files)
- `text-splitters/` (2 files)
- `tutorials/` (9 files)
- `use-cases/` (8 files)
- `using-flowise/` (16 files)
- `README.md` and `SUMMARY.md` (2 files)

**Excluded**: `.gitbook/` directory (GitBook assets and configuration)

## Prerequisites

### 1. Install Python Dependencies

```bash
pip install anthropic
```

### 2. Get Your Anthropic API Key

1. Go to [Anthropic Console](https://console.anthropic.com)
2. Sign in or create an account
3. Navigate to the API Keys section
4. Create a new API key
5. Copy the key

### 3. Set Environment Variable

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Or temporarily for one command:

```bash
ANTHROPIC_API_KEY="your-api-key-here" python3 translate_to_korean.py
```

## Usage

### Basic Translation

```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 translate_to_korean.py
```

### What the Script Does

1. **Reads all English files** from the `en/` directory
2. **Extracts code blocks** to preserve them unchanged
3. **Translates content** to Korean using Claude API
4. **Restores code blocks** to the translated content
5. **Creates Korean files** in the `ko/` directory with the same structure
6. **Reports progress** with file counts and any errors

## Translation Rules Enforced by Script

### Content to Translate
- All headings (# ## ### etc.)
- Paragraphs and descriptions
- List items (both bullet and numbered)
- Table headers and cells
- Image captions

### Content to Preserve (English)
- **Technical Terms**: API, LLM, RAG, Node, Agent, Tool, Flowise, JSON, HTTP, REST, CLI, SDK, Docker, Kubernetes, AWS, Azure, GCP, Redis, PostgreSQL, MongoDB, JavaScript, TypeScript, Python, Node.js, Express, React, OpenAI, Anthropic, Claude, GPT, LLAMA, and 100+ other technical terms
- **Code blocks** (``` blocks and inline `code`)
- **URLs and file paths** (completely unchanged)
- **Markdown formatting** (# ## ###, -, *, **, [text](url), tables, etc.)
- **HTML tags** (if present)

### Link Translation
For markdown links: `[English text](url)` becomes `[한국어 텍스트](url)`

## Expected Output

### Successful Run
```
Found 346 markdown files to process
Source: /Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en
Target: /Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko

Starting translation...

[1/346] README.md ✓
[2/346] SUMMARY.md ✓
[3/346] api-reference/README.md ✓
...
[346/346] use-cases/some-file.md ✓

================================================================================
Translation Summary:
================================================================================
Successfully translated: 345
Failed:                  1
Skipped:                 0
Total processed:         346

================================================================================
✓ All translations completed successfully!
  345 files translated to Korean
```

### File Structure After Translation

```
FlowiseDocs/
├── en/
│   ├── README.md
│   ├── api-reference/
│   │   ├── README.md
│   │   ├── assistants.md
│   │   └── ...
│   └── ...
└── ko/
    ├── README.md
    ├── api-reference/
    │   ├── README.md (Translated to Korean)
    │   ├── assistants.md (Translated to Korean)
    │   └── ...
    └── ...
```

## Verification

After translation completes, verify the results:

### 1. Check a Sample File

```bash
head -20 ko/configuration/running-flowise-using-queue.md
```

Expected: Korean text with preserved English technical terms and code blocks.

### 2. Verify Korean Characters

```bash
# Should show many Korean characters (유니코드 한글)
grep -o '[가-힣]' ko/README.md | wc -l
```

### 3. Check Code Blocks Preserved

```bash
# Should find code blocks intact
grep -c '```' ko/configuration/environment-variables.md
```

Should be the same count as in English version:

```bash
grep -c '```' en/configuration/environment-variables.md
```

### 4. Verify URLs Unchanged

```bash
# Should find all URLs preserved
grep -o 'https://[^)]\+' ko/getting-started/README.md
```

Compare with English version to ensure they match.

## Troubleshooting

### Error: ANTHROPIC_API_KEY environment variable not set

**Solution**: Set the API key before running the script:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
python3 translate_to_korean.py
```

### Error: Request failed with status 401

**Cause**: Invalid or expired API key

**Solution**:
1. Check your API key is correct
2. Log into Anthropic Console and regenerate if needed
3. Update the environment variable

### Some Files Failed to Translate

**Possible causes**:
- Large files exceeding token limits
- Network issues
- Rate limiting (too many requests)

**Solution**:
- The script reports which files failed
- You can re-run the script to retry failed files
- Check that ko/ directory has the correct structure before re-running
- Wait a few minutes if rate limited

### Code Blocks Appear Translated

**Cause**: Regex pattern didn't correctly identify code blocks

**Solution**:
- Check the file's backtick formatting
- Ensure code blocks use ``` with optional language specifier
- Report the file for debugging

## Performance Notes

- **Average speed**: ~2-3 seconds per file (depends on file size and internet)
- **Total time for 346 files**: ~15-30 minutes
- **Cost**: Approximately $0.50-$1.00 USD (using Claude 3.5 Sonnet)
- **Rate limit**: 50 requests per minute by default with Anthropic API

## Advanced: Processing Specific Directories

To translate only certain directories, modify the script to filter files:

```python
# In process_files() function, add:
if "integrations" not in en_file.parts:
    continue
```

Then run with that filter applied.

## Advanced: Batch Processing

For very large translation jobs, you can split the work:

```bash
# Get all files
find en -name "*.md" > all_files.txt

# Split into batches of 100
split -l 100 all_files.txt batch_

# Process each batch in parallel or sequentially
# Then combine results
```

## Updating Translations

If English files are updated:

1. **For new files**: Run the full script again (it will translate new files)
2. **For modified files**: Delete the translated Ko file and re-run script
3. **For sync**: Keep both `en/` and `ko/` in sync by regularly running this script

## SEO Considerations

Since translations are for technical documentation:
- Korean headings should accurately reflect English content for better search indexing
- Preserve technical terms in English (they're searchable in Korean tech documentation)
- Meta descriptions should be translated for Korean search engines

## Support

If issues occur:
1. Check that ANTHROPIC_API_KEY is set correctly
2. Verify internet connection
3. Check API quota/rate limits at console.anthropic.com
4. Review the failed files list for patterns
5. Check Python version: Python 3.7+

## Next Steps

1. Run the translation script
2. Verify a sample of translated files
3. Commit translated files to git
4. Deploy Korean documentation site

```bash
# After verification:
git add ko/
git commit -m "Translate Flowise documentation to Korean"
git push origin main
```
