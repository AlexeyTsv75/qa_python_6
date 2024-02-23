from selenium.webdriver.common.by import By


class MainPageLocator:
    BUTTON_CONFIRM_COCKY = By.ID, "rcc-confirm-button"
    QUESTION_LOCATOR = By.ID, "accordion__heading-{}"
    ANSWER_LOCATOR = By.XPATH, ".//*[@id='accordion__panel-{}']/p"
