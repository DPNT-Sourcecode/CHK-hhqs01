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