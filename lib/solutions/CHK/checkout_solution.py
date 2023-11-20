PRICE_TABLE = {
    "A" : {
        "price": 50,
        "offer": [
            {
                "count": 3,
                "offer_price": 130,
                "TYPE": "BUNDLE"
            },
            {
                "count": 5,
                "offer_price": 200,
                "TYPE": "BUNDLE"
            }
        ]
    },
    "B" : {
        "price": 30,
        "offer": [
            {    
                "count": 2,
                "offer_price": 45,
                "type" : "BUNDLE"
            }
        ]
    },
    "C" : {
        "price": 20,
    },
    "D" : {
        "price": 15
    },
    "E": {
        "price": 20,
        "offer": {
            "count": 2,
            "type": "GET_FREE",
            "item_free": "B"

        }
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
    price = 0
    for item in basket:
        price += compute_price_for_item(item, basket)

    return price



def compute_price_for_item(item, basket):
    price_for_item = 0
    item_number_to_account = basket[item]
    if "offer" in PRICE_TABLE[item]:
        # Find out how many times we satisfy the offer
        price_for_item += item_number_to_account // PRICE_TABLE[item]["offer"]["count"] * PRICE_TABLE[item]["offer"]["offer_price"]   
        # Add the non offer ones
        price_for_item += item_number_to_account % PRICE_TABLE[item]["offer"]["count"] * PRICE_TABLE[item]["price"]
    else:
        price_for_item = item_number_to_account * PRICE_TABLE[item]["price"]

    return price_for_item

def apply_offers(basket, price):
    return 0

def _is_valid_input(character):
    return character in ["A", "B", "C", "D", "E"]
