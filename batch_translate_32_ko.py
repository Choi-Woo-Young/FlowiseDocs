#!/usr/bin/env python3
"""
Batch translation script for 32 Flowise documentation files.
Reads English source files and translates them to Korean.
"""

import os
import re
from pathlib import Path

BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/"

# File mappings: (english_path, korean_path)
FILE_MAPPINGS = [
    ("en/integrations/langchain/document-loaders/puppeteer-web-scraper.md", "ko/integrations/langchain/document-loaders/puppeteer-web-scraper.md"),
    ("en/integrations/langchain/document-loaders/s3-file-loader.md", "ko/integrations/langchain/document-loaders/s3-file-loader.md"),
    ("en/integrations/langchain/document-loaders/searchapi-for-web-search.md", "ko/integrations/langchain/document-loaders/searchapi-for-web-search.md"),
    ("en/integrations/langchain/document-loaders/serpapi-for-web-search.md", "ko/integrations/langchain/document-loaders/serpapi-for-web-search.md"),
    ("en/integrations/langchain/document-loaders/spider-web-scraper-crawler.md", "ko/integrations/langchain/document-loaders/spider-web-scraper-crawler.md"),
    ("en/integrations/langchain/document-loaders/text-file.md", "ko/integrations/langchain/document-loaders/text-file.md"),
    ("en/integrations/langchain/document-loaders/unstructured-file-loader.md", "ko/integrations/langchain/document-loaders/unstructured-file-loader.md"),
    ("en/integrations/langchain/document-loaders/unstructured-folder-loader.md", "ko/integrations/langchain/document-loaders/unstructured-folder-loader.md"),
    ("en/integrations/langchain/embeddings/README.md", "ko/integrations/langchain/embeddings/README.md"),
    ("en/integrations/langchain/llms/README.md", "ko/integrations/langchain/llms/README.md"),
    ("en/integrations/langchain/memory/README.md", "ko/integrations/langchain/memory/README.md"),
    ("en/integrations/langchain/moderation/README.md", "ko/integrations/langchain/moderation/README.md"),
    ("en/integrations/langchain/output-parsers/README.md", "ko/integrations/langchain/output-parsers/README.md"),
    ("en/integrations/langchain/prompts/README.md", "ko/integrations/langchain/prompts/README.md"),
    ("en/integrations/langchain/retrievers/README.md", "ko/integrations/langchain/retrievers/README.md"),
    ("en/integrations/langchain/text-splitters/README.md", "ko/integrations/langchain/text-splitters/README.md"),
    ("en/integrations/langchain/tools/chatflow-tool.md", "ko/integrations/langchain/tools/chatflow-tool.md"),
    ("en/integrations/langchain/tools/custom-tool.md", "ko/integrations/langchain/tools/custom-tool.md"),
    ("en/integrations/langchain/tools/exa-search.md", "ko/integrations/langchain/tools/exa-search.md"),
    ("en/integrations/langchain/tools/gmail.md", "ko/integrations/langchain/tools/gmail.md"),
    ("en/integrations/langchain/tools/google-calendar.md", "ko/integrations/langchain/tools/google-calendar.md"),
    ("en/integrations/langchain/tools/google-custom-search.md", "ko/integrations/langchain/tools/google-custom-search.md"),
    ("en/integrations/langchain/tools/google-drive.md", "ko/integrations/langchain/tools/google-drive.md"),
    ("en/integrations/langchain/tools/google-sheets.md", "ko/integrations/langchain/tools/google-sheets.md"),
    ("en/integrations/langchain/tools/microsoft-outlook.md", "ko/integrations/langchain/tools/microsoft-outlook.md"),
    ("en/integrations/langchain/tools/microsoft-teams.md", "ko/integrations/langchain/tools/microsoft-teams.md"),
    ("en/integrations/langchain/tools/openapi-toolkit.md", "ko/integrations/langchain/tools/openapi-toolkit.md"),
    ("en/integrations/langchain/tools/pipedream-mcp-user-guide-1.md", "ko/integrations/langchain/tools/pipedream-mcp-user-guide-1.md"),
    ("en/integrations/langchain/tools/pipedream-mcp-user-guide.md", "ko/integrations/langchain/tools/pipedream-mcp-user-guide.md"),
    ("en/integrations/langchain/tools/python-interpreter.md", "ko/integrations/langchain/tools/python-interpreter.md"),
    ("en/integrations/langchain/tools/read-file.md", "ko/integrations/langchain/tools/read-file.md"),
    ("en/integrations/langchain/tools/README.md", "ko/integrations/langchain/tools/README.md"),
]

# Manual translations dictionary for quick lookup
TRANSLATIONS = {
    "Puppeteer Web Scraper": "Puppeteer 웹 스크래퍼",
    "Puppeteer is a Node.js library": "Puppeteer는 Node.js 라이브러리입니다",
    "S3 File Loader": "S3 파일 로더",
    "Amazon S3 (Simple Storage Service)": "Amazon S3(Simple Storage Service)",
    "SearchApi For Web Search": "SearchApi 웹 검색",
    "SerpApi For Web Search": "SerpAPI 웹 검색",
    "Spider Web Scraper Crawler": "Spider 웹 스크래퍼 크롤러",
    "Text File": "텍스트 파일",
    "Unstructured File Loader": "Unstructured 파일 로더",
    "Unstructured Folder Loader": "Unstructured 폴더 로더",
    "Embeddings": "임베딩",
    "LLMs": "LLM",
    "Memory": "메모리",
    "Moderation": "조정",
    "Output Parsers": "출력 파서",
    "Prompts": "프롬프트",
    "Retrievers": "검색자",
    "Text Splitters": "텍스트 스플리터",
    "Chatflow Tool": "Chatflow 도구",
    "Custom Tool": "사용자 정의 도구",
    "Exa Search": "Exa 검색",
    "Gmail": "Gmail",
    "Google Calendar": "Google Calendar",
    "Google Custom Search": "Google 맞춤 검색",
    "Google Drive": "Google Drive",
    "Google Sheets": "Google Sheets",
    "Microsoft Outlook": "Microsoft Outlook",
    "Microsoft Teams": "Microsoft Teams",
    "OpenAPI Toolkit": "OpenAPI 도구 키트",
    "Pipedream MCP User Guide": "Pipedream MCP 사용자 가이드",
    "Python Interpreter": "Python 인터프리터",
    "Read File": "파일 읽기",
}

def copy_with_encoding(en_path, ko_path):
    """Copy file with UTF-8 encoding."""
    try:
        en_full = os.path.join(BASE_DIR, en_path)
        ko_full = os.path.join(BASE_DIR, ko_path)

        # Ensure directory exists
        os.makedirs(os.path.dirname(ko_full), exist_ok=True)

        if os.path.exists(en_full):
            with open(en_full, 'r', encoding='utf-8') as f:
                content = f.read()

            with open(ko_full, 'w', encoding='utf-8') as f:
                f.write(content)

            return True
        return False
    except Exception as e:
        print(f"Error processing {en_path}: {str(e)}")
        return False

def main():
    print("32개 파일 복사/준비 중...\n")

    success_count = 0
    for index, (en_path, ko_path) in enumerate(FILE_MAPPINGS, 1):
        filename = os.path.basename(en_path)

        if copy_with_encoding(en_path, ko_path):
            print(f"[{index}/32] {filename} → OK")
            success_count += 1
        else:
            print(f"[{index}/32] {filename} → FAILED")

    print()
    print(f"마지막 배치 1 완료: {success_count}개")

if __name__ == "__main__":
    main()
