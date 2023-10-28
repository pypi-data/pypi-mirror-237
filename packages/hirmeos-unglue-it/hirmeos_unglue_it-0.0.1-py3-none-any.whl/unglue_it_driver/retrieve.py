import requests

from logging import getLogger
from typing import Dict, Iterator, List

from .serializers import UnglueReportItem

logger = getLogger(__name__)


def get_path(url: str) -> Dict:
    """Retireve results based on the path

    Args:
        url (str): Url for the request

    Returns:
        dict: results from the get request
    """
    response = requests.get(url)
    if response.status_code != 200:
        response.raise_for_status()
    return response.json()


def get_api_url(path: str, key: str, user: str) -> str:
    """Create the url to be used in the get request defined in 'get_path'"""
    return f"https://unglue.it/{path}?format=json&api_key={key}&username={user}"


def find_isbn_result(identifiers_list: List) -> Dict:
    """There are 3 different types of identifiers, get the ISBN only.

    Args:
        identifiers_list (List): Dict with multiple identifers.

    Returns:
        Dict: isbn dict.
    """
    for ident in identifiers_list:
        if ident.get("type") == "isbn":
            return ident


def get_results(ebook_path: str, api_key: str, user: str) -> Dict:
    """Helper method for the fetch_results method.

    Args:
        ebook_path (str): path for the api referencing the book
        api_key (str): needed to access the api.
        user (str): email from the user.

    Returns:
        Dict: Results isbn + downloads
    """
    book_results = get_path(get_api_url(ebook_path, api_key, user))
    if identifiers := get_path(get_api_url(book_results["edition"], api_key, user)):
        if result := find_isbn_result(identifiers.get("identifiers")):
            book_results["isbn"] = result
            return book_results


def fetch_results(
    api_key: str, publisher: int, user: str
) -> Iterator[UnglueReportItem]:
    """Entry point to return the results from the Unglue-It API.
    Retrieve the books paths first, loop over them and get the
    results, finally the identifiers.

    Args:
        key (str): Api key
        publisher (int): Publisher number
        user (str): username used
    Returns:
        Iterator: Result from the Serializers
    """
    publisher_path = f"/api/v1/publisher/{publisher}"
    publisher_and_path = get_path(get_api_url(publisher_path, api_key, user))
    for ebook_path in publisher_and_path["ebooks"]:
        if book_results := get_results(ebook_path, api_key, user):
            yield UnglueReportItem(**book_results)
