from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_out_of_bounds_x(self):
        try:
            sum_solution.compute(-1, 2)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

        try:
            sum_solution.compute(101, 2)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

    def test_sum_out_of_bounds_x_negative(self):
        pass

    def test_sum_out_of_bounds_x_not_int():
        pass

    def test_sum_out_of_bounds_y(self):
        pass

    def test_sum_out_of_bounds_y_negative(self):
        pass

    def test_sum_out_of_bounds_y_not_int(self):
        pass

