import httpx
from parsel import Selector
from pprint import pprint
from db.base import DB
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


def clean_text(text: str):
    if text is None:
        return ""
    text = " ".join(text.split())
    return text.strip().replace("\t", "").replace("\n", "")


def price_to_int(price: str):
    result_price = ''
    for i in price:
        if i.isdigit():
            result_price += i
    return int(result_price)


def get_house_data(html: Selector):
    houses = html.css("div.main-wrapper")
    houses_list = []
    for house in houses:
        house_data = {}
        house_data["title"] = clean_text(house.css("p.title a::text").get())
        house_data["price"] = price_to_int(clean_text(house.css("div.price::text").get()))
        house_data["som_price"] = price_to_int(clean_text(house.css("div.price-addition::text").get()))
        house_data["house_description"] = clean_text(house.css("div.description::text").get())
        house_data["address"] = clean_text(house.css("div.address::text").getall()[1])
        houses_list.append(house_data)
    return houses_list


def get_houses():
    houses = []
    for page in range(1, 5):
        url = f"{MAIN_URL}?page={page}"
        html = get_page(url)
        houses.extend(get_house_data(html))
    # return get_house_links(html)
    #   pprint(houses)
    # print("Lenght", len(houses))
    return houses


if __name__ == "__main__":
    page = get_page(MAIN_URL)
    houses = get_houses()
    db = DB()
    for house in houses:
        db.insert_houses(house)
    print('дома добавлены')


