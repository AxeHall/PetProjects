import os
import psycopg2
import requests
from bs4 import BeautifulSoup

SITE_URL = "https://freehtml5.co/"

class Freehtml(object):
    def __init__(self, url):
        self.url = url
    
    def get_html(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return 0
        
    def main_paige(self, page):
        html = self.get_html(f'https://freehtml5.co/page/{page}/')
        
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pairs_block = soup.find_all("main", class_ = "site-main card-deck row")
            
            for pair in pairs_block:

                pairs = pair.find_all("div", "col-sm-12 col-md-6 col-lg-4")
                pictures = ""
                header = ""
                publication_date = ""
                downloads = ""
                views = ""
                for item in pairs:
                    pictures = "".join(item.img["src"])
                    header = "".join(item.div.h2.a.text)
                    publication_date = "".join(item.div.div.p.small.text.replace(",", "").split(" ")[1:4])
                    downloads_views_block = item.find_all("p", class_ = "card-text hits")
                    
                    for downloads_views_item in downloads_views_block:
                        downloads_views_info = downloads_views_item.small.text
                        downloads_views = downloads_views_info.split("Downloads")
                        if len(downloads_views) == 2:
                            d_and_v = downloads_views[0].replace(" ", "").replace(",", ""), downloads_views[1].split(" ")[1].replace(",", "")
                            downloads = d_and_v[0]
                            views = d_and_v[-1]
                        else:
                            d_v = 0, downloads_views[0].split()[0].replace(",", "")
                            downloads = d_v[0]
                            views = d_v[-1]
                    article_link_description = item.a["href"]
                    article_definition_html = self.get_html(article_link_description)
                    text = ""
                    if article_definition_html:
                        definition_soup = BeautifulSoup(article_definition_html, "html.parser")
                        text_blocks = definition_soup.find_all("div", class_ = "entry-content")
                        for description in text_blocks:
                            before_index = description.text.index('Leave your vote')
                            text = "".join(description.text[0:before_index])
                            zips_articel_teg = description.find_all("div", class_ = 'single-demo-download')
                            for zips_articel_item in zips_articel_teg:
                                zips_articel = zips_articel_item.a["href"]
                                zips_articel_result = zips_articel.replace("/preview", "/download")
                                os.system(f'wget {zips_articel_result} -P files/')
                        else:
                            continue
                    else:
                        continue
                yield {"pictures": pictures, "header": header, "downloads": downloads, "views": views, "text": text, "publication_date": publication_date}
                   
        return "Oshibka"

    def get_number_of_pages(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.find("ul", class_="pagination")
            number_of_pages = pagination.text.split(" ")
           
            return number_of_pages[-2]
        return 0

freehtml = Freehtml(SITE_URL)

images = []
headers= []
downloads = []
publication_dates = []
views = []
texts = []

try:
    pages = freehtml.get_number_of_pages()
    for page in range(1, int(pages)):
        a = freehtml.main_paige(page)
      
        for i in a:
            images.append(i.get("pictures"))
            headers.append((i.get("header")))
            downloads.append(i.get("downloads"))
            publication_dates.append(i.get("publication_date"))
            views.append(i.get("views"))
            texts.append(i.get("text"))
except requests.exceptions.ConnectionError:
    print("Нет интернета!")


bd_password = input("Введите пароль от Базы Данных: ")

conn = psycopg2.connect(
    dbname='postgres', 
    user='postgres', 
    password=bd_password, 
    host='localhost'
)

cursor = conn.cursor()

cursor.execute('''CREATE TABLE freehtml(
    id SERIAL PRIMARY KEY, 
    image VARCHAR(200) NOT NULL, 
    header VARCHAR(80) NOT NULL, 
    downloads INT, 
    views INT, 
    text TEXT);'''
)

query = '''INSERT INTO freehtml(image, header, downloads, views, text) VALUES '''
for index in range(len(images)):
    query += f'(\'{images[index]}\', \'{headers[index]}\', \'{downloads[index]}\', \'{views[index]}\', \'{texts[index]}\'),'

sql_query = query[:-1] + ";"

cursor.execute(sql_query)
conn.commit()

cursor.close()
conn.close()