from calculator.calculator import Calculator


class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        assert Calculator().subtract(1234, 1234) == 0

    def test_multiply(self):
        assert Calculator().multiply(9, 9) == 81

    def test_divide(self):
        assert Calculator().divide(999, 999) == 1
