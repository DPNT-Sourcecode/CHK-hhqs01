
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
    raise NotImplementedError()
