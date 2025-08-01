from app.utils import multiply, divide, factorial
import pytest

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    
def test_divide_by_zero():
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert "Division by zero" in str(excinfo.value)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120
    
def test_factorial_negative():
    with pytest.raises(ValueError) as excinfo:
        factorial(-3)
    assert "not defined for negative numbers" in str(excinfo.value)
