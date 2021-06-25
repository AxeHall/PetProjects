import requests
from bs4 import BeautifulSoup


SITE_URL = "https://xakep.ru/"


class Xakep(object):
    def __init__(self, url):
        self.url = url

    def get_html(self, url):
        r = requests.get(url)

        if r.status_code == 200:
            return r.text
        else:
            return 0

    def main_page(self, page):
        html = self.get_html(f"https://xakep.ru/page/{page}/")

        if html:
            soup = BeautifulSoup(html, "html.parser")
            pairs_block = soup.find_all("div", class_="bd-block-row")

            for pair in pairs_block:

                pairs = pair.find_all(
                    "div", class_="block-article bd-col-md-6 bdaiaFadeIn"
                )

                for item in pairs:
                    picture = item.img["src"]
                    header = item.h3.span.text
                    article_link = item.a["href"]
                    article_definition_html = self.get_html(article_link)

                    if article_definition_html:
                        definition_soup = BeautifulSoup(
                            article_definition_html, "html.parser"
                        )
                        text_blocks = definition_soup.find_all("p")
                        text_list = [p.text for p in text_blocks[6:-1]]
                        text = " ".join(text_list)
                        yield {"picture": picture, "header": header, "definition": text}

                    else:
                        continue

        return "Ошибка на сайте"

    def get_number_of_pages(self):
        html = self.get_html(self.url)
        if html:
            soup = BeautifulSoup(html, "html.parser")
            pagination = soup.find("div", class_="bdaia-pagination")
            pagination_list = pagination.span.text.split("из")

            number_of_pages = int(
                "".join([i for i in pagination_list[-1] if i.isdigit()])
            )
            return number_of_pages
        return 0


xakep = Xakep(SITE_URL)
try:
    pages = xakep.get_number_of_pages()

    for page in range(1, pages + 1):
        generator = xakep.main_page(page)
        print(next(generator))
        
except requests.exceptions.ConnectionError:
    print("Нет интернета!")

# html_page = xakep.main_page()
# with open("./xakep.html", "w") as f:
#     f.write(html_page)
