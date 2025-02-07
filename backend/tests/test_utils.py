from unittest.mock import patch

from utils.utils import is_crawlable


@patch('utils.utils.RobotFileParser')
def test_is_crawlable(mock_parser):
    mock_instance = mock_parser.return_value
    mock_instance.can_fetch.return_value = True
    mock_instance.read.return_value = None

    result = is_crawlable('https://www.example.com/page')

    assert result is True
    mock_instance.set_url.assert_called_once_with('https://www.example.com/robots.txt')
    mock_instance.read.assert_called_once()
    mock_instance.can_fetch.assert_called_once_with('*', 'https://www.example.com/page')

@patch('utils.utils.RobotFileParser')
def test_is_crawlable_not_allowed(mock_parser):
    mock_instance = mock_parser.return_value
    mock_instance.can_fetch.return_value = False
    mock_instance.read.return_value = None

    result = is_crawlable('https://www.example.com/page')

    assert result is False
    mock_instance.set_url.assert_called_once_with('https://www.example.com/robots.txt')
    mock_instance.read.assert_called_once()
    mock_instance.can_fetch.assert_called_once_with('*', 'https://www.example.com/page')
