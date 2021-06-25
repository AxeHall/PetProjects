import psycopg2
import os
import requests
from bs4 import BeautifulSoup

""" user = input('Введите название пользователя БД: ')
password = input('Введите пароль от БД: ')

db = 'uzum'
try:
    connection = psycopg2.connect(dbname= db,
                                  user= user,
                                  password= password,
                                  host= 'localhost')

except psycopg2.OperationalError:
    os.system(f"psql -U {user} -c 'CREATE DATABASE {db};' -W")
    connection = psycopg2.connect(dbname= db,
                                  user= user,
                                  password= password,
                                  host= 'localhost')

cursor = connection.cursor()

create_table_cmd = '''CREATE TABLE globus(
    id SERIAL PRIMARY KEY, 
    product_name VARCHAR(50),
    price INT,
    articul VARCHAR(15),
    pictures VARCHAR
)'''

cmd_1 = '''INSERT INTO globus(product_name, price, articul, pictures) VALUES '''

cursor.execute(create_table_cmd)
connection.commit() """

""" 

GLOBUS_URL = 'https://globus-online.kg/catalog/konditerskie_izdeliya/'

def get_html(url):
    r = requests.get(url)
    print(r.status_code)
    return r.text

html = get_html(GLOBUS_URL)

with open('/home/akzhol/Desktop/practic/parsers/globus/globus_page.html', 'w') as file:
    file.write(html)

def extract_data_pictures(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'list-showcase__inner js-element__shadow')
    pictures_list = list()
    for block in items:
        image_block = block.find('div', class_ = 'list-showcase__picture')
        try:
            image = image_block.img['data-src']
            pictures_list.append('https://globus-online.kg/' + image)
        except KeyError:
            pictures_list.append('kartinki net')
    return pictures_list
pictures = extract_data_pictures(html)
print(pictures)


def extract_data_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'list-showcase__inner js-element__shadow')
    name_list = list()
    for block in items:
        name_block = block.find('div', class_ = 'list-showcase__name')
        names = name_block.a
        name = names.text
        name_list.append(name)
    return name_list        
name = extract_data_name(html)

def extract_data_price(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'list-showcase__inner js-element__shadow')
    price_list = list()
    for block in items:
        prices_block = block.find('div', class_ = 'list-showcase__prices')
        price = prices_block.find('span', class_ = "c-prices__value js-prices_pdv_ГЛОБУС Розничная")
        price = price.text
        for i in price.split(' '):
            if i.isdigit():
                price_list.append(i)        
    return price_list
price = extract_data_price(html)

def extract_data_articul(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'list-showcase__inner js-element__shadow')
    articul_list = list()
    for block in items:
        art_block = block.find('div', class_ = 'list-showcase__article')
        articul = art_block.b
        articul = articul.text
        articul_list.append(articul)
    return articul_list
articul = extract_data_articul(html) """
""" 
for i in range(10):
    cmd_1 += f'({name}\', {price}, {articul}, {pictures})'
cmd_1 = cmd_1[:-1] + ';'

cursor.execute(cmd_1)
connection.commit()
connection.close() """
""" import pathlib
import os """

""" a = pathlib.Path(__file__)
a = str(a).split('/')
c = "/".join(a[0:-1])
a = pathlib.Path(c + '/images')
print(a) """
""" d = "https://freehtml5.co/download/?item=multipurpose-free-fully-responsive-website-template-with-cta"
os.system(f'wget {d} -P images/hous34') """



