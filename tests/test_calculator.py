import pytest


@pytest.mark.smoke
class TestCalculatorSmoke:

    def test_add_smoke(self, calc):
        assert calc.add(2, 3) == 5


    def test_subtract_smoke(self, calc):
        assert calc.subtract(17, 8) == 9


    def test_multiply_smoke(self, calc):
        assert calc.multiply(7, 8) == 56


    def test_multiply_by_zero_smoke(self, calc):
        assert calc.multiply(10, 0) == 0


    def test_divide_smoke(self, calc):
        assert calc.divide(16, 8) == 2


    def test_divide_zero_smoke(self, calc):
        with pytest.raises(ZeroDivisionError):
            calc.divide(10, 0)


@pytest.mark.regression
class TestCalculatorRegression:

    @pytest.mark.parametrize(
        "a,b,result",
        [
            (2, 3, 5),  # positive + positive
            (0, 5, 5),  # zero + positive
            (-2, 3, 1),  # negative + positive
            (-4, -5, -9),  # negative + negative
            (7, 0, 7),  # positive + zero
            (0, 0, 0),  # zero + zero
        ]
    )
    def test_add(self, calc, a, b, result):
        assert calc.add(a, b) == result


    @pytest.mark.parametrize(
        "a,b,result",
        [
            (10, 5, 5),  # positive - positive
            (0, 5, -5),  # zero - positive
            (-2, 3, -5),  # negative - positive
            (-4, -5, 1),  # negative - negative
            (7, 0, 7),  # positive - zero
            (0, 0, 0),  # zero - zero
        ]
    )
    def test_subtract(self, calc, a, b, result):
        assert calc.subtract(a, b) == result


    @pytest.mark.parametrize(
        "a,b,result",
        [
            (2, 3, 6),  # positive * positive
            (5, 5, 25),  # positive * positive
            (0, 10, 0),  # zero * positive
            (0, 0, 0),  # zero * zero
            (-2, 3, -6),  # negative * positive
            (4, -3, -12),  # positive * negative
            (-5, -5, 25),  # negative * negative
            (7, 0, 0),  # positive * zero
            (-7, 0, 0),  # negative * zero
        ]
    )
    def test_multiply(self, calc, a, b, result):
        assert calc.multiply(a, b) == result


    @pytest.mark.parametrize(
        "a,b,result",
        [
            (10, 2, 5),  # positive ÷ positive
            (-10, 2, -5),  # negative ÷ positive
            (10, -2, -5),  # positive ÷ negative
            (-10, -2, 5),  # negative ÷ negative
            (0, 5, 0),  # zero ÷ positive
        ]
    )
    def test_divide(self, calc, a, b, result):
        assert calc.divide(a, b) == result


    @pytest.mark.parametrize("a", [10, -5, 0])
    def test_divide_by_zero(self, calc, a):
        with pytest.raises(ZeroDivisionError):
            calc.divide(a, 0)



