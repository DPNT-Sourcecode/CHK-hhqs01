PRICE_TABLE = {
    "A" : 50,
    "B" : 30,
    "C" : 20,
    "D" : 15,
    "E" : 40,
    "F" : 10
}  

OFFERS = [
            {
                "for_item": "A",
                "count": 5,
                "price": 200,
                "type": "BUNDLE"
            },
            {
                "for_item": "A",
                "count": 3,
                "price": 130,
                "type": "BUNDLE"
            },
            {
                "for_item": "B",  
                "count": 2,
                "price": 45,
                "type" : "BUNDLE"
            },
            {
                "for_item": "E",
                "count": 2,
                "type": "GET_FREE",
                "item_free": "B"
            },
             {
                "for_item": "F",
                "count": 3,
                "type": "GET_FREE",
                "item_free": "F"
            }
]

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    if not skus:
        return 0
    
    basket = {}
    try:
        basket = create_basket(skus)
    except ValueError:
        return -1

    return apply_offers(basket)

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
        price += basket[item] * PRICE_TABLE[item]

    return price

def apply_offers(basket):
    bundle_offers = [bundle_offer for bundle_offer in OFFERS if bundle_offer["type"] == "BUNDLE"]
    get_free_offers = [get_free_offer for get_free_offer in OFFERS if get_free_offer["type"] == "GET_FREE"]

    basket = handle_get_free_offers(basket, get_free_offers)

    price = compute_price(basket)

    price, _ = handle_bundle_offers(basket, price, bundle_offers)

    return price

def handle_bundle_offers(basket, price, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket.get(item, 0) // offer["count"]
        total_discount = apply_times * ((PRICE_TABLE[item] * offer["count"]) - offer["price"])

        basket[item] = basket.get(item, 0) % offer["count"]
        price -= total_discount

    return (price, basket)

def handle_get_free_offers(basket, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket.get(item, 0) // offer["count"]
        basket[offer["item_free"]] = max(0, basket.get(offer["item_free"], 0) - apply_times)

    return basket




def _is_valid_input(character):
    return character in PRICE_TABLE



