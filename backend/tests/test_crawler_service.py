from unittest.mock import MagicMock, patch

from services import crawler_service


@patch('services.crawler_service.sync_playwright')
@patch('services.crawler_service.is_crawlable', return_value=True)
def test_fetch_page(mock_crawlable, mock_playwright):
    mock_browser = MagicMock()
    mock_page = MagicMock()

    mock_instance = MagicMock()
    mock_playwright.return_value = mock_instance
    mock_instance.__enter__.return_value.chromium.launch.return_value = mock_browser
    mock_browser.new_page.return_value = mock_page
    mock_page.content.return_value = '<html><title>Test Page</title></html>'

    result = crawler_service.fetch_page('https://www.example.com/page')

    assert result is not None
    assert result.title is not None
    assert result.title.string == 'Test Page'

@patch('services.crawler_service.sync_playwright')
@patch('services.crawler_service.is_crawlable', return_value=False)
def test_fetch_page_not_crawlable(mock_crawlable, mock_playwright):
    result = crawler_service.fetch_page('https://www.example.com/page')
    assert result is None
    mock_playwright.assert_not_called()

@patch('services.crawler_service.sync_playwright')
@patch('services.crawler_service.is_crawlable', return_value=True)
def test_fetch_page_error(mock_crawlable, mock_playwright):
    mock_instance = MagicMock()
    mock_playwright.return_value = mock_instance
    mock_instance.__enter__.side_effect = Exception("Test error")

    result = crawler_service.fetch_page('https://www.example.com/page')
    assert result is None
