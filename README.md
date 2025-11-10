# 🌦️ AccuWeather Forecast Scraper

A simple **Python script** that scrapes the AccuWeather World Weather page to fetch the **current weather forecast** for multiple nearby locations.

---

## 📝 Description

This project uses `requests` to fetch web content, `BeautifulSoup` to parse the HTML data, and `tabulate` to format a text-based report.

The script extracts the following information for several locations:
- 🌍 **City Name** 
- 🌡️ **Current Temperature (°C)** 
- ☁️ **Current Weather Condition** (e.g., *Sunny*, *Cloudy*, *Rain*) 

The script saves the compiled data into two distinct files:
1.  **`output.txt`**: A human-readable report formatted as a table.
2.  **`output.json`**: A machine-readable JSON file.

---

## ⚙️ Requirements

The main dependencies are `requests`, `beautifulsoup4`, and `tabulate`. All required dependencies are listed in **`requirements.txt`**.

Install them with:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
To run the script, execute the main.py file from your terminal:
```bash
python main.py
```
This will execute the scraper, which will then generate or overwrite the output.txt and output.json files in the project's root directory.
## 📄 Output Files
The script generates two files:

### 1. output.txt
A human-readable text file containing the forecast formatted as a table.
Example:
Popular Cities Forecast
Date: 10/11/2025
============================================================
| City         |   Temperature (°C) | Condition           |
|--------------|--------------------|---------------------|
| Beijing      |                  5 | Sunny               |
| Berlin       |                  7 | Mostly Cloudy       |
| Buenos Aires |                 20 | Clear               |
| Cairo        |                 20 | Partly Cloudy       |
...
============================================================

### 2. output.json
A machine-readable JSON file containing the same data, structured with a title, date, and a list of city objects.

Example:
```bash
{
  "title": "Popular Cities Forecast",
  "date": "10/11/2025",
  "cities": [
    {
      "city": "Beijing",
      "temp": 8,
      "condition": "Sunny"
    },
    {
      "city": "Berlin",
      "temp": 8,
      "condition": "Cloudy"
    },
    {
      "city": "Buenos Aires",
      "temp": 20,
      "condition": "Clear"
    },
    ...
  ]
}
```
