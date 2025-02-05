from typing import Optional

import requests
from bs4 import BeautifulSoup


def fetch_page(url: str) -> Optional[BeautifulSoup]:
    """Fetches a page and returns a BeautifulSoup object"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Failed to fetch page {url}: {e}")
        return None
