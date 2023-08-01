import requests
from bs4 import BeautifulSoup
from random import randrange

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
}

url = "https://www.cariboucoffee.com.tr/our-menu"

data = requests.get(url=url, headers=headers)

soup = BeautifulSoup(data.text, "html.parser")

hot_bevs = soup.select(
    "#hot-beverages > .product-list-container > .product-list > .product"
)

bakery = soup.select( "#bakery-products > .product-list-container > .product-list > .product")

menu = []

for bev in hot_bevs:
    bev_name = bev.select_one(".details > h4").text
    bev_desc = bev.select_one(".details > p").text
    bev_img = (
        "https://www.cariboucoffee.com.tr/" + bev.select_one(".image > img")["src"]
    )
    menu.append(
        {
            "name": bev_name.title(),
            "desc": bev_desc,
            "img_url": bev_img,
            "price": randrange(17000, 28000, 1000),
        }
    )

for bake in bakery:
    bake_name = bake.select_one(".details > h4").text
    bake_desc = bake.select_one(".details > p").text
    bake_img = (
        "https://www.cariboucoffee.com.tr/" + bake.select_one(".image > img")["src"]
    )
    menu.append(
        {
            "name": bake_name.title(),
            "desc": bake_desc,
            "img_url": bake_img,
            "price": randrange(17000, 28000, 1000),
        }
    )
print(menu)