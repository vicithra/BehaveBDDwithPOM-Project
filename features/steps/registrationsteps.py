import time

from behave import *

from Utilities import configReader
from features.pageobjects.RegistrationPage import RegistrationPage


@given(u'I navigate to qa.way2automation.com')
def step_impl(context):
    context.reg = RegistrationPage(context.driver)
    context.reg.openurl(configReader.readConfig("basic info","testsiteurl"))


@when(u'I enter the name as "{name}"')
def step_impl(context,name):
    context.reg.setname(name)
    time.sleep(5)

@then(u'I enter the phone number as "{phonenumber}"')
def step_impl(context,phonenumber):
    context.reg.setphnum(phonenumber)

@then(u'I enter the mailID as "{email}"')
def step_impl(context,email):
    context.reg.setmail(email)
@then(u'I select the city as "{city}"')
def step_impl(context,city):
    context.reg.setcity(city)
@then(u'I enter the country as "{country}"')
def step_impl(context,country):
    context.reg.setcountry(country)

@then(u'I enter the username as "{username}"')
def step_impl(context,username):
    context.reg.setusername(username)
    time.sleep(2)

@then(u'I enter the password as "{password}"')
def step_impl(context,password):
    context.reg.setpassword(password)

@then(u'I click the submit button')
def step_impl(context,password):
    context.reg.submitform()
    time.sleep(5)


