import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                 help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    if user_language == "es":
        print("\nstart chrome browser on es for test..")
    elif user_language == "fr":
        print("\nstart chrome browser on fr for test..")  
    else:
        raise pytest.UsageError("--language should be es or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()