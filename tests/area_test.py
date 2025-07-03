import pytest
from codes.calculator import calculate_area_of_circle, calculate_area_of_rectangle, calculate_area_of_square

def test_calculate_area_circle():
    assert calculate_area_of_circle(3.142, 12) == (3.142 * (12 ** 2))