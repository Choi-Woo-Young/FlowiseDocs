# Flowise Korean Translation Toolkit - START HERE

Welcome! This toolkit helps you translate 17 Flowise documentation files from English to Korean using the Anthropic Claude API.

## Choose Your Path

### Option 1: I Just Want To Get Started (5 minutes)
Read: **QUICKSTART_TRANSLATION.md**
- 3-step setup guide
- Get API key → Set environment → Run script
- Perfect for users who want to dive in immediately

### Option 2: I Want To Understand Everything (15 minutes)
Read: **TRANSLATION_GUIDE.md**
- Complete setup instructions
- How the script works
- Translation rules and examples
- Verification and troubleshooting
- Perfect for users who want comprehensive knowledge

### Option 3: I Want To Know What's Included (5 minutes)
Read: **TRANSLATION_README.md**
- Toolkit overview
- Components and features
- File structure and locations
- Perfect for understanding what you're getting

### Option 4: I Need Script Reference (3 minutes)
Read: **scripts/README.md**
- Script options and configuration
- Default files list
- Command examples
- Perfect for script users

## The 3-Minute Version

1. Get API key from https://console.anthropic.com/
2. Run: `export ANTHROPIC_API_KEY='your-key'`
3. Run: `python3 scripts/translate_to_korean.py`

Done! The script will translate 17 files to Korean in 1-2 minutes.

## What Gets Translated?

✓ **TO KOREAN**: Headings, paragraphs, lists, tables, link text
✗ **STAYS ENGLISH**: Code blocks, technical terms (API, LLM, RAG, etc.), URLs

## Files to Translate

17 markdown files across:
- Integrations (4 files)
- Text Splitters (1 file)
- Migration Guides (3 files)
- Use Cases (7 files)
- Using Flowise (2 files)

All files are in the `ko/` directory and verified to exist.

## Quick Troubleshooting

**"ANTHROPIC_API_KEY not set"**
→ Run: `export ANTHROPIC_API_KEY='your-key'`

**"requests library not found"**
→ Run: `pip install requests`

**"API error 401"**
→ Check your API key at https://console.anthropic.com/

**Need more help?**
→ See TRANSLATION_GUIDE.md "Troubleshooting" section

## File Locations

```
FlowiseDocs/
├── START_HERE.md (← you are here)
├── QUICKSTART_TRANSLATION.md (3-step guide)
├── TRANSLATION_GUIDE.md (complete reference)
├── TRANSLATION_README.md (toolkit overview)
├── scripts/
│   ├── translate_to_korean.py (main script)
│   ├── translate.sh (wrapper)
│   └── README.md (script reference)
└── ko/
    └── (17 files to translate)
```

## Next Step

Pick your path above and get started! Most users start with **QUICKSTART_TRANSLATION.md**.

---

**Questions?** Check the relevant documentation or see TRANSLATION_GUIDE.md.
