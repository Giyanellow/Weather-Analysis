""" 
What to find:
1. Date
2. Temeperature (High and Low)
3. Condition
4. Precipitation Probability
5. Real Feel
6. Real Feel Shade
7. UV Index
8. Wind Speed
"""


import time
import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd


url = "https://www.accuweather.com/en/ph/baguio-city/1-262309_1_al/daily-weather-forecast/1-262309_1_al"


def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0'}
    request = requests.get(url, headers=headers)
    status = request.status_code
    if status == 200:
        scrape(request)

    
def scrape(request):
    soup = BeautifulSoup(request.content, "html.parser")
    title = soup.find("title").text
    print(title)
    
    card_class = "daily-wrapper"
    to_scrape = {
        "date": "date",
        "high": "high",
        "low": "low",
        "precipitation": "precipitation",
        "condition" : "phrase"
    }
    divs = soup.find_all("div", class_=card_class)
    
    for div in divs:
        data = {}
        for key, value in to_scrape.items():
            try:
                element = div.find("span", class_=value)
                if element:
                    data[key] = element.text
                else:
                    data[key] = div.find("div", class_=value).text
            except:
                data[key] = "N/A"
        print(data)
        print("\n")
    
if __name__ == "__main__":
    main()