from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager as cdm
from selenium import webdriver

from lib.locators.TabsPageLocators import TabsPageLocators
from lib.page_objects.homepage import HomePage


class TabsPage:

    def __init__(self):
        self.driver = webdriver.Chrome(cdm().install())
        self.hp = HomePage(driver=self.driver)

    def go_to_tab(self, tab_number):
        clicked_tab = self.driver.find_element(*TabsPageLocators().TAB(tab_number)).click()
        return clicked_tab

    def hover_over_tab(self, tab_number):
        actions = ActionChains(self.driver)
        hovered_tab = actions.move_to_element(
            self.driver.find_element(*TabsPageLocators().TAB(tab_number))
        ).perform()
        return hovered_tab

    def get_active_tab_text(self):
        block_text = self.driver.find_element(*TabsPageLocators.TAB_TEXT).text
        return block_text

    def tab_css_property_on_clicked(self, tab_number, property_name):
        self.go_to_tab(tab_number)
        loc = self.driver.find_element(*TabsPageLocators().TAB(tab_number)).value_of_css_property(property_name)
        return loc

    def tab_css_property_on_hover(self, tab_number, property_name):
        self.hover_over_tab(tab_number)
        li_loc = self.driver.find_element(*TabsPageLocators().TAB(tab_number))
        a_loc = li_loc.find_element(*TabsPageLocators.TAB_URL).value_of_css_property(property_name)
        return a_loc
