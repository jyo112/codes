from selenium import webdriver
class DriverFactory():
    def __init__(self, driver):
        super(DriverFactory,self).__init__()
        self.browser = None
        self.driver=driver

    def getWebDriverInstance(self):
        driver = webdriver.Chrome(executable_path= "C:\\Users\\Kiran\\AppData\\Local\\Programs\\Python\\Python36\\Scripts\\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get("https://rahulshettyacademy.com/angularpractice/shop")
        return driver
