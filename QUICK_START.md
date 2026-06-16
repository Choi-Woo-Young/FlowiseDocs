# Quick Start - Flowise Korean Translation

## 1-Minute Setup

```bash
# Step 1: Set your Anthropic API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Step 2: Run the translation script
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 translate_to_korean.py
```

That's it! The script will:
- Translate all 346 English markdown files to Korean
- Preserve code blocks, URLs, and technical terms
- Create files in the `ko/` directory
- Show progress and results

## API Key Setup

### Option A: Export in Terminal (Temporary)
```bash
export ANTHROPIC_API_KEY="your-api-key"
python3 translate_to_korean.py
```

### Option B: Inline (Single Command)
```bash
ANTHROPIC_API_KEY="your-api-key" python3 translate_to_korean.py
```

### Option C: Add to .bashrc/.zshrc (Permanent - Not Recommended for Production)
```bash
echo 'export ANTHROPIC_API_KEY="your-api-key"' >> ~/.zshrc
source ~/.zshrc
python3 translate_to_korean.py
```

## Get Your API Key

1. Go to https://console.anthropic.com
2. Sign in
3. Navigate to API Keys
4. Click "Create Key"
5. Copy and use above

## Monitor Progress

The script outputs:
```
[1/346] README.md ✓
[2/346] SUMMARY.md ✓
[3/346] api-reference/README.md ✓
...
```

## Expected Results

- **Time**: ~20-30 minutes for all 346 files
- **Cost**: ~$0.50-$1.00
- **Success**: Green checkmarks ✓ next to each file
- **Errors**: Red X marks ✗ (rare)

## Verify Translation

```bash
# Check Korean content exists
head ko/README.md

# Count Korean characters (should be > 0)
grep -o '[가-힣]' ko/README.md | wc -l

# Verify URLs preserved (should match English version)
grep "https://" ko/README.md | head -3
grep "https://" en/README.md | head -3
```

## What Gets Translated vs. Preserved

### Translated to Korean ✓
- All headings
- Body text
- Descriptions
- List items
- Table contents

### Stays in English ✓
- Code blocks
- API, LLM, RAG, Node, Agent, Tool, Flowise, JSON, etc.
- URLs and file paths
- Markdown formatting (# ## ** [] etc.)

## Common Issues

| Issue | Solution |
|-------|----------|
| `ANTHROPIC_API_KEY not set` | Set env var: `export ANTHROPIC_API_KEY="..."` |
| `Request failed 401` | Check API key is valid in Anthropic Console |
| `Timeout errors` | Network issue - can re-run to retry |
| `Some files failed` | Script reports them - can retry |

## Next Steps

1. ✓ Set API key
2. ✓ Run `python3 translate_to_korean.py`
3. ✓ Wait for completion
4. ✓ Verify a sample file
5. ✓ Commit and push to git

See `TRANSLATION_GUIDE.md` for detailed documentation.
