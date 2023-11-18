from solutions.SUM import sum_solution


class TestSum():
    def test_sum(self):
        assert sum_solution.compute(1, 2) == 3

    def test_sum_out_of_bounds_x(self):
        try:
            sum_solution.compute(101, 2)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

    def test_sum_out_of_bounds_x_negative(self):
        try:
            sum_solution.compute(-1, 2)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

    def test_sum_out_of_bounds_x_not_int(self):
        try:
            sum_solution.compute("SomeString", 2)
        except TypeError as err:
            assert str(err) == "Input is not an integer"

    def test_sum_out_of_bounds_y(self):
        try:
            sum_solution.compute(1, 200)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

    def test_sum_out_of_bounds_y_negative(self):
        try:
            sum_solution.compute(1, -2)
        except ValueError as err:
            assert str(err) == "Input is not in the expected range"

    def test_sum_out_of_bounds_y_not_int(self):
        try:
            sum_solution.compute(1, "String")
        except TypeError as err:
            assert str(err) == "Input is not an integer"
