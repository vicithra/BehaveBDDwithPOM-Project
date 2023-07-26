from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
service = Service(executable_path="PATH_TO_DRIVER")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
from Utilities import configReader
import logging
from Utilities.LogUtil import Logger
from selenium.webdriver.common.by import By

log = Logger(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element("xpath",configReader.readConfig('locators', locator)).click()
        log.logger.info("Clicking on an element: " + str(locator))

    def type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element("xpath",configReader.readConfig('locators', locator)).send_keys(value)
        log.logger.info("Typing in an element: " + str(locator) + " value entered as : " + str(value))

    def select(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element("xpath",configReader.readConfig('locators', locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)

        log.logger.info("Selecting from an element: " + str(locator) + " value selected as : " + str(value))
