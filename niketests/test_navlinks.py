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

class TestNavlinks():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_navlinks(self):
    # Test name: navlinks
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("http://localhost:5500/")
    # 2 | setWindowSize | 1032x720 | 
    self.driver.set_window_size(1032, 720)
    # 3 | click | linkText=Products | 
    self.driver.find_element(By.LINK_TEXT, "Products").click()
    # 4 | click | linkText=Cart | 
    self.driver.find_element(By.LINK_TEXT, "Cart").click()
    # 5 | click | linkText=Home | 
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    # 6 | click | linkText=Login | 
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    # 7 | click | linkText=Home | 
    self.driver.find_element(By.LINK_TEXT, "Home").click()
  