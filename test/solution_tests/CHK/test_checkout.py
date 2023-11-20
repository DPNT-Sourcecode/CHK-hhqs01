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

    def test_compute_price_for_item_no_offer_has_offer(self):
        basket = {
            "A": 2
        }

        item = "A"

        actual_price = checkout_solution.compute_price_for_item(item, basket)

        expected_price = 100

        assert expected_price == actual_price

    def test_compute_price_for_item_offer_has_offer(self):
        basket = {
            "A": 6
        }

        item = "A"

        actual_price = checkout_solution.compute_price_for_item(item, basket)

        expected_price = 260

        assert expected_price == actual_price

    def test_compute_price_for_item_has_no_offer(self):
        basket = {
            "D": 6
        }

        item = "D"

        actual_price = checkout_solution.compute_price_for_item(item, basket)

        expected_price = 15 * 6

        assert expected_price == actual_price
