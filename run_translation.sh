#!/bin/bash
set -e

# Try to get the API key from various sources
if [ -z "$ANTHROPIC_API_KEY" ]; then
    # Check if it's in ~/.bashrc or ~/.zshrc
    if [ -f ~/.zshrc ]; then
        source ~/.zshrc 2>/dev/null || true
    fi
    if [ -f ~/.bashrc ]; then
        source ~/.bashrc 2>/dev/null || true
    fi
fi

# Check again
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ERROR: ANTHROPIC_API_KEY not found in environment"
    echo "Please set: export ANTHROPIC_API_KEY=<your-key>"
    exit 1
fi

echo "Found API key, starting translation..."
python3 translate_batch_3.py
