l=[1,2,3,4,5,6,7,8,9]
l1=[]
l.reverse()
print(l)
print(l.count(1))
print(l.index(2))
l.insert(3,0)
print(l)
l.pop()
print(l)
l.remove(0)
l.append(10)
print(l)
l.extend(l1)
print(l)
l.sort()
print(l)
l1.copy()
print(l1)
l.clear()
print(l)
OUTPUT:[9, 8, 7, 6, 5, 4, 3, 2, 1]
1
7
[9, 8, 7, 0, 6, 5, 4, 3, 2, 1]
[9, 8, 7, 0, 6, 5, 4, 3, 2]
[9, 8, 7, 6, 5, 4, 3, 2, 10]
[9, 8, 7, 6, 5, 4, 3, 2, 10]
[2, 3, 4, 5, 6, 7, 8, 9, 10]
[]
[]

