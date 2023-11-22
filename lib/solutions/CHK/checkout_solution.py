PRICE_TABLE = {
    "A" : 50,
    "B" : 30,
    "C" : 20,
    "D" : 15,
    "E" : 40,
    "F" : 10,
    "G" : 20,
    "H" : 10,
    "I" : 35,
    "J" : 60,
    "K" : 80,
    "L" : 90,
    "M" : 15,
    "N" : 40,
    "O" : 10,
    "P" : 50,
    "Q" : 30,
    "R" : 50,
    "S" : 30,
    "T" : 20,
    "U" : 40,
    "V" : 50,
    "W" : 20,
    "X" : 90,
    "Y" : 10,
    "Z" : 50,
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
            },
                        {
                "for_item": "H",
                "count": 10,
                "price": 80,
                "type": "BUNDLE"
            },
            {
                "for_item": "H",
                "count": 5,
                "price": 45,
                "type": "BUNDLE"
            },
            {
                "for_item": "K",
                "count": 2,
                "price": 150,
                "type": "BUNDLE"
            },
            {
                "for_item": "N",
                "count": 3,
                "type": "GET_FREE",
                "item_free": "M"
            },
             {
                "for_item": "P",
                "count": 5,
                "type": "BUNDLE",
                "price": 200
            },
            {
                "for_item": "Q",
                "count": 3,
                "type": "BUNDLE",
                "price": 80
            },
            {
                "for_item": "R",
                "count": 3,
                "type": "GET_FREE",
                "item_free": "Q"
            },
            {
                "for_item": "U",
                "count": 4,
                "type": "GET_FREE",
                "item_free": "U"
            },
            {
                "for_item": "V",
                "count": 3,
                "type": "BUNDLE",
                "price": 130
            },
            {
                "for_item": "V",
                "count": 2,
                "type": "BUNDLE",
                "price": 90
            },
            {
                "group": ["S", "T", "X", "Y", "Z"],
                "count": 3,
                "type": "BUNDLE_GROUP",
                "price": 45
            },
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
    group_bundle_offers = [bundle_offer for bundle_offer in OFFERS if bundle_offer["type"] == "BUNDLE_GROUP"]

    basket = handle_get_free_offers(basket, get_free_offers)

    price = compute_price(basket)

    price, basket = handle_bundle_offers(basket, price, bundle_offers)
    price, _ = handle_group_bundle_offers(basket, price, group_bundle_offers)

    return price

def handle_bundle_offers(basket, price, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket.get(item, 0) // offer["count"]
        total_discount = apply_times * ((PRICE_TABLE[item] * offer["count"]) - offer["price"])

        basket[item] = basket.get(item, 0) % offer["count"]
        price -= total_discount

    return (price, basket)

def handle_group_bundle_offers(basket, price, offers):
    for offer in offers:
        items_in_offer = dict(sorted({ item: count for item, count in basket.items() if item in offer["group"]}.items(), key=lambda x: x[1] ,reverse=True))
        
        item_count = sum(items_in_offer.values())
        apply_times = item_count // offer["count"]
        items_to_be_discounted = apply_times * offer["count"]

        while items_to_be_discounted > 0:
            priciest_item, priciest_item_count = items_in_offer
            priciest_item_count = min(priciest_item_count, items_to_be_discounted) # Find out how many items to discount

            price -= priciest_item_count * (PRICE_TABLE[priciest_item]  - (offer["price"] / offer["count"]))

            items_in_offer[priciest_item] -= priciest_item_count # This is more used for debugging purposes
            
            items_to_be_discounted -= priciest_item_count

        basket.update(items_in_offer)


    return (price, basket)

def handle_get_free_offers(basket, offers):
    for offer in offers:
        item = offer["for_item"]
        apply_times = basket.get(item, 0) // offer["count"]
        basket[offer["item_free"]] = max(0, basket.get(offer["item_free"], 0) - apply_times)

    return basket




def _is_valid_input(character):
    return character in PRICE_TABLE
