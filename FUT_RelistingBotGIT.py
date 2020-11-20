from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException 
import chromedriver_binary
import time
import random
import threading
import unidecode
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as EX
from time import sleep


def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

PATH = "C:\Program Files (x86)\chromedriver.exe"

def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timeformat = '[WAIT] {:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		sleep(1)
		t -= 1

#driver = webdriver.Chrome(PATH) # put destination to your chromedriver here.
driver = webdriver.Chrome(ChromeDriverManager().install())

def getcode():
    print("yup")
    windows = driver.window_handles
    time.sleep(2)
    driver.switch_to.window(windows[0])
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    s = driver.current_url
    time.sleep(4)
    #sign in
    driver.find_element_by_xpath("/html/body/header/div/aside/div/nav/ul/li[2]").click()
    # put in email and password
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("your_hotmail_address") # user for hotmail
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input").click()
    # put in password
    time.sleep(5)
    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input").send_keys("your_password") #password for hotmail
    time.sleep(3)

    driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input").click()
    #click on other tab
    
    #time.sleep(10)  
    #driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[1]/div/div[2]/div/div[1]/button[1]/span").click()
                                  
    #click on first email
    time.sleep(5)                     
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div").click()
    # read first email title and extract the code                              
    time.sleep(5) 
    for element in driver.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/div/span"):
        codex = element.text                      
        print(codex)
        code_num = ''.join([n for n in codex if n.isdigit()])
    print(code_num)
    return(code_num)
     
                    

def main():

    driver.get("https://www.easports.com/fifa/ultimate-team/web-app/")
    windows = driver.window_handles
    time.sleep(1)
    windowarr = []
    #driver.switch_to.window(windows[1])
    time.sleep(1)
    #driver.close()
    driver.switch_to.window(windows[0])
    time.sleep(13)
    driver.find_element_by_xpath("/html/body/main[1]/div[1]/div[1]/div[1]/button[1]").click()
    time.sleep(6)
    s = driver.current_url
    driver.get(s)
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[1]/div[1]/span[1]/span[1]/input[1]").send_keys("your_hotmail_address") # put in your hotmail
    driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[3]/div[1]/div[1]/div[1]/ul[1]/li[2]/div[1]/span[1]/span[1]/input[1]").send_keys("your_password") # put in your password.
    driver.find_element_by_id("btnLogin").click() 
    time.sleep(1)
    driver.find_element_by_id("btnSendCode").click()
    s = driver.current_url
    driver.get(s)
    time.sleep(1)
    driver.execute_script('''window.open("http://hotmail.com","_blank");''')
    windows = driver.window_handles
    print(windows)
    driver.switch_to.window(windows[0])
    soi = getcode()
    print(soi)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(random.randint(3,5))

    # enter code to EA sport
    driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/div/div/ul/li[1]/div/span[1]/span/input").send_keys(soi)
    time.sleep(10)
    driver.find_element_by_xpath("/html/body/div[2]/form/div[2]/div/div/div/div[2]/a[1]").click()

    
    #----------------------Repeat releisting several times

    for n in range(20):
        driver.switch_to.window(windows[0])
        time.sleep(3)
        #driver.refresh()
        #def click_transfers:
        print('[LOG] Clicking on Transfers')
        time.sleep(15)
        # goto transfers
        if driver.find_element_by_xpath("/html/body/main/section/nav/button[3]"):
            driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()
        else:
            time.sleep(60)
            driver.find_element_by_xpath("/html/body/main/section/nav/button[3]").click()

        time.sleep(random.randint(3,4))
        # goto transferlist
        driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div/div[3]/div[2]/div").click()
    
        time.sleep(random.randint(3,4))
                                  
        # press relist all

        
        for element in driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button"):
            driver.find_elements_by_xpath("/html/body/main/section/section/div[2]/div/div/div/section[2]/header/button").click()
            time.sleep(random.randint(2,3))

            # press yes
            driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[2]").click()
            print('[SUCCESS] Players relisted')

        # wait fo an hour
        countdown(3630+random.randint(1,10))


if __name__ == "__main__":
    main()