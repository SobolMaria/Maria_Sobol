from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class MyTest:
    @pytest.fixture()
    def init(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def click_button(self, xpath):
        self.driver.find_element(By.XPATH, xpath).click()

    def enter_info(self, xpath, data):
        self.driver.find_element(By.XPATH, xpath).send_keys(data)

    def delete_button(self, xpath):
        self.driver.find_element(By.ID, self.srt).click()
        self.driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()

test = MyTest()

test.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input', 'Admin')
test.enter_info('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input', 'admin123')
test.click_button('/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input')
test.click_button('/html/body/div[1]/div[2]/ul/li[1]/a')
test.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a')
test.click_button('/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[2]/a')
test.click_button('/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]')
test.enter_info('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/input[1]', 'Mariia Sobol')
test.click_button('/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]')
test.click_button('/html/body/div[1]/div[3]/div[3]/div[2]/form/p/input')
test.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/input', 'AUD - Australian Dollar')
test.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input', '1000')
test.enter_info('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input', '10000')
test.click_button('/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/p/input[1]')
test.delete_button("//*[contains(text(), 'Mariia Sobol')]")
