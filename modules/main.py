# main.py - calling module
# adder.py - imported module

# import adder as a
from adder import add, double

value = add(5, 7)
double_value = double(value)
print(double_value)
