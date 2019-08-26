from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://play.typeracer.com')
time.sleep(3)
linkElem = driver.find_element_by_link_text('Enter a typing race')
linkElem.click()
time.sleep(3)
firstLetterElement = driver.find_element_by_xpath('//span[@unselectable="on"]')
letter = firstLetterElement.text
restOfWords = driver.find_elements_by_xpath('//span[@unselectable="on"]')
print(len(restOfWords))
stuffToType = ''
firstWord = ''
for x in range(0,len(restOfWords)-1):
    if len(restOfWords[0].text) == 1:
             firstWord+=restOfWords[x].text
print(firstWord)
for x in range(1,len(restOfWords)):
    stuffToType = firstWord + " " + restOfWords[x].text
print(stuffToType)
time.sleep(11)

inputBox = driver.find_element_by_class_name("txtInput")
inputBox.send_keys(stuffToType)
time.sleep(3)
try:
    beginTestButton = driver.find_element_by_class_name('gwt-Button')
    beginTestButton.click()
except:
    print("Disqualified")
