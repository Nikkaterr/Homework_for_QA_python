import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url-dog",
        default="https://dog.ceo/api",
        help="This is dog_api url"
    )

    parser.addoption(
        "--url-brewer",
        default="https://api.openbrewerydb.org/breweries",
        help="This is brewer_api url"
    )

    parser.addoption(
        "--url-jsonplacholder",
        default="https://jsonplaceholder.typicode.com/posts",
        help="This is jsonholder_api url"
    )

    parser.addoption(
        "--url-test",
        default="https://ya.ru",
        help="This is default url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        type=int,
        help="status code check"
    )


@pytest.fixture
def dog_url(request):
    return request.config.getoption("--url-dog")


@pytest.fixture
def brewer_url(request):
    return request.config.getoption("--url-brewer")


@pytest.fixture
def jsonholder_url(request):
    return request.config.getoption("--url-jsonplacholder")


@pytest.fixture
def check_url(request):
    return request.config.getoption("--url-test")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")
