import requests


def check_url(url):
    """Send HEAD request to the url and return the HTTP status code

    :param url: URL to check
    :type url: str
    :return: HTTP status code
    :rtype: int
    """
    try:
        response = requests.head(url)
    except requests.exceptions.ConnectionError:
        return None
    return response.status_code
