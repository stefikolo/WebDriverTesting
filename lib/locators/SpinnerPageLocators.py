from selenium.webdriver.common.by import By


class SpinnerPageLocators:
    SPIN_DOWN = (By.XPATH, "//a[contains(@class, 'spinner-down')]")
    SPIN_BUTTON = (By.XPATH, "//input[@id='spinner']")
    SPIN_UP = (By.XPATH, "//a[contains(@class, 'spinner-up')]")
    DISABLE_SPINNER = (By.XPATH, "//button[@id='disable']")
    TOGGLE_SPINNER_WIDGET = (By.XPATH, "//button[@id='destroy']")
    SET_VALUE_BUTTON = (By.XPATH, "//button[@id='setvalue']")
    GET_VALUE_BUTTON = (By.XPATH, "//button[@id='getvalue']")
    SPINNER_STATE = (By.XPATH, "//span[contains(@class, 'ui-spinner')]")
