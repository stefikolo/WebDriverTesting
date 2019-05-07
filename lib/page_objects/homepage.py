from lib.locators.HomePageLocators import HomePageLocators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        # = webdriver.Chrome(cdm().install())

    def main_tools_QA_page(self):
        self.driver.find_element(*HomePageLocators.TOOLS_QA_URL).click()

    def go_to_section(self, menu_name, section_name):
        if menu_name == 'top_menu':
            self.driver.find_element(*HomePageLocators().TOP_MENU_ITEM(section_name)).click()
        else:
            self.driver.find_element(*HomePageLocators().TOP_MENU_ITEM(section_name)).click()

        section_header = self.driver.find_element(*HomePageLocators.HEADER).text
        return section_header

    def go_to_subsection(self, main_section, subsection_name):
        self.driver.find_element(*HomePageLocators().TOP_MENU_ITEM(main_section)).click()
        if main_section == 'Home':
            print("No subsection available")
        else:
            self.driver.find_element(*HomePageLocators().SUBMENU_ITEM(subsection_name)).click()


if __name__ == '__main__':
    pass
