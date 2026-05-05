class car:
    brand = None
    color = None
    hp = None
obj1 = car()
obj2 = car()
obj3 = car()

obj1.brand = "BMW"
obj1.color = "red"
obj1.hp = "1000"

obj2.brand = "legender"
obj2.color = "white"
obj2.hp = "1000"

obj3.brand = "mustang"
obj3.color = "yellow"
obj3.hp = "1000"
print(obj1.brand)
print(obj1.color)
print(obj1.hp)
print(obj2.brand)
print(obj2.color)
print(obj2.hp)
print(obj3.brand)
print(obj3.color)
print(obj3.hp)

#!changes
# car.color = "white"
# print(car.color)
# print(obj1.color)
# print(obj2.color)
# obj1.color = "red"
# print(car.color)
# print(obj1.color)
# print(obj2.color)
# car.color = "blue"
# print(car.color)
# print(obj1.color)
# print(obj2.color)
