'''
TPRG 2131 Fall 202x Assignment 1, Test file template.
Sept, 202x
Phil J <philip.jarvis@durhamcollege>


This file is to be the test_A_V_calc.py file to be used with your A_V_calc.py and pytest.
This must test each of your Area/Volume functions, with a least 3 examples for each of the
5 functions your chose to use.

As this stands it will NOT work with your A_V_calc.py file.
'''

# Name: Manpreet Badgal
# Student ID: 100945948
import pytest
from A_V_calc_mb import calculated_rectangle_area, calculated_circle_area, calculated_triangle_area, calculated_cuboid_volume, calculated_cylinder_volume


def test_calculated_rectangle_area():
    assert calculated_rectangle_area(5, 10) == 50
    assert calculated_rectangle_area(2.5, 4) == 10
    assert calculated_rectangle_area(0, 5) == 0

def test_calculated_circle_area():
    assert calculated_circle_area(10) == 314.2
    assert calculated_circle_area(0) == 0

def test_calculated_triangle_area():
    assert calculated_triangle_area(10, 5) == 25
    assert calculated_triangle_area(0, 5) == 0

def test_calculated_cuboid_volume():
    assert calculated_cuboid_volume(2, 3, 4) == 24
    assert calculated_cuboid_volume(0, 3, 4) == 0

def test_calculated_cylinder_volume():
    assert calculated_cylinder_volume(5,10 ) ==261.8 
    assert calculated_cylinder_volume(0, 5) == 0