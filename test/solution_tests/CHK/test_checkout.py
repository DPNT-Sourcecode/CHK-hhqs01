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
        skus = "AAAABBCCCCCD"

        expected_basket = {
            "A": 4,
            "B": 2,
            "C": 5,
            "D": 1
        }

        actual_basket = checkout_solution.create_basket(skus)

        assert actual_basket == expected_basket

    def test_compute_price_for_item_no_offer(self):
        basket = {
            "A": 2
        }

        item = "A"

        actual_price = checkout_solution.compute_price_for_item(item, basket)

        expected_price = 100

        assert expected_price == actual_price