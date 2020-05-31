import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(user_language):
    user_language.addoption('--language', action='store', default=es, 
                    help="Choose --language:ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru ,sk, uk, zh-cn")


@pytest.fixture(scope="function")
def language(request):
    language = request.config.getoption("--language")
    
def browser(language):  
    print("\nstart browser for test..")
    user_language=language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
    
