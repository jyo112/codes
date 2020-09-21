"""Author:jyothsna
date:4/8/2020"""
import time
import pytest

from drivers.driverfactory import *
pytest.mark.usefixtures("oneTimeSetUp")
class Testscenario():
 pytest.fixture(autouse=True)
 def test_adding_to_cart(self,oneTimeSetUp):
  self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  iph=self.driver.find_element_by_xpath("//a[text()='iphone X']").text
  samph=self.driver.find_element_by_xpath("//a[text()='Samsung Note 8']").text
  self.driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
  self.driver.find_element_by_xpath("(//button[@class='btn btn-info'])[2]").click()

  self.driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
  cartiph=self.driver.find_element_by_xpath("//a[text()='iphone X']").text
  cartsamph=self.driver.find_element_by_xpath("//a[text()='Samsung Note 8']").text
  assert iph==cartiph,print("not same")
  print("same iphone in cart")
  assert samph==cartsamph,print("not samsung")
  print("same samsung phone in cart")
  iphoneprice = self.driver.find_element_by_xpath("(//strong[text()='₹. 100000'])[2]").text
  iphone = int(iphoneprice[3:9])
  samsungprice = self.driver.find_element_by_xpath("(//strong[text()='₹. 85000'])[2]").text
  sam = (int(samsungprice[3:8]))
  total =self. driver.find_element_by_xpath("//strong[text()='₹. 185000']").text
  TOTAL = (int(total[3:9]))
  list = []
  list.append(sam)
  list.append(iphone)
  print(sam)
  print(iphone)
  print(TOTAL)
  print(list)
  Sum = sum(list)
  print(Sum)
  assert Sum == TOTAL, print("not matched")
  print("price matched")
  self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
  time.sleep(10)
  self.driver.find_element_by_xpath("//input[@id='country']").send_keys("india")
  time.sleep(10)
  self.driver.find_element_by_xpath("//a[text()='India']").click()
  self.driver.find_element_by_xpath("//label[@for='checkbox2']").click()
 # driver.find_element_by_xpath("//button[@aria-label='Close']").click()
  self.driver.find_element_by_xpath("//input[@value='Purchase']").click()
  message = self.driver.find_element_by_xpath("//strong[text()='Success!']").text
  expectedmessage = "Success!"
  assert message == expectedmessage, print(" not successfull")
  print("successfull message displayed")
  self.driver.close()


