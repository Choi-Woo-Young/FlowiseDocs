# Flowise Documentation Korean Translation Guide

## Overview

This guide explains how to use the Korean translation tool to translate Flowise documentation files from English to Korean using the Anthropic Claude API.

## Current Status

The translation tool supports translating markdown files from the `ko/` directory. These files currently contain English content and need to be translated to Korean.

## Files to Translate (Batch of 17)

The default translation batch includes these 17 files:

1. `ko/integrations/llamaindex/README.md`
2. `ko/integrations/README.md`
3. `ko/text-splitters/charater-text-splitter.md`
4. `ko/migration-guide/v1.4.3-migration-guide.md`
5. `ko/migration-guide/v2.1.4-migration-guide.md`
6. `ko/migration-guide/v1.3.0-migration-guide.md`
7. `ko/use-cases/multiple-documents-qna.md`
8. `ko/use-cases/web-scrape-qna.md`
9. `ko/use-cases/sql-qna.md`
10. `ko/use-cases/README.md`
11. `ko/use-cases/webhook-tool.md`
12. `ko/use-cases/interacting-with-api.md`
13. `ko/use-cases/upserting-data.md`
14. `ko/using-flowise/agentflowv1/README.md`
15. `ko/using-flowise/analytics/langfuse.md`
16. `ko/integrations/utilities/README.md`
17. `ko/integrations/llamaindex/vector-stores/README.md`

## Prerequisites

### 1. Install Python Dependencies

```bash
pip install requests
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
ANTHROPIC_API_KEY="your-api-key-here" python3 scripts/translate_to_korean.py
```

## Usage

### Basic Translation (All Default Files)

```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 scripts/translate_to_korean.py
```

Or using the shell wrapper:

```bash
./scripts/translate.sh
```

### Translate Specific Files

```bash
python3 scripts/translate_to_korean.py \
  ko/integrations/llamaindex/README.md \
  ko/integrations/README.md
```

### What the Script Does

1. **Reads markdown files** from the `ko/` directory
2. **Extracts content** to be translated
3. **Calls Anthropic Claude API** for translation
4. **Preserves code blocks** completely unchanged
5. **Keeps technical terms in English** (API, LLM, RAG, etc.)
6. **Writes translated content** back to the same files
7. **Reports progress** with success/failure counts

## Translation Rules

The script enforces these translation rules:

