from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def clickButton(id) :
    try:
        bail = WebDriverWait(browser, 4).until(
            EC.presence_of_element_located((By.ID, id))
        )
    finally :
        bail.click()

username = 'user'
password = 'pass'

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get('https://192.168.1.1/')

usernameBox = browser.find_element('id', 'Frm_Username')
passwordBox = browser.find_element('id', 'Frm_Password')
loginButton = browser.find_element('id', 'LoginId')

usernameBox.send_keys(username)
passwordBox.send_keys(password)
loginButton.click()

clickButton('mgrAndDiag')
clickButton('devMgr')
clickButton('Btn_restart')
clickButton('confirmOK')
sleep(7)

browser.quit()
exit()
