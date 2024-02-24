from selenium.webdriver.common.by import By


class OrderPageLocator:
    UPPER_ORDER_BUTTON = By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"
    QUESTION_LOCATOR = By.ID, "accordion__heading-0"
    LOWER_ORDER_BUTTON = By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_UltraBig__UU3Lp']"
    FIELD_NAME = By.XPATH,".//input[@placeholder = '* Имя']"
    FIELD_FAMILY = By.XPATH, ".//input[@placeholder = '* Фамилия']"
    FIELD_ADDRESS = By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']"
    FIELD_METRO = By.XPATH, ".//input[@placeholder = '* Станция метро']"
    METRO_NAME = By.XPATH, ".//div[text() = '{}']"
    FIELD_PHONE = By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']"
    FORWARD_BUTTON = By.XPATH, ".//button[text() = 'Далее']"
    FIELD_DATE = By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']"
    FIELD_TERM = By.XPATH, ".//div[text() = '* Срок аренды']"
    DURATION_LIST = By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = '{}']"
    COLOR_CHOOSE = By.ID, "{}"
    FIELD_COMMENT = By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']"
    LIST_ORDER_BUTTON = By.XPATH, (".//button[(@class = 'Button_Button__ra12g Button_Middle__1CSJM') and (text() = 'Заказать')]")
    ORDER_CONFIRMATION_BUTTON = By.XPATH, (".//button[(@class = 'Button_Button__ra12g Button_Middle__1CSJM') and (text() = 'Да')]")
    CHECK_STATUS_BUTTON = By.XPATH, (".//button[(@class = 'Button_Button__ra12g Button_Middle__1CSJM') and (text() = 'Посмотреть статус')]")
    FILLED_NAME = By.XPATH, ".//div[text() = 'Имя']/following-sibling::div"
    CHOSEN_DATE = By.XPATH, ".//div[contains(@class, 'selected')]"






