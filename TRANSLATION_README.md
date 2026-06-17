# Flowise Documentation Korean Translation Toolkit

Complete toolkit for translating Flowise documentation to Korean using the Anthropic Claude API.

## What's Included

This toolkit provides everything needed to translate 17 markdown files from English to Korean:

### Scripts
- **`scripts/translate_to_korean.py`** - Main translation script (Python)
- **`scripts/translate.sh`** - Shell wrapper for easy execution

### Documentation
- **`QUICKSTART_TRANSLATION.md`** - Get started in 3 steps
- **`TRANSLATION_GUIDE.md`** - Complete guide with all details
- **`scripts/README.md`** - Script reference and configuration

## Quick Start (3 Steps)

### 1. Get API Key
Visit https://console.anthropic.com/ → Create API key → Copy it

### 2. Set Environment
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

### 3. Run Translation
```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 scripts/translate_to_korean.py
```

Expected completion: 최종 배치 완료: 17개 파일 번역 완료

## Files to Translate (17 Total)

```
ko/
├── integrations/
│   ├── README.md
│   ├── utilities/README.md
│   └── llamaindex/
│       ├── README.md
│       └── vector-stores/README.md
├── text-splitters/
│   └── charater-text-splitter.md
├── migration-guide/
│   ├── v1.4.3-migration-guide.md
│   ├── v2.1.4-migration-guide.md
│   └── v1.3.0-migration-guide.md
├── use-cases/
│   ├── README.md
│   ├── multiple-documents-qna.md
│   ├── web-scrape-qna.md
│   ├── sql-qna.md
│   ├── webhook-tool.md
│   ├── interacting-with-api.md
│   └── upserting-data.md
└── using-flowise/
    ├── agentflowv1/README.md
    └── analytics/langfuse.md
```

## Key Features

✓ **Automatic Translation**: Converts English to Korean using Claude API
✓ **Preserves Code**: Code blocks remain completely unchanged
✓ **Keeps Technical Terms**: English terms stay English (API, LLM, RAG, etc.)
✓ **Maintains Structure**: Markdown formatting and links preserved
✓ **Error Handling**: Reports failures clearly
✓ **Rate Limiting**: Built-in delays to avoid API limits
✓ **Progress Tracking**: Shows real-time translation progress
✓ **Flexible**: Translates default files or custom list

## Usage Examples

### Translate all default files
```bash
python3 scripts/translate_to_korean.py
```

### Translate specific files
```bash
python3 scripts/translate_to_korean.py ko/README.md ko/integrations/README.md
```

### Adjust API request delay (for rate limiting)
```bash
python3 scripts/translate_to_korean.py --delay 5.0
```

### Use custom base path
```bash
python3 scripts/translate_to_korean.py --base-path /custom/path
```

### Show help
```bash
python3 scripts/translate_to_korean.py --help
```

## Documentation Map

### Start Here
- **New to this tool?** → `QUICKSTART_TRANSLATION.md`
- **Want complete details?** → `TRANSLATION_GUIDE.md`

### Reference
- **Script options?** → `scripts/README.md`
- **Translation rules?** → `TRANSLATION_GUIDE.md` (Translation Rules section)
- **Troubleshooting?** → `TRANSLATION_GUIDE.md` (Troubleshooting section)

### File Locations
```
/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/
├── TRANSLATION_README.md (you are here)
├── QUICKSTART_TRANSLATION.md
├── TRANSLATION_GUIDE.md
├── scripts/
│   ├── README.md
│   ├── translate_to_korean.py (main script)
│   └── translate.sh (wrapper)
└── ko/
    └── (target files for translation)
```

## System Requirements

- **Python**: 3.7 or higher
- **Libraries**: `requests` (install: `pip install requests`)
- **API Key**: Anthropic API key from https://console.anthropic.com/
- **Internet**: Active connection to Anthropic API

## Performance

| Metric | Value |
|--------|-------|
| Time per file | 3-5 seconds |
| Total time for 17 files | 1-2 minutes |
| Cost | ~$0.05-0.15 USD |
| Model | Claude Opus 4.1 |
| Rate limit | 2 sec delay (adjustable) |

## Translation Quality Assurance

The toolkit enforces these translation rules:

### Translate to Korean
- Headings and paragraphs
- Lists and tables
- Link text
- YAML metadata (description field)
- Use formal, professional tone

### Keep in English
- Code blocks (entirely)
- Technical terms (Flowise, API, LLM, RAG, Agent, Flow, etc.)
- URLs and file paths
- Configuration keys and environment variables
- Command-line flags
- Programming language names

## Common Issues & Solutions

### "ANTHROPIC_API_KEY environment variable is not set"
```bash
export ANTHROPIC_API_KEY='your-key-here'
```

### "requests library not found"
```bash
pip install requests
```

### "API error 401 Unauthorized"
- Check your API key is valid
- Regenerate at https://console.anthropic.com/ if needed

### "API error 429 Too Many Requests"
```bash
# Use longer delay between requests
python3 scripts/translate_to_korean.py --delay 5.0
```

For more troubleshooting, see `TRANSLATION_GUIDE.md`

## Next Steps After Translation

1. **Verify**: Check a few translated files manually
2. **Commit**: 
   ```bash
   git add ko/
   git commit -m "Translate 17 Flowise docs to Korean"
   ```
3. **Push**: 
   ```bash
   git push origin main
   ```
4. **Deploy**: Update your documentation site

## Support & Resources

- **Anthropic Documentation**: https://docs.anthropic.com/
- **Anthropic Console**: https://console.anthropic.com/
- **Claude API Pricing**: https://www.anthropic.com/pricing

## Script Implementation Details

### Main Translation Flow
1. Reads markdown file content
2. Sends to Claude API with translation rules
3. Receives translated Korean content
4. Writes back to same file (overwrites English)
5. Reports success or failure

### Error Handling
- File not found: Skips with warning
- API errors: Reports error code and message
- Network timeouts: Retryable
- Invalid API key: Clear error message

### Rate Limiting Strategy
- 2-second delay between requests (default)
- Configurable via `--delay` option
- Helps avoid API rate limits

## Version Information

- **Script Version**: 1.0
- **Claude Model**: claude-opus-4-1-20250805
- **API Endpoint**: https://api.anthropic.com/v1/messages
- **Target Language**: Korean (ko)
- **Created**: 2025-06-16

## License

Same as Flowise project

## Questions?

1. Check the troubleshooting guide in `TRANSLATION_GUIDE.md`
2. Review script options in `scripts/README.md`
3. Verify prerequisites are installed
4. Ensure API key is valid at https://console.anthropic.com/

---

**Ready to translate?** Start with `QUICKSTART_TRANSLATION.md` or run:
```bash
python3 scripts/translate_to_korean.py
```
