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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: Login
    # Step # | name | target | value
    # 1 | open | /login | 
    self.driver.get("https://app.jubelio.com/login")
    # 2 | setWindowSize | 1280x672 | 
    self.driver.set_window_size(1280, 672)
    # 3 | type | name=email | qa.rakamin.jubelio@gmail.com
    self.driver.find_element(By.NAME, "email").send_keys("qa.rakamin.jubelio@gmail.com")
    # 4 | type | name=password | Jubelio123!
    self.driver.find_element(By.NAME, "password").send_keys("Jubelio123!")
    # 5 | click | css=.ladda-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".ladda-button").click()
    # 6 | close |  | 
    self.driver.close()
  
