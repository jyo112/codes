

import cl as cl
from selenium.webdriver.support.select import Select

from utilities import custom_logger as cl
from base.basepage import BasePage
import logging


class TimeTrackPage(BasePage):

    log = cl.customLogger(logging.DEBUG)
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

    def custmer_name(self):
            self.elementClick(self._customer_name, locatorType="xpath")
            self.sendKeys(self._name, self._customer_name, locatorType="xpath")

    def custmer_nametwo(self):
        self.elementClick(self._customer_name, locatorType="xpath")
        self.sendKeys(self._name1, self._customer_name, locatorType="xpath")

    def project_name(self):
        self.elementClick(self._project_name, locatorType="xpath")
        self.sendKeys(self._pname, self._project_name, locatorType="xpath")

    def project_nametwo(self):
            self.elementClick(self._project_name, locatorType="xpath")
            self.sendKeys(self._pname1, self._project_name, locatorType="xpath")

    def task_name(self):
        self.elementClick(self._task_name, locatorType="xpath")
        self.sendKeys(self._tname, self._task_name, locatorType="xpath")
    def create_newproject(self):
        self.elementClick(self._new,locatorType="xpath")
        self.switch_to_window()
        self.elementClick(self._option,locatorType="xpath")
        try:
         select = Select(self.getElement(self._option,locatorType="xpath"))
         select.select_by_visible_text('-- new customer --')
        except:
            print("handled")
        self.custmer_name()
        self.project_name()
        self.task_name()
        self.elementClick(self._createtask_button, locatorType="xpath")

        # self.elementClick(self._new, locatorType="xpath")
        # self.switch_to_window()
        # self.elementClick(self._option, locatorType="xpath")
        # select = Select(self.getElement(self._option, locatorType="xpath"))
        #
        # # select by visible text
        # select.select_by_visible_text('-- new customer --')
        # self.custmer_nametwo()
        # self.project_nametwo()
        # self.task_name()
        #
        # self.elementClick(self._createtask_button, locatorType="xpath")











