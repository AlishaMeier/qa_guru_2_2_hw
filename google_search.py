from selene import be, have
from selene.support.shared import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def window_size():
    browser.config.window_height = 700
    browser.config.window_width = 560
    yield
    browser.close_current_tab()


def google_search_positive(window_size):
    browser.open('https://google.com/ncr')
    browser.element('[name="q"]').should(be.blank).type('selene github yashaka').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def google_search_negative(window_size):
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.no.text('Blah-blah-blah'))
