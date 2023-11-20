from solutions.CHK import checkout_solution

class TestCheckout():

    def test_checkout(self):
        assert 1 == 1

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
            {"type": "BUNDLE", "count": 5, "price": 200},
            {"type": "BUNDLE", "count": 3, "price": 130}
        ]

        expected_price = price

        actual_price = checkout_solution.apply_bundle_offers(item, basket, price, offers)

        assert expected_price == actual_price

    def test_handle_bundle_offer_better_offer_first(self):
        pass

    def test_hande_bundle_offer_multiple_offers(self):
        pass

    def test_hande_bundle_offer_multiple_offers_larger_unsatisfied(self):
        pass

    def test_hande_bundle_offer_multiple_offers_smaller_unsatisfied(self):
        pass

