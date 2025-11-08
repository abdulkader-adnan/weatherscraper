import requests
from bs4 import BeautifulSoup
import re

def get_forecast_data():
    url = 'https://www.accuweather.com/en/world-weather'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
               ,'cookie': 'awx_user=tp:C'}
    
    response = requests.get(url, headers=headers)

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        resorts = soup.find('div', class_='nearby-locations content-module')
        
        re_cities = r'">([\w\s]+)<\/span>'
        cities = re.findall(re_cities, str(resorts))


        re_temps = r'">(\+?|\-?\d+)\W+</span>'
        temps = re.findall(re_temps, str(resorts))
        temps = [int(temp) for temp in temps]

        svgs_elements = resorts.find_all('svg', attrs={'class':'icon'})
        svg_src = [tag['data-src'] for tag in svgs_elements if 'data-src' in tag.attrs]
        conditions_numbers = [re.search(r'(\d+)', cond).group(1) for cond in svg_src]
        accuweather_icon_map = {1:"Sunny",2:"Mostly Sunny",3:"Partly Sunny",4:"Intermittent Clouds",5:"Hazy Sunshine",6:"Mostly Cloudy",7:"Cloudy",8:"Dreary (Overcast)",11:"Fog",12:"Showers",13:"Mostly Cloudy w/ Showers",14:"Partly Sunny w/ Showers",15:"T-Storms",16:"Mostly Cloudy w/ T-Storms",17:"Partly Sunny w/ T-Storms",18:"Rain",19:"Flurries",20:"Mostly Cloudy w/ Flurries",21:"Partly Sunny w/ Flurries",22:"Snow",23:"Mostly Cloudy w/ Snow",24:"Ice",25:"Sleet",26:"Freezing Rain",29:"Rain and Snow",30:"Hot",31:"Cold",32:"Windy",33:"Clear",34:"Mostly Clear",35:"Partly Cloudy",36:"Intermittent Clouds",37:"Hazy Moonlight",38:"Mostly Cloudy",39:"Partly Cloudy w/ Showers",40:"Mostly Cloudy w/ Showers",41:"Partly Cloudy w/ T-Storms",42:"Mostly Cloudy w/ T-Storms",43:"Mostly Cloudy w/ Flurries",44:"Mostly Cloudy w/ Snow"}
        conditions = [accuweather_icon_map[int(num)] for num in conditions_numbers]

        data = zip(cities, temps, conditions)

        return data
    return False



print(list(get_forecast_data()))