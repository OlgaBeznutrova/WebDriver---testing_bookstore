import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en-gb",
                     help="Input the language in ISO 639-1 code format")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    if language in ["ar", "ca", "cs", "da", "de", "en-gb", "el", "es", "fi", "fr", "it", "ko", "nl", "pl", "pt",
                    "pt-br", "ro", "ru", "sk", "uk", "zh-hans"]:
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError(
            "Add --language with ISO 639-1 code format\nالعربيّة: ar\ncatalà: ca\nčesky: cs\ndansk: da\nDeutsch: de\n"
            "British English: en-gb\nΕλληνικά: el\nespañol: es\nsuomi: fi\nfrançais: fr\nitaliano: it\n"
            "한국어: ko\nNederlands: nl\npolski: pl\nPortuguês: pt\nPortuguês Brasileiro: pt-br\nRomână: ro\n"
            "Русский: ru\nSlovensky: sk\nУкраїнська: uk\n简体中文: zh-hans"
        )
    yield browser
    browser.quit()
