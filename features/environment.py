import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="PATH_TO_DRIVER")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
def before_scenario(context,driver):
    context.driver = webdriver.Chrome(service=service, options=options)
def after_scenario(context,driver):
    context.driver = webdriver.Chrome(service=service, options=options)
def after_step(context,step):
    print()
