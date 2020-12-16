from time import sleep

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


@click.command()
@click.argument("urls", nargs=-1)
@click.option("--daemon", "-d", default=False, is_flag=True)
def check(urls, daemon):
    """Check urls and print their HTTP statuses (with colors)

    :param urls: URL (or a tuple with multiple URLs) to check
    :type urls: str or tuple(str)
    :param daemon: If set to True, after checking all URLs,
                   sleep for 5 seconds and check them again
    :type daemon: bool
    """

    while True:
        for url in urls:
            status_code = check_url(url)
            if status_code:
                colorize_status(url, status_code)
        if not daemon:
            break
        sleep(5)


if __name__ == "__main__":
    check()
