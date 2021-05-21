import click
import pytest
import requests
import sys
from click.testing import CliRunner
from uptimer import __version__
from uptimer.uptimer import check, check_url, colorize_status


def test_version():
    assert __version__ == "0.1.0"


def mock_response_object(code):
    resp = requests.Response()
    resp.status_code = code
    return resp


def test_check_url(mocker):
    mocker.patch("requests.head", return_value=mock_response_object(200))
    assert check_url("dummyurl") == 200

    mocker.patch("requests.head", return_value=mock_response_object(404))
    assert check_url("dummyurl") == 404

    with pytest.raises(TypeError):
        check_url()


def test_colorize_status(mocker):
    mocker.patch("click.secho")
    # colorize_status("dummyurl", 200)
    # click.secho.assert_called()
    # Or to check if we called it with correct parameters:
    url = "dummyurl"
    status = 200
    colorize_status(url, status)
    click.secho.assert_called_with(f"{url} -> {status}", fg="green")


@pytest.mark.skipif(
    sys.platform == "win32", reason="Testing colorized output doesn't work on Windows"
)
@pytest.mark.parametrize(
    "code,color",
    [
        (200, "green"),
        (304, "yellow"),
        (404, "bright_red"),
        (500, "red"),
        (1, "magenta"),
    ],
)
def test_check_one_url(mocker, code, color):
    mocker.patch("requests.head", return_value=mock_response_object(code))

    runner = CliRunner()
    result = runner.invoke(check, ["dummyurl"], color=True)

    expected_message = click.style(f"dummyurl -> {code}", fg=color)
    assert result.output == f"{expected_message}\n"


@pytest.mark.skipif(
    sys.platform == "win32", reason="Testing colorized output doesn't work on Windows"
)
def test_check_multiple_urls(mocker):
    mocker.patch(
        "requests.head",
        side_effect=[mock_response_object(200), mock_response_object(500)],
    )

    runner = CliRunner()
    result = runner.invoke(check, ["dummyurl1", "dummyurl2"], color=True)

    expected_message1 = click.style("dummyurl1 -> 200", fg="green")
    expected_message2 = click.style("dummyurl2 -> 500", fg="red")
    assert result.output == f"{expected_message1}\n{expected_message2}\n"
