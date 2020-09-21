"""
Author:Jyothsna
Date:27/8/2020
"""
from pages.home.login_page import LoginPage
from utilities import xlutil
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        path="H:\\Data\\data.xlsx"
        rows=xlutil.RowCount(path,'Sheet1')
        for r in range(2,rows+1):
            username=xlutil.readData(path,"Sheet1",r,1)
            password= xlutil.readData(path, "Sheet1", r, 2)


        self.lp.login(username,password )
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login Verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        result = self.lp.verifyLoginFailed()
        assert result == True