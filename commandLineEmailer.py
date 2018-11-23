# this program takes an
# email address
# a string of text
# and sends an email to the person from root account

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys

browser = webdriver.Safari()
browser.get("https://gmail.com")

print("Sending mail.....")

emailElem = browser.find_element_by_tag_name('input')
emailElem.send_keys('adminEmailAddress')
emailElem.send_keys(Keys.ENTER)

sleep(2)
passElem = browser.find_element_by_name('password')
passElem.send_keys('AdminPassword')
passElem.send_keys(Keys.ENTER)

sleep(20)
composeElem = browser.find_element_by_css_selector('div[gh="cm"]')
composeElem.click()

sleep(5)
emailTo = browser.find_element_by_css_selector('textarea.vO')
emailMessage = browser.find_element_by_css_selector('div[role="textbox"]')
emailTo.send_keys(sys.argv[1:2])
emailMessage.send_keys(sys.argv[2:])

sleep(1)
sendElem = browser.find_element_by_css_selector('div.aoO')
try:
    sendElem.send_keys(Keys.ENTER)
    print("Email sent successfully!")

    sleep(5)
    try:
        sigoutBox = browser.find_element_by_css_selector('span.gb_9a')
        sigoutBox.click()

        sleep(1)
        logoutElem = browser.find_element_by_css_selector('a#gb_71')
        logoutElem.click()
        print("Logged out successfully.")
    except:
        print("Error in loging out.")    

except:
    print("Sorry, Please try again!")    
