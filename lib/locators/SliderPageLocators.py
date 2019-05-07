from selenium.webdriver.common.by import By


class SliderPageLocators:
    SLIDER_SCALE = (By.XPATH, "//span[contains(@class, 'ui-slider')]")
    SLIDER_BUTTON = (By.XPATH, "//div[contains(@class, 'ui-slider-handle')]")
