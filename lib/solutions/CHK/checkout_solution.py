PRICE_TABLE = {
    "A" : {
        "price": 50,
        "offer": [
            {
                "count": 5,
                "offer_price": 200,
                "TYPE": "BUNDLE"
            },
            {
                "count": 3,
                "offer_price": 130,
                "TYPE": "BUNDLE"
            },
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
        "offer": [
            {
                "count": 2,
                "type": "GET_FREE",
                "item_free": "B"
            }
        ]
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

    return apply_offers(basket, price)



def compute_price_for_item(item, basket):
    item_number_to_account = basket[item]
    return item_number_to_account * PRICE_TABLE[item]["price"]
    

def apply_offers(basket, price):
    for item in basket:
        if "offer" in PRICE_TABLE["ITEM"]:
            bundle_offers = [bundle_offer for bundle_offer in PRICE_TABLE[item]["offer"] if bundle_offer["type"] == "BUNDLE_OFFER"]
            get_free_offers = [get_free_offer for get_free_offer in PRICE_TABLE[item]["offer"] if get_free_offer["type"] == "GET_FREE"]


    return price

def handle_bundle_offers(item, basket, price, offers):
    for offer in offers:
        apply_times = basket[item] // offer["count"]
        total_discount = apply_times * ((PRICE_TABLE[item]["price"] * offer["count"]) - offer["price"])

        basket[item] = basket[item] % offer["count"]
        price -= total_discount

    return (price, basket)

def handle_get_free_offers(item, basket, price, offers):
    for offer in offers:
        apply_times = basket[item] // offer["count"]
        # This assumes you only get one free
        discount = min(apply_times, basket[offer["item_free"]]) * PRICE_TABLE[offer["item_free"]]
        basket[offer["item_free"]] = min(0, basket[offer["item_free"]] - apply_times)
        price -= discount

    return price




def _is_valid_input(character):
    return character in ["A", "B", "C", "D", "E"]







