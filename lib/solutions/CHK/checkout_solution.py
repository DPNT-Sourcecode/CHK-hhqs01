
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
    try:
        basket = create_basket(skus)
    except ValueError:
        return -1

    return compute_price(basket)

def create_basket(skus):
    basket = {}
    for character in skus:
        if not _is_valid_input(character):
            raise ValueError("Unrecognized SKU value!")
        
        basket[character] = basket.get(character, 0) + 1
    
    return basket

def compute_price(basket):
    return 0

    
    

def _is_valid_input(character):
    return character in ["A", "B", "C", "D"]




