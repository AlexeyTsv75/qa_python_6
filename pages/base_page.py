from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        element_text = element.text
        return element_text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    def change_locator_data(self, locator_x, num):
        method, locator = locator_x
        locator = locator.format(num)
        locator_x = [method, locator]
        return locator_x

    def check_answer(self, result, expected):
        return result == expected

    def roll_to_locator(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