### Content to Translate
- All headings (# ## ### etc.)
- Paragraphs and descriptions
- List items (both bullet and numbered)
- Table headers and cells
- Link text and image captions
- YAML frontmatter metadata (description field)

### Content to Preserve (Keep in English)
- **Code blocks**: All content inside ``` ... ``` blocks
- **Technical Terms**: Flowise, API, LLM, RAG, Agent, Flow, OpenAI, Azure, Docker, GitHub, HTTP, REST, JSON, YAML, Python, Node.js, JavaScript, TypeScript, React, Vue, Kubernetes, AWS, GCP, SQL, MongoDB, Redis, PostgreSQL, MySQL, LlamaIndex, Agents, Vector Stores, Embeddings, ChatGPT, GPT-4, OpenAI API, Node, Express, Next.js, FastAPI, Flask, and other established technical terms
- **URLs and file paths**: Completely unchanged (only translate link text)
- **Environment variables and configuration keys**: Keep as-is
- **Command-line flags and options**: Preserve in English
- **Markdown formatting** (# ## ###, -, *, **, [text](url), tables, etc.)
- **HTML tags** (if present)

### Link Translation
For markdown links: `[English text](url)` becomes `[한국어 텍스트](url)`

Example:
- Input: `[Click here](https://example.com)` 
- Output: `[여기를 클릭하세요](https://example.com)`

## Expected Output

### Successful Run
```
Starting translation of 17 files...
Using model: claude-opus-4-1-20250805

[1/17] README.md... ✓
[2/17] charater-text-splitter.md... ✓
[3/17] v1.4.3-migration-guide.md... ✓
...
[17/17] vector-stores/README.md... ✓

==================================================
최종 배치 완료: 17개 파일 번역 완료
실패: 0개
==================================================
```

### File Structure After Translation

The script translates files in-place. The `ko/` directory structure remains unchanged, but the content is now in Korean:

```
FlowiseDocs/
└── ko/
    ├── integrations/
    │   ├── llamaindex/
    │   │   ├── README.md (Now in Korean!)
    │   │   └── vector-stores/
    │   │       └── README.md (Now in Korean!)
    │   ├── utilities/
    │   │   └── README.md (Now in Korean!)
    │   └── README.md (Now in Korean!)
    ├── text-splitters/
    │   └── charater-text-splitter.md (Now in Korean!)
    ├── migration-guide/
    │   ├── v1.4.3-migration-guide.md (Now in Korean!)
    │   ├── v2.1.4-migration-guide.md (Now in Korean!)
    │   └── v1.3.0-migration-guide.md (Now in Korean!)
    ├── use-cases/
    │   ├── multiple-documents-qna.md (Now in Korean!)
    │   ├── web-scrape-qna.md (Now in Korean!)
    │   ├── sql-qna.md (Now in Korean!)
    │   ├── webhook-tool.md (Now in Korean!)
    │   ├── interacting-with-api.md (Now in Korean!)
    │   ├── upserting-data.md (Now in Korean!)
    │   └── README.md (Now in Korean!)
    └── using-flowise/
        ├── agentflowv1/
        │   └── README.md (Now in Korean!)
        └── analytics/
            └── langfuse.md (Now in Korean!)
```

## Verification

After translation completes, verify the results:

### 1. Check a Sample File

```bash
head -20 ko/integrations/llamaindex/README.md
```

Expected: Korean text with preserved English technical terms and code blocks. For example:
```
---
description: Flowise가 LlamaIndex 프레임워크와 통합되는 방법을 알아보세요
---

# LlamaIndex
...
```

### 2. Verify Korean Characters

```bash
# Should show many Korean characters
grep -o '[가-힣]' ko/integrations/llamaindex/README.md | wc -l
```

Should return a number greater than 0.

### 3. Check Code Blocks Preserved

```bash
# Should find code blocks intact
grep -c '```' ko/use-cases/sql-qna.md
```

Should match the English version (code blocks unchanged).

### 4. Verify URLs Unchanged

```bash
# Should find all URLs preserved
grep -o 'https://[^)]\+' ko/integrations/README.md
```

URLs should remain exactly as in the original English files.

## Troubleshooting

### Error: ANTHROPIC_API_KEY environment variable is not set

**Solution**: Set the API key before running the script:
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
python3 scripts/translate_to_korean.py
```

To make it permanent, add to your shell profile (`~/.bashrc` or `~/.zshrc`):
```bash
echo "export ANTHROPIC_API_KEY='your-api-key-here'" >> ~/.zshrc
source ~/.zshrc
```

### Error: requests library not found

**Solution**: Install the requests library:
```bash
pip install requests
```

### Error: API error 401 Unauthorized

**Cause**: Invalid or expired API key

**Solution**:
1. Check your API key is correct
2. Log into [Anthropic Console](https://console.anthropic.com) and regenerate if needed
3. Update the environment variable

### Some Files Failed to Translate

**Possible causes**:
- Large files exceeding token limits
- Network issues
- Rate limiting (too many requests)

**Solution**:
- The script reports which files failed
- You can re-run the script to retry failed files
- Increase the delay between requests: `--delay 5.0`
- Wait a few minutes if rate limited

### API Error: 429 Too Many Requests

**Solution**: Increase the delay between API calls:
```bash
python3 scripts/translate_to_korean.py --delay 5.0
```

### Code Blocks Appear to Have Korean Characters

**Cause**: API incorrectly translated code

**Solution**:
- Check the file's backtick formatting
- Ensure code blocks use ``` with language specifier
- Report the specific file for investigation

## Performance Notes

- **Model**: Claude Opus 4.1 (20250805) - Best for translation quality
- **Average speed**: ~3-5 seconds per file (depends on file size and internet)
- **Total time for 17 files**: ~1-2 minutes
- **Cost**: Approximately $0.05-0.15 USD for 17 files
- **Rate limit**: 2 second delay between requests (configurable)

## Custom Options

### Adjust API Request Delay

```bash
# Faster (but may hit rate limits)
python3 scripts/translate_to_korean.py --delay 1.0

# Slower (safer for rate limits)
python3 scripts/translate_to_korean.py --delay 5.0
```

### Translate from Custom Base Path

```bash
python3 scripts/translate_to_korean.py --base-path /custom/path
```

### Add More Files to Translation

Edit `scripts/translate_to_korean.py` and update the `DEFAULT_FILES` list to include additional files.

## Updating Translations

If you need to re-translate files:

1. **For new files**: Add to the `DEFAULT_FILES` list in the script
2. **For modified files**: Simply run the script again (overwrites with new translation)
3. **For partial updates**: Pass specific files as arguments to the script

## Quality Assurance

After translation:

1. **Review a sample file** for accuracy and tone
2. **Check code blocks** are not translated
3. **Verify technical terms** remain in English
4. **Test links** are not broken
5. **Check YAML frontmatter** metadata is properly translated

## SEO Considerations

Since translations are for technical documentation:
- Korean headings accurately reflect content for search indexing
- Technical terms remain in English (searchable in Korean tech documentation)
- Meta descriptions are translated to Korean for Korean search engines
- File structure and URLs remain unchanged for proper redirects

## Commit and Deploy

After successful translation and verification:

```bash
# Stage translated files
git add ko/

# Create meaningful commit message
git commit -m "Translate 17 Flowise documentation files to Korean

- Translated integrations, migration guides, use cases, and analytics docs
- Preserved code blocks and technical terms in English
- Updated YAML frontmatter descriptions"

# Push to repository
git push origin main
```

## Support

If issues occur:
1. Check that `ANTHROPIC_API_KEY` is set correctly
2. Verify internet connection
3. Check API quota/rate limits at [Anthropic Console](https://console.anthropic.com)
4. Review the failed files list for patterns
5. Ensure Python 3.7+ is installed

## Script Location

- **Main script**: `/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/scripts/translate_to_korean.py`
- **Shell wrapper**: `/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/scripts/translate.sh`
- **This guide**: `/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/TRANSLATION_GUIDE.md`
