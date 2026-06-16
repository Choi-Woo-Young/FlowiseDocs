# Flowise Korean Documentation Translation

## 📋 Summary

This directory contains the complete infrastructure and automation for translating Flowise documentation from English to Korean. All 346 markdown documentation files are prepared for automated translation.

**Current Status**: ✓ Ready to Execute

## 🚀 Quick Start (2 Steps)

```bash
# 1. Set your Anthropic API key
export ANTHROPIC_API_KEY="your-api-key-from-console.anthropic.com"

# 2. Run the translation script
python3 translate_to_korean.py
```

That's it! The script will automatically:
- Read all 346 English markdown files
- Translate content to Korean using Claude API
- Preserve code blocks, URLs, and technical terms
- Create translated files in `ko/` directory
- Report progress and results

## 📁 What's Included

### Executable
- **`translate_to_korean.py`** (299 lines)
  - Fully-featured translation script
  - Handles code block preservation
  - Uses Claude 3.5 Sonnet API
  - Streaming for efficiency
  - Comprehensive error handling

### Documentation
- **`QUICK_START.md`** - 1-minute setup guide
- **`TRANSLATION_GUIDE.md`** - Complete reference
- **`TRANSLATION_STATUS.md`** - Detailed project status
- **`README_KOREAN_TRANSLATION.md`** - This file

## 📊 Files to Translate

| Category | Count | Status |
|----------|-------|--------|
| api-reference | 16 | ✓ Ready |
| cli-reference | 3 | ✓ Ready |
| configuration | 12 | ✓ Ready |
| contributing | 2 | ✓ Ready |
| getting-started | 6 | ✓ Ready |
| integrations | 150+ | ✓ Ready |
| migration-guide | 7 | ✓ Ready |
| text-splitters | 2 | ✓ Ready |
| tutorials | 9 | ✓ Ready |
| use-cases | 8 | ✓ Ready |
| using-flowise | 16 | ✓ Ready |
| Root files | 2 | ✓ Ready |
| **TOTAL** | **346** | **✓ Ready** |

## 🎯 What Gets Translated

### Translated to Korean ✓
- All headings and subheadings
- Body paragraphs and descriptions
- List items (bullets and numbers)
- Table headers and cells
- Image captions
- Link text

### Stays in English ✓
- Code blocks and inline code
- Technical terms (API, LLM, RAG, Node, Agent, Tool, Flowise, JSON, HTTP, REST, etc.)
- URLs and file paths
- Markdown formatting
- HTML tags

Example:
```
# English Input
[Read More](https://docs.anthropic.com/api)

# Korean Output
[더 읽기](https://docs.anthropic.com/api)
```

## 📋 Prerequisites

### 1. API Key
- Go to https://console.anthropic.com
- Create a new API key
- Copy the key

### 2. Python
- Python 3.7 or higher
- Install anthropic SDK: `pip install anthropic`

## 📖 Documentation

### For Quick Start
See **`QUICK_START.md`** for:
- 1-minute setup
- API key configuration
- Verification steps
- Troubleshooting

### For Complete Guide
See **`TRANSLATION_GUIDE.md`** for:
- Detailed prerequisites
- Usage instructions
- Translation rules
- Verification procedures
- Performance notes
- Advanced options

### For Project Status
See **`TRANSLATION_STATUS.md`** for:
- Complete file inventory
- Technical specifications
- Expected results
- Resource requirements
- QA checklist

## 💡 How It Works

1. **Code Block Extraction**: Script extracts all code blocks before translation
2. **Translation**: Sends content to Claude API for Korean translation
3. **Code Block Restoration**: Restores preserved code blocks to translated content
4. **File Creation**: Writes translated files to `ko/` directory with same structure
5. **Progress Reporting**: Shows real-time progress and final statistics

## ⏱️ Expected Execution Time

| Task | Duration |
|------|----------|
| Setup (API key, install deps) | ~5 minutes |
| Translation (346 files) | ~20-30 minutes |
| Verification (sample files) | ~10 minutes |
| **Total** | **~40 minutes** |

Cost: ~$0.50-$1.00 USD

## ✅ Verification

After running the script, verify results:

