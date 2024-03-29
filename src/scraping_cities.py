import requests
import src.utils as utils
from bs4 import BeautifulSoup
from os.path import exists


def get():
    if not exists("data/cities.json"):
        print("→ data/cities.json does not exist, creating it ...")
        cities = {}
        base_url = "https://be.welipro.com/v?page="
        for i in range(1, 1001):
            url = base_url + str(i)
            req = requests.get(url)
            res = BeautifulSoup(req.text, 'html.parser')
            if res.find("div") is None:
                break
            else:
                list = res.find("div", class_="content")
                for item in list.find_all("a"):
                    city_name = item.text
                    city_url = item.get("href")
                    if city_name.__len__() > 1:
                        cities |= {city_name.strip(
                            ' '): city_url + "?page="}
        utils.write("data/cities.json", cities)
        print("→ " + str(cities.__len__()) +
              " cities saved in data/cities.json.")
        return utils.load("data/cities.json")
    else:
        print("→ data/cities.json is already created.")
        return utils.load("data/cities.json")
