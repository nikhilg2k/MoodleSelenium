from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH='C:\\Users\\nikhi\\Desktop\\Moodle1\\chromedriver.exe'
driver=webdriver.Chrome(PATH)
driver.get(r'https://moodle.iitd.ac.in/login/index.php')

#Function to solve captcha
def Captcha_Solver(captcha):
    l1=captcha.split()
    if l1[2]=='first':
        return l1[4]
    elif l1[2]=='second':
        return l1[6]
    elif l1[1]=='add':
        return str(int(l1[2])+int(l1[4]))
    else:
        return str(int(l1[2])-int(l1[4]))

#Try/Except to prevent loading error 
try:
    #Username
    username=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    #Input
    userin=input("Enter Username: ")
    username.send_keys(userin)

    #Password
    password=driver.find_element_by_id('password')

    #Input
    passin=input('Enter Password: ')
    password.send_keys(passin)

    #Captcha
    text= driver.find_element_by_id('login').text
    text=text.split('\n')
    captcha=text[3]
    answer=Captcha_Solver(captcha)
    captcha=driver.find_element_by_id('valuepkg3')
    captcha.clear()
    captcha.send_keys(answer)

    #Login
    login=driver.find_element_by_id('loginbtn')
    login.click()

#Exception
except:
    print('Error')
    #driver.quit()

#Wait for user to see
time.sleep(5)

#Quit
driver.quit()