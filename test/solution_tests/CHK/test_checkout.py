from solutions.CHK import checkout_solution

class TestCheckout():

    def test_checkout(self):
        #SKUS = "AAAAAAAAABBBCEE"

# EEEEBB 160 BEBEEE 160 ABCDEABCDE 280

        expected_price = 160
        actual_price = checkout_solution.checkout("EEEEBB")
        assert expected_price == actual_price

    def test_basket_invalid(self):
        try:
            skus = "ABCDEFG"
            checkout_solution.create_basket(skus)
        except ValueError:
            assert True

    def test_basket_valid(self):
        skus = "AAAABBCCCCCDEE"

        expected_basket = {
            "A": 4,
            "B": 2,
            "C": 5,
            "D": 1,
            "E": 2
        }

        actual_basket = checkout_solution.create_basket(skus)

        assert actual_basket == expected_basket

    def test_compute_price_for_item(self):
        basket = {
            "A": 6
        }

        item = "A"

        actual_price = checkout_solution.compute_price_for_item(item, basket)
        expected_price = 6 * 50

        assert expected_price == actual_price

    def test_handle_bundle_offer_no_offer(self):
        item = "A"

        basket = {
            "A": 2
        }

        price = 100

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = price

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert basket == actual_basket

    def test_handle_bundle_offer_better_offer_first(self):
        item = "A"

        basket = {
            "A": 9
        }

        price = 9 * 50

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = 200 + 130 + 50
        expected_basket = {"A": 1}

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert expected_basket == actual_basket
        

    def test_hande_bundle_offer_multiple_offers(self):
        item = "A"

        basket = {
            "A": 13
        }

        price = 13 * 50

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = 200 + 200 + 130
        expected_basket = {"A": 0}

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert expected_basket == actual_basket

    def test_hande_bundle_offer_multiple_offers_larger_unsatisfied(self):
        item = "A"

        basket = {
            "A": 3
        }

        price = 3 * 50

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = 130
        expected_basket = {"A": 0}

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert expected_basket == actual_basket

    def test_hande_bundle_offer_multiple_offers_smaller_unsatisfied(self):
        item = "A"

        basket = {
            "A": 6
        }

        price = 6 * 50

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = 200 + 50
        expected_basket = {"A": 1}

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert expected_basket == actual_basket

    def test_hande_bundle_offer_multiple_offers_smaller_unsatisfied(self):    
        basket = {
            "A": 6,
            "B": 3
        }

        price = 6 * 50 + 3 * 30

        offers = [
            {"for_item": "A", "type": "BUNDLE", "count": 5, "price": 200},
            {"for_item": "A", "type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = 200 + 50 + 3 * 30
        expected_basket = {"A": 1, "B": 3}

        actual_price, actual_basket = checkout_solution.handle_bundle_offers(basket, price, offers)

        assert expected_price == actual_price
        assert expected_basket == actual_basket

    def test_handle_get_free_offers(self):
        item = "E"
        
        basket = {
            "B": 1,
            "E": 2
        }

        price = 30 + 2 * 40

        offers = [
            {"for_item": "E", "type": "GET_FREE", "count": 2, "item_free": "B"}
        ]

        expected_basket = { "B": 0, "E" : 2}

        actual_basket = checkout_solution.handle_get_free_offers(basket, offers)

        assert expected_basket == actual_basket


