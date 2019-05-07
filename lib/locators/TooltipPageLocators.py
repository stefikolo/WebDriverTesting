from selenium.webdriver.common.by import By


class TooltipPageLocators:
    TOOLTIP_LABEL = (By.XPATH, "//label[@for='age']")
    AGE_FIELD = (By.XPATH, "//input[@id='age']")
    TOOLTIP = (By.CSS_SELECTOR, ".ui-tooltip")
