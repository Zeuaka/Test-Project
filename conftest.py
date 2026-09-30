import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose language for browser: en, es, fr, etc."
    )


@pytest.fixture(scope="function")
def browser(request):
    # Считываем параметр --language из командной строки
    language = request.config.getoption("--language")

    # Настраиваем Chrome с нужным языком
    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": language}
    )

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
