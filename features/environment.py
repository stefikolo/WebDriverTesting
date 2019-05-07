from behave import use_fixture
from lib.fixtures.fixtures import selenium_chrome_driver, selenium_firefox_driver


def before_tag(context, tag):
    if tag == 'chrome':
        use_fixture(selenium_chrome_driver, context)
    else:
        use_fixture(selenium_firefox_driver, context)
