import re
from sys import path
from bs4.builder import HTML
import requests
import time
from bs4 import BeautifulSoup
import psycopg2
import pathlib

REDFIN_URL = "https://www.redfin.com/city/2672/IN/Carmel"
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "Referer": "https://www.redfin.com/",
    "Upgrade-Insecure-Requests": "1",
    "Content-Type": "text/plain;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
}


class Redfin(object):
    def __init__(self, url):
        self.url = url

    def get_html(self, url):
        r = requests.get(url=url, headers=HEADERS)
        if r.status_code == 200:
            time.sleep(3)
            return r.text
        else:
            print(r.status_code)
            return 0

    def main_page(self):
        html = self.get_html(self.url)
        BASE_DIR = pathlib.Path(__file__).parent
        pathes = BASE_DIR.joinpath('images')
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pairs_block = soup.find_all(
                "div", class_="HomeCardContainer selectedHomeCard"
            )
            for pair in pairs_block:
                pairs = pair.find_all("div", class_="scrollable")
                for item in pairs:
                    article_houses = "https://www.redfin.com" + item.a["href"]
                    folder_name = "/" + article_houses.split("/")[5]
                    article_houses_html = self.get_html(article_houses)
                    if article_houses_html:
                        houses_soup = BeautifulSoup(article_houses_html, "html.parser")
                        images_block = houses_soup.find_all(
                            "div",
                            class_="InlinePhotoPreview Section pos-rel ThreePhotos",
                        )
                        for images_class in images_block:
                            images_link = images_class.find_all("span")
                            for images in images_link:
                                image = images.img["src"]
                                image_name = image.split("/")
                                path = pathes.joinpath(folder_name)
                                with open(image_name[-1], "w") as f:
                                    f.write(image)

                                
                    else:
                        continue
        return "Oshibka"


"""     def get_number_of_pages(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.find("div", class_ = "PagingControls")
            number_of_page = pagination.text
            return int(number_of_page[-1])
        else:
            return 0 """


redfin = Redfin(REDFIN_URL)
redfin.main_page()
""" redfin.get_html() """
""" try:
     pages = redfin.get_number_of_pages()
     for page in range(1, int(pages)):
         generator = redfin.main_page(page)
except requests.exceptions.ConnectionError:
    print("Нет интернета!") """

""" html_page = redfin.get_html(REDFIN_URL)
with open("./redfin.html", "w") as f:
    f.write(html_page) """


""" html = redfin.get_html(REDFIN_URL)
with open("./redfin.html", "w") as f:
    f.write(html) """
