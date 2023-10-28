import click
import requests

from typing import (Optional)
from bs4 import BeautifulSoup


@click.command()
@click.argument('url', type=str)
@click.argument('file', type=click.Path(writable=True), required=True)
def scrape(url: str, file: Optional[str] = None) -> None:
    """
    Scrapes text content from the specified URL and optionally saves it to file.

    [URL] The full URL from which content should be scraped.

    [FILE] The file where the scraped content should be saved.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we got a successful response

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract and join text from the parsed HTML content
        text = " ".join(soup.stripped_strings)

        # Save the extracted text if a file path is provided
        if file:
            with open(file, 'w') as outfile:
                outfile.write(text)
    except requests.RequestException as e:
        raise click.ClickException(f"Error extracting content from {url}: {e}")
