# 🌦️ AccuWeather Forecast Scraper

A simple **Python script** that scrapes the AccuWeather World Weather page to fetch the **current weather forecast** for multiple nearby locations.

---

## 📝 Description

This project uses `requests` to fetch web content and `BeautifulSoup` to parse the HTML data.

The script extracts the following information for several locations:
- 🌍 **City Name**
- 🌡️ **Current Temperature (°C)**
- ☁️ **Current Weather Condition** (e.g., *Sunny*, *Cloudy*, *Rainy*)

All data is displayed in the console as a list of tuples.

---

## ⚙️ Requirements

The required dependencies are listed in **`requirements.txt`**.  
Install them with:

```bash
pip install -r requirements.txt
