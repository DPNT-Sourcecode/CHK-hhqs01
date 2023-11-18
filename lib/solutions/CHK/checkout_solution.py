
import re

PRICE_TABLE = {
    "A" : {
        "price": 50,
        "offer": {
            "count": 3,
            "price": 130
        }
    },
    "B" : {
        "price": 30,
        "offer": {
            "count": 2,
            "price": 45
        }
    },
    "C" : {
        "price": 20,
    },
    "D" : {
        "price": 15
    }
}  


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = {}
    for character in skus:
        if not _is_valid_input(character):
            return -1
        
        if character in basket:
            basket[character] += 1
        else:
            basket[character] == 1

def _is_valid_input(character):
    return character in ["A", "B", "C", "D"]



