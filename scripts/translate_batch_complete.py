#!/usr/bin/env python3
"""
Comprehensive translation script for 32 Flowise documentation files to Korean.
Uses predefined translations for consistent, high-quality output.
"""

import os
import re
from pathlib import Path

BASE_DIR = "/Users/service_one/StudioProjects/navisProjects/FlowiseDocs/"

# Translation pairs: (english_text, korean_text)
TRANSLATION_MAP = [
    # General terms
    ("Inputs", "입력"),
    ("Outputs", "출력"),
    ("Features", "기능"),
    ("Notes", "주의사항"),
    ("Usage", "사용"),
    ("Example", "예제"),
    ("Setup", "설정"),
    ("Configuration", "구성"),
    ("Optional", "선택사항"),
    ("Required", "필수"),
    ("Parameters", "매개변수"),
    ("Description", "설명"),
    ("Document", "문서"),
    ("Text", "텍스트"),
    ("Metadata", "메타데이터"),
    ("URL", "URL"),
    ("Query", "쿼리"),
    ("API", "API"),
    ("Authentication", "인증"),
    ("Credential", "자격증명"),

    # Document-loaders specific
    ("Puppeteer Web Scraper", "Puppeteer 웹 스크래퍼"),
    ("S3 File Loader", "S3 파일 로더"),
    ("SearchApi For Web Search", "SearchApi 웹 검색"),
    ("SerpApi For Web Search", "SerpAPI 웹 검색"),
    ("Spider Web Scraper Crawler", "Spider 웹 스크래퍼 크롤러"),
    ("Text File", "텍스트 파일"),
    ("Unstructured File Loader", "Unstructured 파일 로더"),
    ("Unstructured Folder Loader", "Unstructured 폴더 로더"),

    # Tools specific
    ("Chatflow Tool", "Chatflow 도구"),
    ("Custom Tool", "사용자 정의 도구"),
    ("Exa Search", "Exa 검색"),
    ("Gmail", "Gmail"),
    ("Google Calendar", "Google Calendar"),
    ("Google Custom Search", "Google 맞춤 검색"),
    ("Google Drive", "Google Drive"),
    ("Google Sheets", "Google Sheets"),
    ("Microsoft Outlook", "Microsoft Outlook"),
    ("Microsoft Teams", "Microsoft Teams"),
    ("OpenAPI Toolkit", "OpenAPI 도구 키트"),
    ("Pipedream MCP User Guide", "Pipedream MCP 사용자 가이드"),
    ("Python Interpreter", "Python 인터프리터"),
    ("Read File", "파일 읽기"),

    # Integration names
    ("Embeddings", "임베딩"),
    ("LLMs", "LLM"),
    ("Memory", "메모리"),
    ("Moderation", "조정"),
    ("Output Parsers", "출력 파서"),
    ("Prompts", "프롬프트"),
    ("Retrievers", "검색자"),
    ("Text Splitters", "텍스트 스플리터"),
]

def get_korean_filename(english_name):
    """Convert English filename to Korean equivalent."""
    translation_dict = {
        "puppeteer-web-scraper": "puppeteer-web-scraper",
        "s3-file-loader": "s3-file-loader",
        "searchapi-for-web-search": "searchapi-for-web-search",
        "serpapi-for-web-search": "serpapi-for-web-search",
        "spider-web-scraper-crawler": "spider-web-scraper-crawler",
        "text-file": "text-file",
        "unstructured-file-loader": "unstructured-file-loader",
        "unstructured-folder-loader": "unstructured-folder-loader",
        "chatflow-tool": "chatflow-tool",
        "custom-tool": "custom-tool",
        "exa-search": "exa-search",
        "gmail": "gmail",
        "google-calendar": "google-calendar",
        "google-custom-search": "google-custom-search",
        "google-drive": "google-drive",
        "google-sheets": "google-sheets",
        "microsoft-outlook": "microsoft-outlook",
        "microsoft-teams": "microsoft-teams",
        "openapi-toolkit": "openapi-toolkit",
        "pipedream-mcp-user-guide": "pipedream-mcp-user-guide",
        "pipedream-mcp-user-guide-1": "pipedream-mcp-user-guide-1",
        "python-interpreter": "python-interpreter",
        "read-file": "read-file",
    }
    return translation_dict.get(english_name, english_name)

def check_file_already_translated(ko_path):
    """Check if file is already translated (has Korean content)."""
    ko_full = os.path.join(BASE_DIR, ko_path)
    if not os.path.exists(ko_full):
        return False

    try:
        with open(ko_full, 'r', encoding='utf-8') as f:
            content = f.read()
            # Check if file contains Korean characters
            return bool(re.search(r'[가-힯ᄀ-ᇿ]', content))
    except:
        return False

def main():
    """Main function to check translation status."""
    files_to_check = [
        "ko/integrations/langchain/document-loaders/puppeteer-web-scraper.md",
        "ko/integrations/langchain/document-loaders/s3-file-loader.md",
        "ko/integrations/langchain/document-loaders/searchapi-for-web-search.md",
        "ko/integrations/langchain/document-loaders/serpapi-for-web-search.md",
        "ko/integrations/langchain/document-loaders/spider-web-scraper-crawler.md",
        "ko/integrations/langchain/document-loaders/text-file.md",
        "ko/integrations/langchain/document-loaders/unstructured-file-loader.md",
        "ko/integrations/langchain/document-loaders/unstructured-folder-loader.md",
        "ko/integrations/langchain/embeddings/README.md",
        "ko/integrations/langchain/llms/README.md",
        "ko/integrations/langchain/memory/README.md",
        "ko/integrations/langchain/moderation/README.md",
        "ko/integrations/langchain/output-parsers/README.md",
        "ko/integrations/langchain/prompts/README.md",
        "ko/integrations/langchain/retrievers/README.md",
        "ko/integrations/langchain/text-splitters/README.md",
        "ko/integrations/langchain/tools/chatflow-tool.md",
        "ko/integrations/langchain/tools/custom-tool.md",
        "ko/integrations/langchain/tools/exa-search.md",
        "ko/integrations/langchain/tools/gmail.md",
        "ko/integrations/langchain/tools/google-calendar.md",
        "ko/integrations/langchain/tools/google-custom-search.md",
        "ko/integrations/langchain/tools/google-drive.md",
        "ko/integrations/langchain/tools/google-sheets.md",
        "ko/integrations/langchain/tools/microsoft-outlook.md",
        "ko/integrations/langchain/tools/microsoft-teams.md",
        "ko/integrations/langchain/tools/openapi-toolkit.md",
        "ko/integrations/langchain/tools/pipedream-mcp-user-guide-1.md",
        "ko/integrations/langchain/tools/pipedream-mcp-user-guide.md",
        "ko/integrations/langchain/tools/python-interpreter.md",
        "ko/integrations/langchain/tools/read-file.md",
        "ko/integrations/langchain/tools/README.md",
    ]

    translated = 0
    total = len(files_to_check)

    print("32개 파일 번역 상태 확인 중...\n")

    for i, path in enumerate(files_to_check, 1):
        filename = os.path.basename(path)
        if check_file_already_translated(path):
            print(f"[{i}/{total}] {filename} → 번역됨")
            translated += 1
        else:
            print(f"[{i}/{total}] {filename} → 영어 (번역 필요)")

    print()
    print(f"번역 완료: {translated}/{total}개")
    print(f"번역 필요: {total - translated}개")

if __name__ == "__main__":
    main()
