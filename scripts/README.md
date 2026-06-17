# Translation Scripts

This directory contains scripts for translating Flowise documentation to Korean using the Anthropic Claude API.

## Files in This Directory

### `translate_to_korean.py`
Main Python script that handles the translation workflow.

**Usage:**
```bash
python3 translate_to_korean.py [options] [files...]
```

**Options:**
- `--delay N.N`: Delay between API calls in seconds (default: 2.0)
- `--base-path PATH`: Base directory for file operations (default: current directory)
- `[files...]`: Specific files to translate (uses defaults if not provided)

**Example:**
```bash
# Translate all default files
python3 translate_to_korean.py

# Translate specific files
python3 translate_to_korean.py ko/README.md ko/configuration/README.md

# Use longer delay for rate limiting
python3 translate_to_korean.py --delay 5.0
```

### `translate.sh`
Convenience shell wrapper around the Python script.

**Usage:**
```bash
./translate.sh [options]
```

Equivalent to:
```bash
python3 translate_to_korean.py [options]
```

**Example:**
```bash
./translate.sh --delay 3.0
```

## Configuration

### Environment Variables

**Required:**
- `ANTHROPIC_API_KEY`: Your Anthropic API key from https://console.anthropic.com/

**Set it:**
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### Translation Parameters (Hardcoded in Script)

Edit the script directly to modify these:
- `MODEL`: Claude model to use (currently: `claude-opus-4-1-20250805`)
- `DEFAULT_FILES`: List of files to translate by default
- `TRANSLATION_PROMPT`: Translation rules and instructions

## Default Files

The script translates these 17 files by default:

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

## Quick Start

```bash
# 1. Set API key
export ANTHROPIC_API_KEY='your-key-here'

# 2. Navigate to project root
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs

# 3. Run translation
python3 scripts/translate_to_korean.py

# Expected output:
# 최종 배치 완료: 17개 파일 번역 완료
# 실패: 0개
```

## Translation Rules

The scripts enforce these translation rules:

### Translate
- Headings, paragraphs, lists, tables
- Link text and image captions
- YAML frontmatter metadata (description field)

### Keep in English
- Code blocks (all content unchanged)
- Technical terms (Flowise, API, LLM, RAG, Agent, Flow, etc.)
- URLs and file paths
- Environment variables and configuration keys
- Command-line flags

## Error Handling

The script handles these error cases gracefully:

- Missing files (skipped with warning)
- API errors (reported with details)
- Network timeouts (reported with details)
- Invalid API keys (clear error message)

Failed files are listed at the end with error messages.

## Performance

- **Average time**: ~3-5 seconds per file
- **Total for 17 files**: ~1-2 minutes
- **Model**: Claude Opus 4.1 (best for translations)
- **Rate limit**: 2-second delay between requests (configurable)

## Cost Estimation

Approximate costs for a full run:
- Small batch (17 files): ~$0.05-0.15 USD
- Depends on file sizes and API pricing
- Check current pricing: https://www.anthropic.com/pricing

## Dependencies

- Python 3.7+
- `requests` library (install: `pip install requests`)

## Support

For detailed help, see:
- `TRANSLATION_GUIDE.md` - Complete guide with troubleshooting
- `QUICKSTART_TRANSLATION.md` - Quick 3-step setup

## License

Same as the Flowise project
