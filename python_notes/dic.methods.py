
car = {'make': 'bmw', 'model': '550i', 'year': 2016}
cars = {'bmw': {'model': '550i', 'year': 2016}, 'benz': {'model': 'E350', 'year': 2015}}

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())

car_copy = car.copy()
print(car_copy)

print(car.pop('model'))
print(car)
""" OUTPUT:
dict_keys(['make', 'model', 'year'])
dict_keys(['bmw', 'benz'])
dict_values(['bmw', '550i', 2016])
dict_values([{'model': '550i', 'year': 2016}, {'model': 'E350', 'year': 2015}])
dict_items([('make', 'bmw'), ('model', '550i'), ('year', 2016)])
{'make': 'bmw', 'model': '550i', 'year': 2016}
550i
{'make': 'bmw', 'year': 2016}"""
