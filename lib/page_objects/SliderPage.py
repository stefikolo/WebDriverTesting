from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver
import re

from lib.locators.SliderPageLocators import SliderPageLocators
from lib.page_objects.homepage import HomePage


class SliderPage:
    def __init__(self):
        self.driver = webdriver.Chrome(cdm().install())
        self.hp = HomePage(driver=self.driver)

    def click_on_slider_button(self):
        self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON).click()

    # TODO
    # def click_on_slider_scale(self):
    #     actions = ActionChains(self.driver)
    #     scale = actions.move_to_element_with_offset(
    #         self.driver.find_element(*SliderPageLocators.SLIDER_SCALE), 960, 327).click().perform()
    #     return scale

    def hover_over_slider_button(self):
        actions = ActionChains(self.driver)
        hovered_tab = actions.move_to_element(
            self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON)
        ).perform()
        return hovered_tab

    def click_and_hold_slider(self):
        actions = ActionChains(self.driver)
        click_hold = actions.click_and_hold(
            self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON)
        ).perform()
        return click_hold

    def move_slider(self, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.click_and_hold(
            self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON)
        ).move_by_offset(x_offset, y_offset).perform()

    def get_slider_css_attribute(self, attribute_name):
        value = self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON).value_of_css_property(attribute_name)
        return value

    def get_slider_attribute(self, attribute_name):
        value = self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON).get_attribute(attribute_name)
        return value

    def get_slider_position(self):
        pattern = re.compile("\d+%")
        attr_value = self.driver.find_element(*SliderPageLocators.SLIDER_BUTTON).get_attribute('style')
        percent_value = pattern.search(attr_value).group(0)
        return percent_value
