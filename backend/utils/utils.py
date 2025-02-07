from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser


def material_to_dict(material):
    """Converts a material object to a dictionary"""
    return {
        'id': material.id,
        'name': material.name,
        'unit': material.unit,
        'prices': [{
            'amount': price.amount,
            'vendor': price.vendor,
            'timestamp': price.timestamp.isoformat()
        } for price in sorted(material.prices, key=lambda p: p.timestamp, reverse=True)]
    }

def is_crawlable(url):
    """Checks if a URL is crawlable by checking the site's robots.txt"""
    if not url:
        return False

    try:
        parsed_url = urlparse(url)
        if not parsed_url.scheme or not parsed_url.netloc:
            return False

        robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"

        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()

        return rp.can_fetch('*', url)
    except Exception as e:
        print(f'Failed to check if {url} is crawlable: {e}')
        return False
