import httpx
from parsel import Selector

MAIN_URL = "https://www.house.kg/snyat"
BASE_URL = "https://www.house.kg"


def get_page(url):
    response = httpx.get(url)
    # return response.text
    return Selector(response.text)


def get_title(html):
    title = html.css("title::text").get()
    return title


def get_house_links(html):
    houses = html.css(".left-image a::attr(href)").getall()
    links = list(map(lambda x: BASE_URL + x, houses))
    return links


# if __name__ == "__main__":
#     page = get_page(MAIN_URL)
#     links = get_house_links(page)
#     print(links)
