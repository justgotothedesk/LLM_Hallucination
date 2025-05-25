""" 출처 검증 """

import re
import requests

class SourceChecker:
    def extract_sources(self, text):
        urls = re.findall(r'(https?://[^\s]+)', text)
        return urls

    def evaluate_source(self, url):
        if ".gov" in url or ".edu" in url:
            return 1.0
        elif "wikipedia" in url or ".org" in url:
            return 0.8
        elif "blog" in url or "medium" in url:
            return 0.4
        else:
            return 0.5