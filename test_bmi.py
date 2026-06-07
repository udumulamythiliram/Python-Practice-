from bmi_calculator import get_category , get_bmi

def test_underweight():
    assert get_category(17) == "Underweight"

def test_normal():
    assert get_category(22) == "Normal weight"

def test_over():
    assert get_category(28) == "Overweight"

def test_obese():
    assert get_category(35) == "Obese"
