import os
import sys
# https://stackoverflow.com/questions/16771894/python-nameerror-global-name-file-is-not-defined
if '__file__' in vars():
    print("We are running the script non interactively")
    path = os.path.join(os.path.dirname(__file__), os.pardir)
    # see https://www.geeksforgeeks.org/python-os-pardir-method-with-example/ for an example
    sys.path.append(path)
else:
    print('We are running the script interactively')
    sys.path.append("..")

from src.my_math_lib.basic import multiply

a = 3
b = 2
c = multiply(a, b)
print(f"{a} * {b} = {c}")