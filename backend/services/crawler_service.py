from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright
from utils.utils import is_crawlable


def fetch_page(url):
    """Fetches a page and returns a BeautifulSoup object"""
    if not is_crawlable(url):
        print(f"URL {url} is not crawlable")
        return None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url)
            page.wait_for_load_state('networkidle')
            html = page.content()
            browser.close()
            return BeautifulSoup(html, 'html.parser')
    except Exception as e:
        print(f"Failed to fetch page {url}: {e}")
        return None

def extract_material_data(soup):
    """
    Extracts all relevant material information from a page
    Returns a dictionary with material data
    """
    return {
        'name': extract_name(soup),
        'price': extract_price(soup),
        'unit': extract_unit(soup),
        'vendor': extract_vendor(soup),
        'url': extract_url(soup)
    }

def extract_name(soup):
    """Extract material name from a page"""
    pass

def extract_price(soup):
    """Extract material price from a page"""
    pass

def extract_unit(soup):
    "Extract material unit (kg, m³, etc) from a page"
    pass

def extract_vendor(soup):
    """Extract material vendor from a page"""
    pass

def extract_url(soup):
    """Extract material URL from a page"""
    pass
