from unittest.mock import patch

import requests
from services import crawler_service


@patch('utils.utils.RobotFileParser')
@patch('requests.get')
def test_fetch_page(mock_get, mock_robot_parser):
    robot_instance = mock_robot_parser.return_value
    robot_instance.can_fetch.return_value = True
    robot_instance.read.return_value = None

    mock_response = mock_get.return_value
    mock_response.text = '<html><title>Test Page</title></html>'
    mock_response.raise_for_status.return_value = None

    result = crawler_service.fetch_page('https://www.example.com/page')

    assert result is not None
    assert result.title is not None
    assert result.title.string == 'Test Page'

    mock_get.assert_called_once()
    robot_instance.can_fetch.assert_called_once()

@patch('utils.utils.RobotFileParser')
@patch('requests.get')
def test_fetch_page_not_crawlable(mock_get, mock_robot_parser):
    robot_instance = mock_robot_parser.return_value
    robot_instance.can_fetch.return_value = False
    robot_instance.read.return_value = None

    result = crawler_service.fetch_page('https://www.example.com/page')

    assert result is None
    mock_get.assert_not_called()

@patch('utils.utils.RobotFileParser')
@patch('requests.get')
def test_fetch_page_request_error(mock_get, mock_robot_parser):
    robot_instance = mock_robot_parser.return_value
    robot_instance.can_fetch.return_value = True
    robot_instance.read.return_value = None

    mock_get.side_effect = requests.RequestException("Test error")

    result = crawler_service.fetch_page('https://www.example.com/page')

    assert result is None
