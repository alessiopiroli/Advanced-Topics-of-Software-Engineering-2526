import pytest
from calculator import Calculator

class TestCalculator:
    # --- Basic Operations ---
    def test_add(self):
        calc = Calculator()
        assert calc.add(1, 2) == 3
        assert calc.get_stack() == [3]

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(4, 2) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 5) == 10

    def test_divide(self):
        calc = Calculator()
        # Test normal division
        assert calc.divide(10, 2) == 5

    # [NEW] Test division by zero exception
    def test_divide_by_zero(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)

    # --- Advanced Operations ---
    def test_power(self):
        calc = Calculator()
        assert calc.power(2, 3) == 8
        assert calc.get_last_result() == 8

    # [NEW] Test square root of positive number
    def test_square_root(self):
        calc = Calculator()
        assert calc.square_root(9) == 3.0

    def test_square_root_negative_raises(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.square_root(-4)

    def test_factorial(self):
        calc = Calculator()
        assert calc.factorial(5) == 120

    # [NEW] Test factorial negative input exception
    def test_factorial_negative(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.factorial(-1)
            
    # [NEW] Test factorial non-integer input exception (already partially there, but explicit)
    def test_factorial_float(self):
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.factorial(4.5)

    # --- Utility Functions [NEW SECTION] ---
    def test_negate(self):
        calc = Calculator()
        assert calc.negate(5) == -5
        assert calc.negate(-5) == 5

    def test_absolute(self):
        calc = Calculator()
        assert calc.absolute(-10) == 10
        assert calc.absolute(10) == 10

    def test_modulo(self):
        calc = Calculator()
        assert calc.modulo(10, 3) == 1
        with pytest.raises(ValueError):
            calc.modulo(10, 0)

    def test_is_even(self):
        calc = Calculator()
        assert calc.is_even(2) is True
        assert calc.is_even(3) is False
        with pytest.raises(ValueError):
            calc.is_even(2.5)

    def test_gcd(self):
        calc = Calculator()
        assert calc.gcd(12, 6) == 6
        assert calc.gcd(7, 3) == 1

    # --- Memory & Stack Functions ---
    def test_memory_store_and_clear(self):
        calc = Calculator()
        calc.memory_store(7)
        assert calc.memory_recall() == 7
        calc.memory_clear()
        assert calc.memory_recall() is None

    def test_get_last_result_and_clear_stack(self):
        calc = Calculator()
        calc.add(1, 1)
        calc.multiply(2, 3)
        assert calc.get_last_result() == 6
        calc.clear_stack()
        assert calc.get_stack() == []
        calc.add(2, 3)
        assert calc.get_last_result() == 5

    # [NEW] Test getting result from empty stack
    def test_get_last_result_empty(self):
        calc = Calculator()
        assert calc.get_last_result() is None