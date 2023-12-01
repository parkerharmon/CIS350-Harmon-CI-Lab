from math_functions import *
def test_calc_addition():
	output = add_numbers(2,4)
	assert output == 6
def test_calc_subtraction():
	output = subtract_numbers(2, 4)
	assert output == -2
def test_calc_multiply():
	output = multiply_numbers(2,4)
	assert output == 8
def test_calc_multiply_fail():
	output = multiply_numbers(2,4)
	assert output == 8
def test_calc_divide():
	output = divide_numbers(10,2)
	assert output == 5
def test_calc_square():
	output = square_number(5)
	assert output == 25
def test_calc_square_root():
	output = square_root(36)
	assert output == 6