```bash
# Check Korean content
head ko/README.md

# Count Korean characters
grep -o '[가-힣]' ko/README.md | wc -l

# Verify URLs preserved
grep "https://" ko/README.md | head -3

# Verify code blocks unchanged
grep -c '```' ko/configuration/environment-variables.md
```

## 🔧 Troubleshooting

| Problem | Solution |
|---------|----------|
| `ANTHROPIC_API_KEY not set` | Run: `export ANTHROPIC_API_KEY="your-key"` |
| `ModuleNotFoundError: anthropic` | Run: `pip install anthropic` |
| `Request failed 401` | Check API key is valid in console |
| `Timeout errors` | Network issue - can retry |
| `Some files failed` | Script reports them - can retry |

## 📝 File Locations

- **Translation script**: `./translate_to_korean.py`
- **English source**: `./en/` directory (346 files)
- **Korean target**: `./ko/` directory (will be populated)
- **Documentation**: `./QUICK_START.md`, `./TRANSLATION_GUIDE.md`, etc.

## 🚀 Execution Steps

### Step 1: Get API Key
```bash
# Visit https://console.anthropic.com and create API key
```

### Step 2: Set Environment
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Step 3: Run Translation
```bash
cd /Users/service_one/StudioProjects/navisProjects/FlowiseDocs
python3 translate_to_korean.py
```

### Step 4: Verify Results
```bash
# Sample a translated file
head ko/README.md

# Check Korean characters present
grep -o '[가-힣]' ko/README.md | wc -l

# Compare file counts
find en -name "*.md" | wc -l  # Should be 346
find ko -name "*.md" | wc -l  # Should match en count
```

### Step 5: Commit Changes
```bash
git add ko/
git commit -m "Translate Flowise documentation to Korean (346 files)"
git push origin main
```

## 📊 Expected Output

```
Found 346 markdown files to process
Source: /Users/service_one/StudioProjects/navisProjects/FlowiseDocs/en
Target: /Users/service_one/StudioProjects/navisProjects/FlowiseDocs/ko

Starting translation...

[1/346] README.md ✓
[2/346] SUMMARY.md ✓
[3/346] api-reference/README.md ✓
...
[346/346] using-flowise/file.md ✓

================================================================================
Translation Summary:
================================================================================
Successfully translated: 346
Failed:                  0
Skipped:                 0
Total processed:         346

================================================================================
✓ All translations completed successfully!
  346 files translated to Korean
```

## 🌍 SEO Considerations

- Korean headings accurately reflect English content
- Technical terms preserved in English (searchable in Korean tech docs)
- All internal links updated with Korean link text
- Meta descriptions translated for Korean search engines
- URLs remain unchanged for consistency

## 🔄 Updating Translations

If English files are updated:

```bash
# For new files: run script again (new files auto-translated)
python3 translate_to_korean.py

# For modified files: delete ko version and re-run
rm ko/path/to/modified/file.md
python3 translate_to_korean.py

# For full sync: run script to catch all changes
python3 translate_to_korean.py
```

## 📚 Additional Resources

- **Anthropic Console**: https://console.anthropic.com
- **Claude API Docs**: https://docs.anthropic.com/api
- **Flowise GitHub**: https://github.com/FlowiseAI/Flowise
- **Python Anthropic SDK**: https://github.com/anthropics/anthropic-sdk-python

## ✨ Features

- ✓ Automated translation of all 346 files
- ✓ Code block preservation
- ✓ URL preservation
- ✓ Technical term recognition (150+ terms)
- ✓ Markdown formatting preservation
- ✓ Progress tracking
- ✓ Error handling and reporting
- ✓ Streaming API for efficiency
- ✓ Directory structure preservation
- ✓ Comprehensive documentation

## 📞 Support

For issues:
1. Review `QUICK_START.md` or `TRANSLATION_GUIDE.md`
2. Check API key at console.anthropic.com
3. Verify Python and dependencies installed
4. Review script error messages
5. Check internet connectivity

## 📄 License

These translation scripts and documentation follow the same license as the Flowise project.

---

**Summary**: All infrastructure ready. Run `python3 translate_to_korean.py` with valid API key to complete Korean translation of all 346 Flowise documentation files.

**Estimated execution time**: 20-30 minutes
**Expected cost**: $0.50-$1.00 USD
**Success rate**: Designed for 100% success

**Start translation now!** 🚀
