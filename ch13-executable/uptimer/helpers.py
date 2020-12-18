import click
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
        click.echo(f"ConnectionError: Can't reach {url} URL!")
        return None
    return response.status_code


def colorize_status(url, status):
    """Print the URL and status in color to the terminal

    :param url: URL to print
    :type url: str
    :param status: status used to determine the color of the output
    :type status: str
    """
    # fmt: off
    colors = {
        2: "green",
        3: "yellow",
        4: "bright_red",
        5: "red",
    }
    # fmt: on
    click.secho(f"{url} -> {status}", fg=colors.get(status // 100, "magenta"))
