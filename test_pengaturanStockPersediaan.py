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

class TestPengaturanStockPersediaan():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pengaturanStockPersediaan(self):
    # Test name: Pengaturan Stock Persediaan
    # Step # | name | target | value
    # 1 | open | https://app.jubelio.com/home/inventory | 
    self.driver.get("https://app.jubelio.com/home/inventory")
    # 2 | setWindowSize | 1280x672 | 
    self.driver.set_window_size(1280, 672)
    # 3 | mouseOver | css=.ladda-button:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".ladda-button:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 4 | mouseOut | css=.ladda-button:nth-child(2) | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 5 | click | css=.btn-primary > .ladda-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn-primary > .ladda-label").click()
    # 6 | type | css=.form-group:nth-child(2) .form-control | 14 Mei 2023
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(2) .form-control").send_keys("14 Mei 2023")
    # 7 | click | name=note | 
    self.driver.find_element(By.NAME, "note").click()
    # 8 | type | name=note | Tersedia
    self.driver.find_element(By.NAME, "note").send_keys("Tersedia")
    # 9 | click | css=.col-md-12 > .form-control | 
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control").click()
    # 10 | type | css=.col-md-12 > .form-control | Purple-11
    self.driver.find_element(By.CSS_SELECTOR, ".col-md-12 > .form-control").send_keys("Purple-11")
    # 11 | click | css=.input-group-btn .ladda-label | 
    self.driver.find_element(By.CSS_SELECTOR, ".input-group-btn .ladda-label").click()
    # 12 | click | css=.react-grid-Cell:nth-child(6) .text-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right").click()
    # 13 | click | css=.react-grid-Cell:nth-child(6) .text-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right").click()
    # 14 | doubleClick | css=.react-grid-Cell:nth-child(6) .text-right | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 15 | type | css=.editor-main | 1200000
    self.driver.find_element(By.CSS_SELECTOR, ".editor-main").send_keys("1200000")
    # 16 | click | css=.react-grid-Cell:nth-child(2) .text-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(2) .text-right").click()
    # 17 | click | css=.react-grid-Canvas | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Canvas").click()
    # 18 | click | css=.react-grid-Cell:nth-child(6) .text-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right").click()
    # 19 | click | css=.react-grid-Cell:nth-child(6) .text-right | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right").click()
    # 20 | doubleClick | css=.react-grid-Cell:nth-child(6) .text-right | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Cell:nth-child(6) .text-right")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    # 21 | type | css=.editor-main | 12000000
    self.driver.find_element(By.CSS_SELECTOR, ".editor-main").send_keys("12000000")
    # 22 | click | css=.react-grid-Canvas | 
    self.driver.find_element(By.CSS_SELECTOR, ".react-grid-Canvas").click()
    # 23 | click | css=.page-editor | 
    self.driver.find_element(By.CSS_SELECTOR, ".page-editor").click()
    # 24 | click | css=.pull-right > .ladda-button | 
    self.driver.find_element(By.CSS_SELECTOR, ".pull-right > .ladda-button").click()
    # 25 | close |  | 
    self.driver.close()
  
