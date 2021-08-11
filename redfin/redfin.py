import os
import csv
from time import sleep
from pathlib import Path


import requests
from bs4 import BeautifulSoup


from db import Postgres


class RedfinParser(object):
    def __init__(self, url):
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Referer": "https://www.redfin.com/",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "text/plain;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        }

        self.PATH = str(Path(__file__).parent)

        self.csv_broker(
            [
                "List Price",
                "Price/Sq.Ft.",
                "Est. Mo. Payment",
                "Buyer's Brokerage Commission",
                "HOA Dues",
                "Status",
                "Time on Redfin",
                "Property Type",
                "Year Built",
                "Style",
                "Community",
                "Lot Size",
                "MLS#",
                "beds",
                "baths",
                "address",
            ],
            mode="w",
        )

    def get_html(self, url):
        sleep(3.5)
        try:
            result = requests.get(url, headers=self.headers)
        except requests.exceptions.ConnectionError:
            print("There is something wrong with Internet connection...")
            return 0

        if result.status_code == 200:
            return result.text

        elif result.status_code == 403:
            print("You are blocked by the site")
            return 0

        elif result.status_code == 404:
            print("Wrong URL!")
            return 0

    def homes(self, url):
        html = self.get_html(url)
        soup = BeautifulSoup(html, "html.parser")
        url_blocks = soup.find_all("div", class_="HomeCardContainer")
        n = 0
        for block in url_blocks:
            try:
                if block["id"]:
                    n += 1
            except:
                pass
        return n

    def get_amount_of_pages(self):
        main_html = self.get_html(self.url)

        if main_html:
            soup = BeautifulSoup(main_html, "html.parser")
            url_blocks = soup.find("span", class_="pageText")

            if url_blocks:
                pagination = str(url_blocks.text).split(" ")
                return int(pagination[-1])

        return 0

    def harvest(self, page):
        list_of_tables = postgres.get_list_of_tables()

        if "redfin_data" not in list_of_tables:
            postgres.create_table()

        url = self.url + f"/page-{page}"

        main_html = self.get_html(url)

        if main_html:
            soup = BeautifulSoup(main_html, "html.parser")

            url_blocks = soup.find_all("a", attrs={"data-rf-test-id": "slider-item-0"})

            for block in url_blocks:
                home_link = block["href"]
                home_url = "https://www.redfin.com" + home_link

                home_html = self.get_html(home_url)

                if home_html:
                    fields_dict = {"HOA Dues": 0}

                    soup = BeautifulSoup(home_html, "html.parser")

                    fields_dict["beds"] = (
                        soup.find("div", attrs={"data-rf-test-id": "abp-beds"})
                    ).div.text.strip()

                    fields_dict["baths"] = (
                        soup.find("div", attrs={"data-rf-test-id": "abp-baths"})
                    ).div.text.strip()

                    dataset = soup.find_all(
                        "div", class_="keyDetail font-weight-roman font-size-base"
                    )

                    fields_dict["square"] = (
                        soup.find("div", attrs={"data-rf-test-id": "abp-sqFt"})
                        .span.text.replace(",", "")
                        .strip()
                    )

                    fields_dict["address"] = (
                        soup.find("h1", class_="homeAddress-variant")
                    ).text.strip()

                    image_1 = soup.find(
                        "div",
                        class_="InlinePhotoPreview--Photo InlinePhotoPreview--PhotoOne pos-rel inline-block",
                    )

                    if image_1:
                        if image_1.img:
                            img = image_1.img["src"]
                            os.system(f"wget -P {self.PATH}/images/ {img}")

                    image_2 = soup.find(
                        "div",
                        class_="InlinePhotoPreview--Photo InlinePhotoPreview--PhotoTwo pos-abs inline-block",
                    )
                    if image_2:
                        if image_2.img:
                            img = image_2.img["src"]
                            os.system(f"wget -P {self.PATH}/images/ {img}")

                    image_3 = soup.find(
                        "div",
                        class_="InlinePhotoPreview--Photo InlinePhotoPreview--PhotoThree pos-abs",
                    )

                    if image_3:
                        if image_3.img:
                            img = image_3.img["src"]
                            os.system(f"wget -P {self.PATH}/images/ {img}")

                    for data in dataset:
                        spans = data.find_all("span")
                        if spans[0].text not in fields_dict:
                            fields_dict[spans[0].text] = 0

                        if spans[0].text in (
                            "List Price",
                            "Est. Mo. Payment",
                            "Price/Sq.Ft.",
                        ):
                            if "—" not in spans[1].text:
                                fields_dict[spans[0].text] = (
                                    spans[1].text.replace("$", "").replace(",", "")
                                )
                            else:
                                fields_dict[spans[0].text] = 0

                        elif spans[0].text in (
                            "Status",
                            "Property Type",
                            "Community",
                            "MLS#",
                            "Style",
                            "Year Built",
                        ):
                            fields_dict[spans[0].text] = spans[1].text

                        elif spans[0].text in ("Time on Redfin", "Lot Size", "Baths"):
                            fields_dict[spans[0].text] = (
                                spans[1].text.split()[0].replace(",", "")
                            )

                        elif spans[0].text == "HOA Dues":
                            fields_dict[spans[0].text] = (
                                spans[1]
                                .text.split("/")[0]
                                .replace(",", "")
                                .replace("$", "")
                            )
                        else:
                            fields_dict[spans[0].text] = (
                                spans[2]
                                .text.replace(",", "")
                                .replace("$", "")
                                .replace("%", "")
                            )

                    values = tuple(
                        fields_dict.get(key).replace("'", "") for key in postgres.order
                    )

                    self.csv_broker(values)
                    postgres.insert_data(values)

    def csv_broker(self, data, mode="a"):
        with open("Price_Insights.csv", mode=mode, encoding="utf-8") as w_file:
            file_writer = csv.writer(w_file)
            file_writer.writerow(data)


if __name__ == "__main__":
    dbname = input("The name of database: ")
    dbuser = input("Username of database: ")
    dbpswd = input(f"{dbuser}'s password: ")

    postgres = Postgres(db_name=dbname, user=dbuser, pswd=dbpswd)

    site_url = input("Please type URL: ")

    redfin = RedfinParser(url=site_url)
    pages_number = redfin.get_amount_of_pages()

    for page in range(1, pages_number + 1):
        redfin.harvest(page)

    postgres.end()
