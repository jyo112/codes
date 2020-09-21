import time

import cl as cl
from selenium.webdriver.support.select import Select

from utilities import custom_logger as cl, xlutil
from base.basepage import BasePage
import logging


class Project_Customer(BasePage):
    log = cl.customLogger(logging.DEBUG)
    _task = "//div[text()='Tasks']"
    _project = "//a[text()='Projects & Customers']"
    _create_cust = "//span[text()='Create Customer']"
    _create_proj = "//span[text()='Create Project']"
    _cust_name = "//input[@name='name']"
    # send
    # data
    _radio_button = "(//input[@name='afterCreateAction'])[3]"
    _create_custmer = "//input[@name='createCustomerSubmit']"
    _create_project="//span[text()='Create Project']"
    _add_project = "//input[@name='name']"
    _radi_add_more_projects = "//input[@id='add_more_projects']"
    # submit_addmor
    radi_add_more_projects = "//input[@name='createProjectSubmit']"
    _pro_name="//input[@name='name']"
    _option="//select[@name='customerId']"
    _option1="//select[@name='selectedCustomer']"
    _project_submit="//input[@name='createProjectSubmit']"
    _check_box="//input[@name='customers[29]']"
    _delete="//input[@value='Delete Selected']"
    _show="//input[@value='   Show   ']"
    _checkbox1="(//input[@type='checkbox'])[2]"
    _iframe="//iframe(@id='editDescriptionPopupIframe']"
    _deletecustomer="//input[@value='Delete This Customer']"

    def project(self):
     path = "H:\Data1\\data.xlsx"
     rows = xlutil.RowCount(path, 'Sheet2')
     self.elementClick(self._task, locatorType="xpath")
     self.elementClick(self._project, locatorType="xpath")
     time.sleep(10)

     def reading_data(data):
         self.sendKeys(data, self._cust_name, locatorType="xpath")

     def reading_projectdata(data):
         self.sendKeys(data, self._pro_name, locatorType="xpath")

     self.elementClick(self._create_cust, locatorType="xpath")
     for r in range(2, rows + 1):
         input= xlutil.readData(path, "Sheet2", r, 1)
         print(input)
         reading_data(input)
         time.sleep(10)
         self.elementClick(self._radio_button, locatorType="xpath")
         time.sleep(10)
         self.elementClick(self._create_custmer, locatorType="xpath")
     print("before project")
     self.elementClick(self._project, locatorType="xpath")
     self.elementClick(self._create_project, locatorType="xpath")
     try:
      print("to select visibletext")
      select = Select(self.getElement(self._option, locatorType="xpath"))
      print("aftr selection")
      for r in range(2, rows + 1):
          input2 = xlutil.readData(path, "Sheet3", r, 1)
          print(input2)
          select.select_by_visible_text(input2)
      print("visible text selected")
     except:
         print("hello")

     for r in range(2, rows + 1):
          input1= xlutil.readData(path, "Sheet3", r, 2)
          print(input1)
          reading_projectdata(input1)
          time.sleep(10)
          self.elementClick(self._radi_add_more_projects, locatorType="xpath")
          time.sleep(1)
          self.elementClick(self._project_submit, locatorType="xpath")


    def delete(self):
        path = "H:\Data1\\data.xlsx"
        rows = xlutil.RowCount(path, 'Sheet2')
        self.elementClick(self._task, locatorType="xpath")
        self.elementClick(self._project, locatorType="xpath")
        try:
          print("to select visibletext")
          select = Select(self.getElement(self._option1, locatorType="xpath"))
          print("aftr selection")
          for r in range(2, rows + 1):
             dele= xlutil.readData(path, "Sheet4", r, 1)
             print(dele)
             time.sleep(1)
             select.select_by_visible_text(dele)
             print("visibal selected")
             time.sleep(2)
             self.elementClick(self._show, locatorType="xpath")
             print("show")
             time.sleep(2)
             self.elementClick(self._checkbox1, locatorType="xpath")
             print("chexkbox")
             time.sleep(2)
             self.elementClick(self._delete, locatorType="xpath")
             print("switching to frame")

             self.driver.switch_to.frame(self.getElement(self._iframe, locatorType="xpath"))
             print("deleting")
             self.elementClick(self._deletecustomer, locatorType="xpath")
        except:
          print("except block")


     # creating project
    #  def project(self):
    #      self.elementClick(self._task, locatorType="xpath")
    #      self.elementClick(self._project, locatorType="xpath")
    #      self.elementClick(self._create_cust, locatorType="xpath")
    #      self.sendKeys("jo", self._cust_name, locatorType="xpath")
    #      self.elementClick(self._radio_button, locatorType="xpath")
    #      self.elementClick(self._create_custmer, locatorType="xpath")
    #      self.sendKeys("vi", self._cust_name, locatorType="xpath")
    #      self.elementClick(self._radio_button, locatorType="xpath")
    #      self.elementClick(self._create_custmer, locatorType="xpath")
    #      self.elementClick(self._project, locatorType="xpath")
    #      self.elementClick(self._create_project, locatorType="xpath")
    #      try:
    #          select = Select(self.getElement(self._option, locatorType="xpath"))
    #          select.select_by_visible_text('jo')
    #      except:
    #          print("hello")
    #      self.sendKeys("account", self._pro_name, locatorType="xpath")
    #      self.elementClick(self._radi_add_more_projects, locatorType="xpath")
    #      self.elementClick(self._project_submit, locatorType="xpath")
    #
    #      # creating project
    #
    #  #
    #
    # #
