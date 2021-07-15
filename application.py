from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

LOG_IN_LINK = "//a[contains(text(),'Log In')]"
LOG_IN_BUTTON = "//button[contains(text(),'Log In')]"


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def login(self, email, password):
        wd = self.wd
        wd.find_element_by_xpath(LOG_IN_LINK).click()
        wd.find_element_by_id("email").click()
        wd.find_element_by_xpath("//input[@id='email']").is_enabled()
        wd.find_element_by_id("email").send_keys(email)
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath(LOG_IN_BUTTON).click()
        wd.find_element_by_xpath("//span[contains(text(),'auto_first_name')]").is_displayed()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://grinfer.com/")

    def destroy(self):
        wd = self.wd
        wd.quit()
