from codes import calculator

def test_example():
    assert True

def test_circle_area():
    assert calculator.calculate_area_of_circle(10, 20) == (10 * (20 ** 2))