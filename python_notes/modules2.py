"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
from python_notes.car import info
class ModulesDemo():
    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))
    def car_description(self):
        make = "bmw"
        model = "550i"
        info(make, model)
m = ModulesDemo()
m.builtin_modules()
m.car_description()
"""
output:
10.0
10.0
Make of the car: bmw
Model of the car: 550i"""