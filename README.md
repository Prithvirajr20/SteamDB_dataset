# SteamDB_dataset

# scrapedata Documentation

This function scrapes data from the SteamDB charts page using Selenium and BeautifulSoup, and returns a Pandas DataFrame containing the collected data.

## Parameters

This function does not accept any parameters.

## Returns

- `df`: Pandas DataFrame
    - A DataFrame containing the scraped data from the SteamDB charts page.

## Dependencies

- `pandas` (imported as `pd`): For creating and manipulating DataFrames.
- `requests`: For accessing web pages (currently not used).
- `selenium.webdriver`: For handling dynamic websites.
- `selenium.webdriver.common.by`: For locating elements by various strategies.
- `selenium.common.exceptions.NoSuchElementException`: For handling exceptions.
- `bs4.BeautifulSoup`: For parsing HTML.
- `time`: For introducing pauses in the script.

## Usage

```python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

def scrapedata():
    # Function body here...

# Example usage:
data_frame = scrapedata()
print(data_frame.head())



Description
The function initializes a WebDriver using Chrome to interact with the SteamDB charts page.
It waits for the page to load completely using a pause of 2 seconds.
The function then maximizes the window to ensure full visibility of the page.
Using BeautifulSoup, it extracts the header of the table from the HTML.
It creates an empty DataFrame with the extracted header.
It iterates through the pages of the table, extracting data row by row and appending it to the DataFrame.
During navigation through the pages, it handles the NoSuchElementException to locate and click on the next page button.
Once all pages are collected, the function quits the WebDriver and returns the populated DataFrame.
Exceptions
If unable to find any of the required elements on the page, it raises a NoSuchElementException.
If unable to access the SteamDB charts page, it may raise other exceptions related to WebDriver or network issues.
Limitations
Relies on specific XPath for locating elements, which may break if the HTML structure changes.
Assumes a certain structure of the table on the SteamDB charts page.
Note
Ensure that the Chrome WebDriver is compatible with your Chrome browser version.
Install required dependencies (selenium, beautifulsoup4, pandas) before using the function.
Run the function with a stable internet connection to avoid network issues.
