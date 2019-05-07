from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver

# from lib.locators.SelectmenuPageLocators import SelectmenuPageLocators
from lib.page_objects.homepage import HomePage

from selenium.webdriver.common.by import By


class SelectmenuPageLocators:
    def MENU_BUTTON(self, menu_name):
        return By.XPATH, f"//span[@aria-owns='{menu_name}-menu']/span[contains(@class, 'text')]"

    def SELECT_MENU_OPTION(self, menu_name, option_id):
        return By.XPATH, "//div[contains(@class, 'ui-selectmenu-open')]/" \
            f"ul[contains(@aria-labelledby, '{menu_name}-button')]/li/div[contains(@id, '{option_id}')]"

    def SPEED_MENU_OPTION_NAME(self, option_id):
        return By.XPATH, f"//select[@name='speed']/option[{option_id}]"


class SelectmenuPage:
    def __init__(self):
        self.driver = webdriver.Chrome(cdm().install())
        self.hp = HomePage(driver=self.driver)

    def open_menu(self, menu_name):
        self.driver.find_element(*SelectmenuPageLocators().MENU_BUTTON(menu_name)).click()

    def select_menu_option(self, menu_name, option_id):
        self.driver.find_element(*SelectmenuPageLocators().SELECT_MENU_OPTION(menu_name, option_id)).click()


if __name__ == '__main__':
    sp = SelectmenuPage()
    sp.driver.get('https://demoqa.com/')
    sp.hp.go_to_subsection('Widgets', 'selectmenu')
    sp.open_menu('salutation')
    sp.select_menu_option('salutation', 3)
    sleep(2)

    sp.driver.quit()
