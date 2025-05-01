from unittest.mock import AsyncMock
import pytest
from asyncp.scraper.downloader import download_url, look_for_links


@pytest.mark.asyncio
async def test_download_url():
    mock_client_session = AsyncMock()
    mock_url = "http://example.com"

    example_response = """
    <html>
        <head><title>Test Page</title></head>   
        <body>
            <a href="http://example.com">Example</a>
            <a href="http://test.com">Test</a>
        </body>
    </html>
    """
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.text.return_value = example_response

    mock_client_session.get.return_value = mock_response

    result = await download_url(mock_client_session, mock_url)

    assert result.url == mock_url
    assert result.success is True
    assert result.content is not None
    assert len(result.issues) == 0
    assert result.content == example_response


def test_look_for_links():
    mock_content = """
    <html>
        <head><title>Test Page</title></head>   
        <body>
            <a href="http://example.com">Example</a>
            <a href="http://test.com">Test</a>
        </body>
    </html>
    """

    result = look_for_links(mock_content)

    assert sorted(result) == sorted(["http://example.com", "http://test.com"])
