# Weather Analysis on Baguio Philippines (Jul. - Sept. 2024)

## Table of Contents

- [IMPORTANT](#important)
- [Introduction](#introduction)
- [Gathered Data / Dataset](#gathered-data--dataset)
- [Tools and Libraries](#tools-and-libraries)
- [Installation](#installation)
- [Conclusion](#conclusion)
- [License](#license)

## IMPORTANT

Do take into account that this Analysis is not a direct and accurate Analysis on Baguio, Philippines' weather patterns. This is an activity and is designed to showcase Web Scraping, Data Analysis, Cleanup, and Machine Learning techniques.

## Introduction

Welcome to the Weather Analysis project! In this project, we will explore and analyze weather patterns in Baguio, Philippines. By leveraging data analysis, cleanup, and machine learning techniques, we aim to gain insights into the weather trends and make predictions for future patterns.

Through this analysis, we will showcase the power of data-driven approaches in understanding and interpreting weather data. We will also highlight the importance of data preprocessing and feature engineering in preparing the dataset for analysis.

So let's dive in and uncover the fascinating world of Baguio's weather patterns!

## Gathered Data / Dataset
For this analysis, we used the BeautifulSoup library in Python to scrape weather data from an online weather website (Accuweather). We collected data for a period of 45 days to ensure a comprehensive dataset for analysis.

Using BeautifulSoup, we were able to extract various weather parameters such as temperature, humidity, wind speed, and precipitation for each day. The scraped data was then stored in a CSV file for further processing and analysis.

By leveraging web scraping techniques with BeautifulSoup, we obtained a rich and diverse dataset that captures the weather patterns in Baguio, Philippines over a 45-day period.

## Tools and Libraries

- [Jupyter Notebook](https://jupyter.org)
- [Visual Studio Code](https://code.visualstudio.com)
- [Python](https://www.python.org)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)
- [Seaborn](https://seaborn.pydata.org)
- [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)

_You can install the necessary libraries in the [Installation](Installation) section; but you will need to have [Visual Studio Code](https://code.visualstudio.com) installed already._

## Installation

To run the analysis locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/Giyanellow/Weather-Analysis
   ```

2. Move to main folder
   ```bash
   cd Weather-Analysis
   ```
3. Run scrape.py
   ```bash
   python scrape.py
   ```
4. Run ALL OF THE CELLS in clean.ipynb

You will need to run ```scrape.py``` and it manually scrapes all available data in Accuweather's Baguio webpage, however you will need to manually run all of the code cells in the Jupyter notebook.

See this [link](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) on how to run Jupyter notebooks on Vscode.

## Check out Interactive Dashboard (Optional)

To run the dashboard, follow these steps:

1. Move to dashboard folder

   ```bash
   cd dashboard
   ```
2. Run app.py

   ```bash
   python app.py
   ```

*This dashboard is an experimental feature...*

## Conclusion

In conclusion, this weather analysis project has provided valuable insights into the weather patterns in Baguio, Philippines. By leveraging data analysis, cleanup, and machine learning techniques, we were able to uncover trends and make conclusions about features and feature importance.

Through the use of web scraping with BeautifulSoup, we collected a comprehensive dataset that captured various weather parameters such as temperature, humidity, wind speed, and precipitation. This dataset served as the foundation for our analysis and allowed us to gain a deeper understanding of the weather patterns in Baguio.

The analysis highlighted the power of data-driven approaches in interpreting weather data and showcased the importance of data preprocessing and feature engineering. By applying these techniques, we were able to extract meaningful insights and make conclusions on what factors affect different aspects of weather.

Overall, this project demonstrates the value of data analysis in understanding and predicting weather patterns. It also emphasizes the significance of using the right tools and libraries such as Jupyter Notebook, Visual Studio Code, Python, Scikit-Learn, Pandas, NumPy, Matplotlib, and Seaborn.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
````
