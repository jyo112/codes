car = {'make': 'bmw', 'model': '550i', 'year': 2016}
print(car)
d = {}
model = car['model']
print(car['make'])
print(model)
d['one'] = 1
d['two'] = 2
print(d)
sum_1 = d['two'] + 8
print(sum_1)
print(d)
d['two'] = d['two'] + 8
print(d)
"""
OUTPUT:
{'make': 'bmw', 'model': '550i', 'year': 2016}
bmw
550i
{'one': 1, 'two': 2}
10
{'one': 1, 'two': 2}
{'one': 1, 'two': 10}"""
