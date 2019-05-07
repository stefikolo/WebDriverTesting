from selenium.webdriver.common.by import By


class TabsPageLocators:
    TAB_TEXT = (By.XPATH, "//div[@aria-hidden='false']")
    TAB_URL = (By.XPATH, "./a")

    def TAB(self, tab_number):
        return By.XPATH, f"//li[@aria-controls='tabs-{tab_number}']"
