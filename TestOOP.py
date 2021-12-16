from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class MyTest:
    username_id = "txtUsername"
    password_id = "txtPassword"
    link = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)

    def setUserName(self, username):
        self.username_input = self.driver.find_element(By.ID, self.username_id)
        self.username_input.clear()
        self.username_input.send_keys(username)
        self.title = self.driver.title
        assert self.title == 'OrangeHRM'

    def setPassword(self, password):
        self.password_input = self.driver.find_element(By.ID, self.password_id)
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click(self, button):
        self.driver.find_element(By.XPATH, button).click()

    def select(self, field, data):
        self.selectFielf = self.driver.find_element(By.XPATH, field)
        self.selectFielf.clear()
        self.selectFielf.send_keys(data)

    def delete(self, field):
        self.selectFielf2 = self.driver.find_element(By.XPATH, field).get_attribute('href')
        self.value = self.selectFielf2[(self.selectFielf2.index('=') + 1)::]
        self.srt = "ohrmList_chkSelectRecord_"
        self.srt += str(self.value)
        self.driver.find_element(By.ID, self.srt).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()

username = 'Admin'
password = 'admin123'
test = MyTest()
test.setUserName(username)
test.setPassword(password)
test.click('//*[@id="btnLogin"]') 
test.click("/html/body/div[1]/div[2]/ul/li[1]/a/b")  
test.click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")
test.click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a") 
test.click("/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]")
test.select('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/input[1]', 'userX')  
test.click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")
test.click('/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input') 
test.select('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/input', 'AUD - Australian Dollar')
test.select('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input', '1000')
test.select('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input', '10000')
test.click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")
test.click("/html/body/div[1]/div[2]/ul/li[1]/a/b") 
test.click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a") 
test.click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a") 
test.delete("//*[contains(text(), 'userX')]")  
