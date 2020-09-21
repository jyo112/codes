"""
Author:Jyothsna
Date:9/3/2020
"""
import time

from pages.loginpage import LoginPage
from pages.project_customers_page import Project_Customer
from utilities import xlutil
from pages.time_track_page import  TimeTrackPage

import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.tp=TimeTrackPage(self.driver)
        self.pc = Project_Customer(self.driver)
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        path="H:\Data1\\data.xlsx"
        rows=xlutil.RowCount(path,'Sheet1')
        for r in range(2,rows+1):
            usernam=xlutil.readData(path,"Sheet1",r,1)
            passwor= xlutil.readData(path, "Sheet1", r, 2)
            print(usernam)
            print(passwor)

        self.lp.login(usernam,passwor)

        self.pc.project()
        self.pc.delete()
    # @pytest.mark.run(order=1)
    # def test_create_project(self):
    #     self.tp.create_newproject()


    # @pytest.mark.run(order=3)
    # def test_create_project(self):
    #     self.lp.create_second_project()
    #
    #
    # @pytest.mark.run(order=4)
    # def test_create_project_customer(self):
