from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver

from lib.locators.SpinnerPageLocators import SpinnerPageLocators
from lib.page_objects.homepage import HomePage


class SpinnerPage:

    def __init__(self):
        self.driver = webdriver.Chrome(cdm().install())
        self.hp = HomePage(driver=self.driver)

    def spin_up(self):
        self.driver.find_element(*SpinnerPageLocators.SPIN_UP).click()

    def spin_down(self):
        self.driver.find_element(*SpinnerPageLocators.SPIN_DOWN).click()

    def enter_value_in_spinner_field(self, value):
        self.driver.find_element(*SpinnerPageLocators.SPIN_BUTTON).send_keys(value)

    def check_value(self):
        value = self.driver.find_element(*SpinnerPageLocators.SPIN_BUTTON).get_attribute('aria-valuenow')
        return value

    def disable_spinner(self):
        self.driver.find_element(*SpinnerPageLocators.DISABLE_SPINNER).click()

    def toggle_widget(self):
        self.driver.find_element(*SpinnerPageLocators.TOGGLE_SPINNER_WIDGET).click()

    def click_set_value_button(self):
        self.driver.find_element(*SpinnerPageLocators.SET_VALUE_BUTTON).click()

    def click_get_value_button(self):
        self.driver.find_element(*SpinnerPageLocators.GET_VALUE_BUTTON).click()

    def spinner_is_disabled(self):
        locator_attr = self.driver.find_element(*SpinnerPageLocators.SPINNER_STATE).get_attribute('class')
        return 'ui-state-disabled' in locator_attr

    def spinner_widget_is_disabled(self):
        locator = self.driver.find_element(*SpinnerPageLocators.SPIN_BUTTON)
        try:
            locator.get_attribute('role')
            self.driver.find_element(*SpinnerPageLocators.SPIN_UP).click()
        except:
            return True
        else:
            return False

    def get_value_from_alert(self):
        alert = Alert(self.driver)
        alert_value = alert.text
        return alert_value

    def dismiss_alert(self):
        Alert(self.driver).dismiss()
