import pytest


@pytest.mark.asyncio
async def test_perform_single_site_scraping():
    from unittest.mock import AsyncMock
    from asyncp.scraper.scraper import perform_single_site_scraping

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

    result = await perform_single_site_scraping(mock_client_session, mock_url)

    assert result.url == mock_url
    assert result.success is True
    assert len(result.links) == 2
    assert sorted(result.links) == sorted(["http://example.com", "http://test.com"])
    assert result.links[0] == "http://example.com"
