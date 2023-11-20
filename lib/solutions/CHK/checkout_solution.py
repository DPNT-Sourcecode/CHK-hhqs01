PRICE_TABLE = {
    "A" : 50,
    "B" : 30,
    "C" : 20,
    "D" : 15,
    "E" : 40
}  

OFFERS = [
            {
                "for_item": "A",
                "count": 5,
                "offer_price": 200,
                "TYPE": "BUNDLE"
            },
            {
                "for_item": "A",
                "count": 3,
                "offer_price": 130,
                "TYPE": "BUNDLE"
            },
            {
                "for_item": "B",  
                "count": 2,
                "offer_price": 45,
                "type" : "BUNDLE"
            },
            {
                "for_item": "E",
                "count": 2,
                "type": "GET_FREE",
                "item_free": "B"
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

    price = apply_offers(basket, price)
    return price



def compute_price_for_item(item, basket):
    item_number_to_account = basket[item]
    return item_number_to_account * PRICE_TABLE[item]
    

def apply_offers(basket, price):
    bundle_offers = [bundle_offer for bundle_offer in OFFERS if bundle_offer["type"] == "BUNDLE_OFFER"]
    get_free_offers = [get_free_offer for get_free_offer in OFFERS if get_free_offer["type"] == "GET_FREE"]

    price, basket = handle_bundle_offers(basket, price, bundle_offers)
    price, basket = handle_get_free_offers(basket, price, get_free_offers)

    return price

def handle_bundle_offers(basket, price, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket[item] // offer["count"]
        total_discount = apply_times * ((PRICE_TABLE[item] * offer["count"]) - offer["price"])

        basket[item] = basket[item] % offer["count"]
        price -= total_discount

    return (price, basket)

def handle_get_free_offers(basket, price, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket[item] // offer["count"]
        # This assumes you only get one free
        discount = min(apply_times, basket[offer["item_free"]]) * PRICE_TABLE[offer["item_free"]]
        basket[offer["item_free"]] = min(0, basket[offer["item_free"]] - apply_times)
        price -= discount

    return (price, basket)




def _is_valid_input(character):
    return character in ["A", "B", "C", "D", "E"]
