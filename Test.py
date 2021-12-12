# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test11():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_11(self):
    self.driver.get("https://opensource-demo.orangehrmlive.com/")
    self.driver.set_window_size(850, 816)
    self.driver.find_element(By.CSS_SELECTOR, "#divUsername > .form-hint").click()
    self.driver.find_element(By.ID, "txtUsername").click()
    self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
    self.driver.find_element(By.ID, "txtPassword").click()
    self.driver.find_element(By.ID, "txtPassword").click()
    self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
    self.driver.find_element(By.ID, "btnLogin").click()
    self.driver.find_element(By.ID, "menu_admin_viewPayGrades").click()
    self.driver.find_element(By.ID, "btnAdd").click()
    self.driver.find_element(By.ID, "payGrade_name").click()
    self.driver.find_element(By.ID, "payGrade_name").send_keys("Sobol Maria")
    self.driver.find_element(By.ID, "payGrade_name").send_keys("Sobol Mariia")
    self.driver.find_element(By.ID, "btnSave").click()
    self.driver.find_element(By.ID, "btnAddCurrency").click()
    self.driver.find_element(By.ID, "payGradeCurrency_currencyName").click()
    self.driver.find_element(By.ID, "payGradeCurrency_currencyName").send_keys("d")
    self.driver.find_element(By.CSS_SELECTOR, ".ac_even:nth-child(1)").click()
    self.driver.find_element(By.ID, "payGradeCurrency_minSalary").click()
    self.driver.find_element(By.ID, "payGradeCurrency_minSalary").send_keys("1000")
    self.driver.find_element(By.ID, "payGradeCurrency_maxSalary").click()
    self.driver.find_element(By.ID, "payGradeCurrency_maxSalary").send_keys("10000")
    self.driver.find_element(By.ID, "btnSaveCurrency").click()
    self.driver.find_element(By.ID, "menu_admin_viewPayGrades").click()
    self.driver.find_element(By.ID, "ohrmList_chkSelectRecord_14").click()
    self.driver.find_element(By.ID, "btnDelete").click()
    self.driver.find_element(By.ID, "dialogDeleteBtn").click()
  
