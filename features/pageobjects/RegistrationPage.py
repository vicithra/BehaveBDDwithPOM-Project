from features.pageobjects.BasePage import BasePage
class RegistrationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def openurl(self,url):
        self.driver.get(url)
    def setname(self,name):
        self.type("name_XPATH",name)
    def setphnum(self,phonenumber):
        self.type("phone_XPATH",phonenumber)
    def setmail(self,email):
        self.type("email_XPATH",email)
    def setcity(self,city):
        self.type("city_XPATH",city)
    def setcountry(self,country):
        self.select("country_XPATH",country)
    def setusername(self,username):
        self.type("username_XPATH",username)
    def setpassword(self,password):
        self.type("password_XPATH",password)
    def submitform(self):
        self.click("submit_XPATH")
