# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CalfAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_calf_add(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("Admin")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("password123")
        driver.find_element_by_id("submit").click()
        driver.find_element_by_xpath("//li[3]/a/h2").click()
        driver.find_element_by_css_selector("button").click()
        driver.find_element_by_css_selector("tr.model-calf > td > a.addlink").click()
        driver.find_element_by_id("id_calf_Id").clear()
        driver.find_element_by_id("id_calf_Id").send_keys("1241")
        driver.find_element_by_id("id_Breed").clear()
        driver.find_element_by_id("id_Breed").send_keys("dafsdfa")
        driver.find_element_by_css_selector("div.form-row.field-date_of_expiry_insurance > div > span.datetimeshortcuts > a").click()
        driver.find_element_by_name("_save").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
