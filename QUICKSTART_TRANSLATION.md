# Quick Start: Korean Translation

Translate 17 Flowise documentation files to Korean in 3 simple steps.

## Step 1: Get Your API Key

1. Visit https://console.anthropic.com/
2. Sign in or create an account
3. Create a new API key in the API Keys section
4. Copy the key

## Step 2: Set Environment Variable

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

To verify it's set:
```bash
echo $ANTHROPIC_API_KEY
```

## Step 3: Run the Translation

```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 scripts/translate_to_korean.py
```

That's it! The script will:
- Translate all 17 default files to Korean
- Preserve code blocks unchanged
- Keep technical terms in English (API, LLM, RAG, etc.)
- Show progress and completion status
- Report "최종 배치 완료: 17개 파일 번역 완료" when done

## Expected Time

Total time: **1-2 minutes** for 17 files

## Troubleshooting

**"ANTHROPIC_API_KEY environment variable is not set"**
→ Run: `export ANTHROPIC_API_KEY='your-key'`

**"requests library not found"**
→ Run: `pip install requests`

**"API error 401 Unauthorized"**
→ Check your API key is valid at https://console.anthropic.com/

For detailed help, see `TRANSLATION_GUIDE.md`
