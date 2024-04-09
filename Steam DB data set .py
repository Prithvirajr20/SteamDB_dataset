#!/usr/bin/env python
# coding: utf-8

# In[21]:


#lets import the required libraries
import pandas as pd #for data frames
import requests #for accessing the data
from selenium import webdriver # to handle dynamic  websites
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException #for handling exceptions errors
from bs4 import BeautifulSoup #soup for collecting the data
import time #time 

def scrapedata():
    url = 'https://steamdb.info/charts/' #let define the website

    #lets setup selenium webdriver to deal with dynamic websites
    driver = webdriver.Chrome() #setup the driver 
    driver.get(url) #it will open the site
    time.sleep(2) #as it will keep the chrome in idle to load the website completely

    driver.maximize_window() #will maximize the current window

    #lets setup the soup to collect the required information
    soup = BeautifulSoup(driver.page_source,'html.parser')
    table = soup.find('div',class_='dt-container',id='table-apps_wrapper')
    # print(table)
    header = [item.text for item in table.find_all('th')] #will collect the header only 
    print(header)
    df = pd.DataFrame(columns=header) #created a data frame to store the data
    for i in range(1,72): 
        soup = BeautifulSoup(driver.page_source,'html.parser')
        table = soup.find('div',class_='dt-container',id='table-apps_wrapper')
        row = [[item.text for item in row.find_all('td')]
              for row in table.find_all('tr',class_='app')]
        df1 = pd.DataFrame(row,columns=header)
        df = pd.concat([df,df1],ignore_index=True)

        #navigating through pages and handling exception erros as whenever raised
        time.sleep(2)
        try:
            next_button = driver.find_element(By.XPATH,'//*[@id="table-apps_wrapper"]/div[3]/div[2]/button[8]')
            next_button.click()
        except NoSuchElementException:
            try:
                nxt_button = driver.find_element(By.XPATH,'//*[@id="table-apps_wrapper"]/div[3]/div[2]/button[7]')
                nxt_button.click()
            except NoSuchElementException:
                print('None of the above button found')    
        print('page collected',i)    
    print('all page collected')
    driver.quit()#it closes the window
    return df


# In[22]:


df.to_csv(r'E:\Program\PowerBI\scrapped data\steamgames.csv')

