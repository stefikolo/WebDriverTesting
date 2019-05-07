from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver

from lib.locators.TooltipPageLocators import TooltipPageLocators
from lib.page_objects.homepage import HomePage


class TooltipPage:

    def __init__(self):
        self.driver = webdriver.Chrome(cdm().install())
        self.hp = HomePage(driver=self.driver)

    def age_field_css(self, css_property):
        self.driver.find_element(*TooltipPageLocators.TOOLTIP_LABEL).click()
        field = self.driver.find_element(*TooltipPageLocators.AGE_FIELD)
        return field.value_of_css_property(css_property)

    def focused_age_field_css(self, css_property):
        focused = self.driver.find_element(*TooltipPageLocators.AGE_FIELD).click()
        return focused.value_of_css_property(css_property)

    def fill_age_field(self, age):
        self.driver.find_element(*TooltipPageLocators.AGE_FIELD).send_keys(age)

    def hover_over_age_field(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.driver.find_element(*TooltipPageLocators.AGE_FIELD)).perform()
        hidden_tooltip = self.driver.find_element(*TooltipPageLocators.TOOLTIP).text
        return hidden_tooltip
