""" TOKEN = "1779909135:AAFbQegiPKYCylIfuHXd8V-nxBrh_lC1m_I" """

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
        """ list_of_tables = postgres.get_list_of_tables()

        if "redfin_data" not in list_of_tables:
            postgres.create_table() """

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
        breakfast_dict = {}
        for item in breakfast_information:
            breakfast_dict["name"] = (item.get("Name"))
            breakfast_dict["price"] = (int(item.get("Price")))
            pictures_values = item.get("PicturePath")
            pictures_link = "\'" + pictures_values + "\'"
            image_name = pictures_values.replace(" ", "_").split("/")
            breakfast_dict["image"] = (breakfast_pictures_directory + "/" + image_name[-1])
            os.system(f"wget -c -P {breakfast_pictures_directory} {pictures_link}")
        
        values = tuple(
            breakfast_dict.get(key) for key in postgres.order
        )
        postgres.breakfast_insert_data(values)
        """ yield {"breakfast_name": breakfast_names, "breakfast_price": breakfast_prices, "breakfast_image": breakfast_pictures} """


"""     def pizza_40_cm(self, page):
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

        yield {"pizza_name": pizza_names, "pizza_price": pizza_prices, "pizza_image": pizza_pictures}

    
    def rolly(self, page):
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
        PATH = str(Path(__file__).parent)
        with open(f"{page}", "r") as f:
            html = f.read()
        
        about_soup = BeautifulSoup(html, "html.parser")
        content_block = about_soup.p
        about_text = content_block.text
        yield about_text


class Vacancies(object):

    def jobs(self, page):
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
            
        yield {"vacancies": jobs_names, "theme": description}
        


mypizza_menu = Menu(PATH)
mypizza_menu.breakfast(4354)
mypizza_menu.pizza_40_cm(4372)
mypizza_menu.rolly(4365)
mypizza_menu.salaty(4358)
mypizza_menu.zakuski(4356) """




""" shares_pages = [1014, 1017, 1018, 1019, 5146, 6161, 6163, 6164, 6168, 6172]
mypizza_shares = Shares()
for share_page in shares_pages:
    print(next(mypizza_shares.shares(share_page)))

mypizza_about = About_company()
print(next(mypizza_about.about(f'{PATH}/mypizza.kg/Company/About.html')))


jobs_pages = [10, 11]
mypizza_jobs = Vacancies()
for page in jobs_pages:
    print(next(mypizza_jobs.jobs(page))) """


if __name__ == "__main__":
    dbname = input("The name of database: ")
    dbuser = input("Username of database: ")
    dbpswd = input(f"{dbuser}'s password: ")

    postgres = Postgres(db_name=dbname, user=dbuser, pswd=dbpswd)
    mypizza_menu = Menu(PATH)
    mypizza_menu.breakfast(4354)
    postgres.end()
