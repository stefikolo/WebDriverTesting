from selenium.webdriver.common.by import By


class HomePageLocators:
    # section_name = ''
    TOOLS_QA_URL = (By.XPATH, "//div/a[@href='https://www.toolsqa.com/']")
    HEADER = (By.XPATH, "//h1")

    def TOP_MENU_ITEM(self, section_name):
        return By.XPATH, f"//li[@class='menu-item']/a[@title='{section_name}']"

    def ASIDE_MENU_ITEM(self, section_name):
        return By.XPATH, f"//aside/ul/li/a[contains(@href, '{section_name}')]"

    def SUBMENU_ITEM(self, subsection_name):
        return By.XPATH, f"//div[@class='demo-frame']/ul/li/a[contains(@href, '{subsection_name}')]"
