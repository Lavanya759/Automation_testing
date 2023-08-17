#Assignment 1:In "https://demowebshop.tricentis.com/" write a script to click on register and fill all details and register from demo webshop
"""
from selenium.webdriver import Chrome
from time import sleep
driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element("class name","ico-register").click()
driver.find_element("id","gender-female").click()
driver.find_element("name","FirstName").send_keys("lavanya")
driver.find_element("name","LastName").send_keys("reddy")
driver.find_element("id","Email").send_keys("lavanyasreddy214@gmail.com")
driver.find_element("name","Password").send_keys("Lavanyasreddy1@")
driver.find_element("id","ConfirmPassword").send_keys("Lavanyasreddy1@")
driver.find_element("name","register-button").click()
"""

#or

"""
from selenium.webdriver import Chrome
from time import sleep
def registration(lis,gen):
    driver=Chrome(executable_path="../drivers/chromedriver.exe")
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    driver.find_element("class name","ico-register").click()
    if gen=='boy':
        driver.find_element("id","gender-male").click()
    else:
        driver.find_element("id", "gender-female").click()
    driver.find_element("name","FirstName").send_keys(lis[0])
    driver.find_element("name","LastName").send_keys(lis[1])
    driver.find_element("id","Email").send_keys(lis[2])
    driver.find_element("name","Password").send_keys(lis[3])
    driver.find_element("id","ConfirmPassword").send_keys(lis[4])
    driver.find_element("name","register-button").click()
    sleep(10)
    driver.close()
boy=['lokesh','reddy','lokesh123@gmail.com','lok1234@','lok1234@']
girl=['lavanya','reddy','lavany217@gmail.co','Lavanyasreddy1@','Lavanyasreddy1@']
gender=input("enter")
registration(boy,gender) if gender=='boy' else registration(girl,gender)
"""


#Assignment 2: Launching of youtube and search for song and then play

"""
from selenium.webdriver import Chrome
from time import sleep
driver=Chrome(executable_path="../drivers/chromedriver.exe")
driver.get("http://www.youtube.com/")
driver.maximize_window()
driver.find_element("css selector","input[autocapitalize='none']").send_keys("na raja nuvve song")
driver.find_element("css selector","button[id='search-icon-legacy']").click()
sleep(3)
driver.find_element("css selector",'yt-formatted-string[class="style-scope ytd-video-renderer"]').click()
"""




