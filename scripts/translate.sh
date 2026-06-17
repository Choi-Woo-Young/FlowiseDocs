#!/bin/bash
#
# Wrapper script for translating Flowise documentation to Korean
# Usage: ./translate.sh [files...]
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed"
    exit 1
fi

# Check if requests library is available
if ! python3 -c "import requests" 2>/dev/null; then
    echo "Error: requests library not found"
    echo "Install with: pip install requests"
    exit 1
fi

# Check for API key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable is not set"
    echo ""
    echo "Set your API key:"
    echo "  export ANTHROPIC_API_KEY='your-api-key-here'"
    exit 1
fi

# Run the translation script from the project directory
cd "$PROJECT_DIR"
python3 "$SCRIPT_DIR/translate_to_korean.py" "$@"
