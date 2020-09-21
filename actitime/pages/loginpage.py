import time

import cl as cl
from selenium.webdriver.support.select import Select

from utilities import custom_logger as cl
from base.basepage import BasePage
import logging


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
    # username = "//input[@name='username']"
    # password="//input[@name='pwd']"
    # login="//div[text()='Login ']"
    _email_field = "//input[@name='username']"
    _password_field = "//input[@name='pwd']"
    _login_button = "//div[text()='Login ']"
    _new="//a[text()='New']"
    _option="//select[@name='customerId']"
    _customer_name="//input[@name='customerName']"
    _name="internal"
    _name1= "internal12"
    _name2= "internal23"
    _project_name="//input[@name='projectName']"
    _pname="account"
    _pname1 = "Admin"
    _createtask_button="//input[@class='hierarchy_element_wide_button']"
    _task_name="//input[@id='task[0].name']"
    _tname="management"
    _tname1= "administrating"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enterEmail(self, email):
        print(email)
        self.elementClick(self._email_field, locatorType="xpath")
        self.sendKeys(email, self._email_field,locatorType="xpath")

    def enterPassword(self, password):
        self.elementClick(self._password_field, locatorType="xpath")
        self.sendKeys(password, self._password_field,locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")

    def login(self, UN="", PWD=""):
            self.enterEmail(UN)
            print(UN)

            self.enterPassword(PWD)
            print(PWD)

            self.clickLoginButton()
            time.sleep(2)

