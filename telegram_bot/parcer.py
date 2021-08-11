

import os
import json
from bs4.element import SoupStrainer
from pathlib import Path
from data_base import Postgres
from bs4 import BeautifulSoup

SITE_URL = "https://mypizza.kg/"
PATH = str(Path(__file__).parent)

""" os.system("wget -r -k -l 7 -p -E -nc https://mypizza.kg/") """

class Menu(object):
    def __init__(self, path):
        self.PATH = path
    
    def breakfast(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "breakfast" not in list_of_tables:
            postgres.create_table_breakfast()

        with open(f"{self.PATH}/mypizza.kg/Menu/Category/{page}.html", "r") as f:
            menu = f.read()
            
        x1 = menu.find("categoryController.init")
        x2 = menu.find("function isNumberKey(evt)")
        all_breakfast_line = menu[x1+len("categoryController.init")+1:x2].replace("\n", "")
        x3 = all_breakfast_line.find("document")
        all_breakfast_info =all_breakfast_line[0:x3-17]
        breakfast_information = json.loads(all_breakfast_info)
        breakfast_names = []
        breakfast_pictures = []
        breakfast_prices = []
        breakfast_pictures_directory = self.PATH + "/images/breakfasts"
        for item in breakfast_information:
            breakfast_names.append(item.get("Name"))
            breakfast_prices.append(int(item.get("Price")))
            pictures_values = item.get("PicturePath")
            pictures_link = "\'" + pictures_values + "\'"
            image_name = pictures_values.replace(" ", "_").split("/")
            breakfast_pictures.append(breakfast_pictures_directory + "/" + image_name[-1])
            os.system(f"wget -c -P {breakfast_pictures_directory} {pictures_link}")

        yield {"breakfast_name": tuple(breakfast_names), "breakfast_price": tuple(breakfast_prices), "breakfast_image": tuple(breakfast_pictures)}


    def pizza_40(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "pizza_40_cm" not in list_of_tables:
            postgres.create_table_pizza_40_cm()
        with open(f"{self.PATH}/mypizza.kg/Menu/Category/{page}.html", "r") as f:
            menu = f.read()
        x1 = menu.find("categoryController.init")
        x2 = menu.find("function isNumberKey(evt)")
        all_pizza_line = menu[x1+len("categoryController.init")+1:x2].replace("\n", "")
        x3 = all_pizza_line.find("document")
        all_breakfast_info =all_pizza_line[0:x3-17]
        pizza_information = json.loads(all_breakfast_info)
        pizza_names = []
        pizza_pictures = []
        pizza_prices = []
        pizza_pictures_directory = self.PATH + "/images/pizza_40cm"
        for item in pizza_information:
            pizza_names.append(item.get("Name"))
            pizza_price_values = item.get("Price")
            if len(str(pizza_price_values)) > 5:
                pizza_prices.append(0)
            else:
                pizza_prices.append(int(pizza_price_values))
            pizza_pictures_values = item.get("PicturePath")
            pizza_pictures_link = "\'" + pizza_pictures_values + "\'"
            pizza_image_name = pizza_pictures_values.replace(" ", "_").split("/")
            pizza_pictures.append(pizza_pictures_directory + "/" + pizza_image_name[-1])
            os.system(f"wget -c -P {pizza_pictures_directory} {pizza_pictures_link}")

        yield {"pizza_name": tuple(pizza_names), "pizza_price": tuple(pizza_prices), "pizza_image": tuple(pizza_pictures)}

    
    def rolly(self, page):

        list_of_tables = postgres.get_list_of_tables()

        if "rolly" not in list_of_tables:
            postgres.create_table_rolly()

        with open(f"{self.PATH}/mypizza.kg/Menu/Category/{page}.html", "r") as f:
            menu = f.read()
        x1 = menu.find("categoryController.init")
        x2 = menu.find("function isNumberKey(evt)")
        all_rollys_line = menu[x1+len("categoryController.init")+1:x2].replace("\n", "")
        x3 = all_rollys_line.find("document")
        all_rollys_info =all_rollys_line[0:x3-17]
        rollys_information = json.loads(all_rollys_info)
        rolly_names = []
        rolly_pictures = []
        rolly_prices = []
        rolly_pictures_directory = self.PATH + "/images/rolly"
        for item in rollys_information:
            rolly_names.append(item.get("Name"))
            rolly_prices.append(int(item.get("Price")))
            rolly_pictures_values = item.get("PicturePath")
            rolly_pictures_link = "\'" + rolly_pictures_values + "\'"
            rolly_image_name = rolly_pictures_values.replace(" ", "_").split("/")
            rolly_pictures.append(rolly_pictures_directory + "/" + rolly_image_name[-1])
            os.system(f"wget -c -P {rolly_pictures_directory} {rolly_pictures_link}")
        
        yield {"rolly_name": rolly_names, "rolly_price": rolly_prices, "rolly_image": rolly_pictures}

    def salaty(self, page):
        
        list_of_tables = postgres.get_list_of_tables()

        if "salaty" not in list_of_tables:
            postgres.create_table_salaty()

        with open(f"{self.PATH}/mypizza.kg/Menu/Category/{page}.html", "r") as f:
            menu = f.read()
        x1 = menu.find("categoryController.init")
        x2 = menu.find("function isNumberKey(evt)")
        all_salaty_line = menu[x1+len("categoryController.init")+1:x2].replace("\n", "")
        x3 = all_salaty_line.find("document")
        all_salaty_info =all_salaty_line[0:x3-17]
        salaty_information = json.loads(all_salaty_info)
        salaty_names = []
        salaty_pictures = []
        salaty_prices = []
        salaty_pictures_directory = self.PATH + "/images/salaty"
        for item in salaty_information:
            salaty_names.append(item.get("Name"))
            salaty_prices.append(int(item.get("Price")))
            salaty_pictures_values = item.get("PicturePath")
            salaty_pictures_link = "\'" + salaty_pictures_values + "\'"
            salaty_image_name = salaty_pictures_values.replace(" ", "_").split("/")
            salaty_pictures.append(salaty_pictures_directory + "/" + salaty_image_name[-1])
            os.system(f"wget -c -P {salaty_pictures_directory} {salaty_pictures_link}")
            
        yield {"salaty_name": salaty_names, "salaty_price": salaty_prices, "salaty_image": salaty_pictures}


    def zakuski(self, page):

        list_of_tables = postgres.get_list_of_tables()

        if "zakuski" not in list_of_tables:
            postgres.create_table_zakuski()

        with open(f"{self.PATH}/mypizza.kg/Menu/Category/{page}.html", "r") as f:
            menu = f.read()
        x1 = menu.find("categoryController.init")
        x2 = menu.find("function isNumberKey(evt)")
        all_zakuski_line = menu[x1+len("categoryController.init")+1:x2].replace("\n", "")
        x3 = all_zakuski_line.find("document")
        all_zakuski_info =all_zakuski_line[0:x3-17]
        zakuski_information = json.loads(all_zakuski_info)
        zakuski_names = []
        zakuski_pictures = []
        zakuski_prices = []
        zakuski_pictures_directory = self.PATH + "/images/zakuski"
        for item in zakuski_information:
            zakuski_names.append(item.get("Name"))
            zakuski_prices.append(int(item.get("Price")))
            zakuski_pictures_values = item.get("PicturePath")
            zakuski_pictures_link = "\'" + zakuski_pictures_values + "\'"
            zakuski_image_name = zakuski_pictures_values.replace(" ", "_").split("/")
            zakuski_pictures.append(zakuski_pictures_directory + "/" + zakuski_image_name[-1])
            os.system(f"wget -c -P {zakuski_pictures_directory} {zakuski_pictures_link}")
        
        yield {"zakuski_name": zakuski_names, "zakuski_price": zakuski_prices, "zakuski_image": zakuski_pictures}


class Shares(object):

    def shares(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "shares" not in list_of_tables:
            postgres.create_table_shares()

        PATH = str(Path(__file__).parent)
        with open(f"{PATH}/mypizza.kg/Shares/ShareItem/{page}.html", "r") as f:
            html = f.read()
        
        shares_soup = BeautifulSoup(html, "html.parser")
        content_block = shares_soup.find_all("div", class_ = "c-content")
        pictures = []
        title = []
        description = []
        shares_pictures_path = PATH + "/images/shares"
        for item in content_block:
            title.append(item.h1.text)
            description.append(item.p.text)
            shares_pictures_link = item.img["src"]
            os.system(f"wget -c -P {shares_pictures_path}  {shares_pictures_link}")
            shares_name = shares_pictures_link.split("=")
            pictures.append(shares_pictures_path + "/" + shares_name[-1])
        yield {"share_title": title, "share_description": description, "share_pictures": pictures}

    
class About_company(object):

    def about(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "about" not in list_of_tables:
            postgres.create_table_about()

        PATH = str(Path(__file__).parent)
        with open(f"{page}", "r") as f:
            html = f.read()
        
        about_soup = BeautifulSoup(html, "html.parser")
        content_block = about_soup.p
        about_text = content_block.text
        yield about_text


class Vacancies(object):

    def jobs(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "jobs" not in list_of_tables:
            postgres.create_table_jobs()

        PATH = str(Path(__file__).parent)
        with open(f"{PATH}/mypizza.kg/Vacancies/VacancyItem/{page}.html", "r") as f:
            html = f.read()
        
        jobs_soup = BeautifulSoup(html, "html.parser")
        content_block = jobs_soup.find_all("div", class_ = "c-vacancy")
        jobs_names = []
        description = []
        for item in content_block:
            jobs_names.append(item.div.text)
            text_line = item.find_all("div", class_ = "c-content__text")
            for texts in text_line:
                description.append(texts.text.replace("\r", "").replace("\n", "").replace("  ", ""))
            
        yield {"jobs_name": jobs_names, "theme": description}



if __name__ == "__main__":
    dbname = input("The name of database: ")
    dbuser = input("Username of database: ")
    dbpswd = input(f"{dbuser}'s password: ")

    postgres = Postgres(db_name=dbname, user=dbuser, pswd=dbpswd)

    """ mypizza_menu = Menu(PATH)
    breakfast_name = []
    breakfast_price = []
    breakfast_image = []

    for breakfast_item in mypizza_menu.breakfast(4354):
        for name in breakfast_item.get("breakfast_name"):
            breakfast_name.append(name)
        for price in breakfast_item.get("breakfast_price"):
            breakfast_price.append(price)
        for image in breakfast_item.get("breakfast_image"):
            breakfast_image.append(image)
    

    for i in range(len(breakfast_name)):
        values = f'(\'{breakfast_name[i]}\', \'{breakfast_image[i]}\', {breakfast_price[i]})'
        postgres.breakfast_insert_data(values)

    pizza_40_name = []
    pizza_40_price = []
    pizza_40_image = []

    for pizza_item in mypizza_menu.pizza_40(4372):
        for name in pizza_item.get("pizza_name"):
            pizza_40_name.append(name)
        for price in pizza_item.get("pizza_price"):
            pizza_40_price.append(price)
        for image in pizza_item.get("pizza_image"):
            pizza_40_image.append(image)

    for i in range(len(pizza_40_name)):
        values = f'(\'{pizza_40_name[i]}\', \'{pizza_40_image[i]}\', {pizza_40_price[i]})'
        postgres.pizza_40_cm_insert_data(values)

    rolly_name = []
    rolly_price = []
    rolly_image = []

    for rolly_item in mypizza_menu.rolly(4365):
        for name in rolly_item.get("rolly_name"):
            rolly_name.append(name)
        for price in rolly_item.get("rolly_price"):
            rolly_price.append(price)
        for image in rolly_item.get("rolly_image"):
            rolly_image.append(image)

    for i in range(len(rolly_name)):
        values = f'(\'{rolly_name[i]}\', \'{rolly_image[i]}\', {rolly_price[i]})'
        postgres.rolly_insert_data(values)

    salaty_name = []
    salaty_price = []
    salaty_image = []

    for salaty_item in mypizza_menu.salaty(4358):
        for name in salaty_item.get("salaty_name"):
            salaty_name.append(name)
        for price in salaty_item.get("salaty_price"):
            salaty_price.append(price)
        for image in salaty_item.get("salaty_image"):
            salaty_image.append(image)

    for i in range(len(salaty_name)):
        values = f'(\'{salaty_name[i]}\', \'{salaty_image[i]}\', {salaty_price[i]})'
        postgres.salaty_insert_data(values)

    zakuski_name = []
    zakuski_price = []
    zakuski_image = []

    for zakuski_item in mypizza_menu.zakuski(4356):
        for name in zakuski_item.get("zakuski_name"):
            zakuski_name.append(name)
        for price in zakuski_item.get("zakuski_price"):
            zakuski_price.append(price)
        for image in zakuski_item.get("zakuski_image"):
            zakuski_image.append(image)

    for i in range(len(zakuski_name)):
        values = f'(\'{zakuski_name[i]}\', \'{zakuski_image[i]}\', {zakuski_price[i]})'
        postgres.zakuski_insert_data(values)

    shares_pages = [1014, 1017, 1018, 1019, 5146, 6161, 6163, 6164, 6168, 6172]
    mypizza_shares = Shares()
    shares_title = []
    shares_image = []
    shares_decription = []
    for share_page in shares_pages:
        for shares_item in mypizza_shares.shares(share_page):
            for title in shares_item.get("share_title"):
                shares_title.append(title)
            for image in shares_item.get("share_pictures"):
                shares_image.append(image)
            for description in shares_item.get("share_description"):
                shares_decription.append(description)

    for i in range(len(shares_title)):
        values = f'(\'{shares_title[i]}\', \'{shares_image[i]}\', \'{shares_decription[i]}\')'
        postgres.shares_insert_data(values)

    mypizza_about = About_company()
    for about_info in mypizza_about.about(f'{PATH}/mypizza.kg/Company/About.html'):
        values = f'(\'{about_info}\')'
        postgres.about_insert_data(values)
    
    
    jobs_pages = [10, 11]
    mypizza_jobs = Vacancies()
    jobs_name = []
    jobs_theme = []
    for page in jobs_pages:
        for jobs_item in mypizza_jobs.jobs(page):
            for vacancie in jobs_item.get("jobs_name"):
                jobs_name.append(vacancie)
            for theme in jobs_item.get("theme"):
                jobs_theme.append(theme)
    for i in range(len(jobs_name)):
        values = f'(\'{jobs_name[i]}\', \'{jobs_theme[i]}\')'
        postgres.jobs_insert_data(values) """


    postgres.end()

