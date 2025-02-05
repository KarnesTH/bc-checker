from services import crawler_service


def test_fetch_page():
    result = crawler_service.fetch_page('https://www.google.com')
    assert result is not None
    assert result.title is not None

def test_fetch_page_invalid_url():
    result = crawler_service.fetch_page('https://www.google.com/invalid')
    assert result is None
