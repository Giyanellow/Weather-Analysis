import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.accuweather.com/en/ph/baguio-city/1-262309_1_al/daily-weather-forecast/1-262309_1_al"

def main():
    if check_status(url):
        ...
    
    
def check_status(url):
    if requests.get(url) == 200:
        return True
    return False

def scrape(url):
    driver = webdriver.Chrome()
    driver.get(url)


if "__name__" == "__main__":
    main()