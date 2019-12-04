import requests
import json

class Beer:
    def __init__ (self, name, tag, abv, image):
        self.name = name
        self.tag = tag
        self.abv = abv
        self.image = image


def get_beer(identifier):
    url = f'https://api.punkapi.com/v2/beers/{identifier}'

    r = requests.get(url)

    random_beer = json.loads(r.text)

    beer_name = random_beer[0]['name']
    beer_tag = random_beer[0]['tagline']
    beer_abv = random_beer[0]['abv']
    beer_image = random_beer[0]['image_url']
    return Beer(beer_name, beer_tag, beer_abv, beer_image)


try_this_beer = get_beer(3)
or_this_one = get_beer(99)

print(try_this_beer.name, ' or ', or_this_one.name)


