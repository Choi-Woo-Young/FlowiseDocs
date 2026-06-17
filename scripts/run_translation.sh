#!/bin/bash

# Check if ANTHROPIC_API_KEY is set
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable not set"
    echo ""
    echo "Please set your API key first:"
    echo "  export ANTHROPIC_API_KEY='your-api-key-here'"
    echo ""
    echo "Then run this script again:"
    echo "  bash run_translation.sh"
    exit 1
fi

# Run the translation script
python3 translate_to_korean.py
