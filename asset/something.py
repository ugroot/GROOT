from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
import time



def anything(lol):
    print(lol)
    #Taking input from user
    lo1=lol
    email=input('Enter your Email/User_name:   ')
    password=getpass.getpass('Enter your password:    ')
    print('Dont worry we dont save you password...may be we could :)')

    #connecting firefox webdriver
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("https://www.facebook.com/")

    #finding email and password box
    username = driver.find_element_by_id("email")
    password1 = driver.find_element_by_id("pass")

    #passing email and password to box
    username.send_keys(email)
    password1.send_keys(password)

    #clicking login button
    driver.find_element_by_id("loginbutton").click()
