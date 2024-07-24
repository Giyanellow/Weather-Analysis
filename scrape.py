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
import re


url = "https://www.accuweather.com/en/ph/baguio-city/1-262309_1_al/daily-weather-forecast/1-262309_1_al"

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0'}
    request = requests.get(url, headers=headers)
    status = request.status_code
    if status == 200:
        weather_df = scrape(request)
    
    weather_df.to_csv("weather_data.csv", index=False)
        
    

    
def scrape(request):
    soup = BeautifulSoup(request.content, "html.parser")
    title = soup.find("title").text
    print(title)
    
    card_class = "daily-wrapper"
    to_scrape = {
        "date": "module-header sub date",
        "high": "high",
        "low": "low",
        "precipitation": "precip",
        "condition" : "phrase"
    }
    
    special_cases = {
        "real feel": "RealFeel®",
        "real feel shade": "RealFeel Shade™",
        "max uv index": "Max UV Index",
        "wind": "Wind"
    }
    divs = soup.find_all("div", class_=card_class)
    
    weather_data = []
    
    for div in divs:
        data = {}
        for key, value in to_scrape.items():
            try:
                if key == "precipitation":
                    element = div.find("div", class_=value)
                    if element:
                        data[key] = element.text.replace('\n', '').replace('\t', '').strip()
                    else:
                        data[key] = "N/A"
                    continue
                
                element = div.find("span", class_=value)
                if element:
                    data[key] = element.text.replace('\n', '').replace('\t', '').strip()
                else:
                    data[key] = div.find("div", class_=value).text
            except:
                data[key] = "N/A"
                print(f"Exception {key}: {value}")
                
        panel_items = div.find_all("p", class_="panel-item")        
        for item in panel_items:
            try:
                label = item.contents[0].strip()
                span = item.find("span", class_="value")
                if span:
                    for key, special_label in special_cases.items():
                        if special_label in label:
                            data[key] = span.text.strip()
                            break
            except Exception as e:
                print(f"Exception for special case in panel-item: {e}")
                
        weather_data.append(data)
        
    weather_df = pd.DataFrame(weather_data)
    return weather_df
    
if __name__ == "__main__":
    main()