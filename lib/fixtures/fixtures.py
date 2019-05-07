from webdriver_manager.chrome import ChromeDriverManager as cdm
from webdriver_manager.firefox import GeckoDriverManager as gdm
from behave import fixture
from selenium import webdriver


@fixture
def selenium_chrome_driver(context):
    context.driver = webdriver.Chrome(cdm().install())
    yield context.driver

    context.driver.quit()


@fixture
def selenium_firefox_driver(context):
    context.driver = webdriver.Firefox(executable_path=gdm().install())
    yield context.driver

    context.driver.quit()
