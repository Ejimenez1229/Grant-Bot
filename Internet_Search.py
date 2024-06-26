from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

###################################################################################################################################################################
## This the list of key words that the bot will search for, if you ever need to add more just add to the list
Search_words = ['Tester','Study']

## This is the minimum number of days from today that the grant will end that the bot is looking for, ex 30 means 30 days from today the grant will end 
Days_til = 90 

## This is the maximum number of days from the day the grant was posted (Added this incase you dont want old grants) Ex 365 means posted within the year 
Days_From = 365
####################################################################################################################################################################

##This is the website we are searching in 
for i in Search_words:
    service = Service(executable_path='chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.grants.gov/search-grants')

    ## Here we are waiting for the elements to show up, website to load 
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="inp-keywords"]'))
    )
    input_element = driver.find_element(By.XPATH, '//*[@id="inp-keywords"]')
    time.sleep(10)
    input_element.clear()
    ## input_element.send_keys("Test it out!" + Keys.ENTER)
    time.sleep(15)
    input_element.send_keys(i)

    ## Here I am only wanting active so I am unclicking 'Forecast'
    posted_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div/label')
    posted_element.click()


    ## Here I am only looking for Grants so I am only clicking Grants
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="m-a1"]/div/div[2]/div[2]/label'))
    )
    Grant_element = driver.find_element(By.XPATH, '//*[@id="m-a1"]/div/div[2]/div[2]/label')
    Grant_element.click()

    time.sleep(2) 

    ## Push the search button 
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="btn-search"]'))
    )
    Push_element = driver.find_element(By.XPATH, '//*[@id="btn-search"]')
    Push_element.click()

    time.sleep(5) 


    ## I am downloading the CSV 
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__nuxt"]/div[4]/div/div/div/div[2]/div[1]/div[2]/a'))
    )
    Dload_element = driver.find_element(By.XPATH, '//*[@id="__nuxt"]/div[4]/div/div/div/div[2]/div[1]/div[2]/a')
    Dload_element.click()

    time.sleep(10)
    ## driver.quit()
    time.sleep(30)
