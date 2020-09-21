# """
# Author:Jyothsna
# Date:9/3/2020
# """
# import time
#
# from pages.loginpage import LoginPage
# from utilities import xlutil
# from pages.time_track_page import  TimeTrackPage
# from pages.project_customers_page import Project_Customer
#
# import unittest
# import pytest
#
# @pytest.mark.usefixtures("oneTimeSetUp", "setUp")
# class CreateProject(unittest.TestCase):
#
#     @pytest.fixture(autouse=True)
#     def classSetup(self, oneTimeSetUp):
#         # self.lp = LoginPage(self.driver)
#         self.pc=Project_Customer(self.driver)
#
#     @pytest.mark.run(order=2)
#     def test_addproject(self):
#         self.pc.project()
#
#
#
