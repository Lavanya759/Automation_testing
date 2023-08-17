from selenium.webdriver import Chrome
# c=Chrome(executable_path=r"C:\Users\sloke\PycharmProjects\selenium\drivers\chromedriver.exe")
#or
# c=Chrome(executable_path="..\drivers\chromedriver.exe")


from selenium.webdriver import Edge
# e=Edge(executable_path=r"C:\Users\sloke\PycharmProjects\selenium\drivers\msedgedriver.exe")
#or
# e=Edge(executable_path="..\drivers\msedgedriver.exe")

from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
# option=Options()
# f=Firefox(executable_path="..\drivers\geckodriver.exe",options=option)

#Day2:
from time import sleep
# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# driver.back()
# driver.forward()
# driver.refresh()
# driver.close()

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# pos=driver.get_window_position()
# print(pos)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# siz=driver.get_window_size()
# print(siz)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# all=driver.get_window_rect()
# print(all)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# driver.set_window_size(100,100)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# driver.set_window_rect(90,20,100,100)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# atile=driver.title
# print(atile)

# driver=Chrome(executable_path="..\drivers\chromedriver.exe")
# driver.get("https://www.google.com")
# url=driver.current_url
# print(url)


# driver=Chrome(executable_path="../drivers/chromedriver.exe")
# driver.get("https://na.account.amazon.com/ap/signin?_encoding=UTF8&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.pape.max_auth_age=0&ie=UTF8&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=lwa&openid.assoc_handle=amzn_lwa_na&marketPlaceId=ATVPDKIKX0DER&arb=d956bccc-7692-4103-afd1-e5b2fb0ab83c&language=en_US&openid.return_to=https%3A%2F%2Fna.account.amazon.com%2Fap%2Foa%3FmarketPlaceId%3DATVPDKIKX0DER%26arb%3Dd956bccc-7692-4103-afd1-e5b2fb0ab83c%26language%3Den_US&enableGlobalAccountCreation=1&metricIdentifier=amzn1.application.e3b40bcf8dae40e6bf8b197b9b3dec8d&signedMetricIdentifier=b1rnnUP4iinb%2B%2BwjCOWA1f5Y%2B6DlINB%2BDQCz1Q54AtU%3D")
# mobile_num=driver.find_element("id","ap_email")
# mobile_num.send_keys("7598424267")
# acct=driver.find_element("class","a-button-input")
# acct.click()
