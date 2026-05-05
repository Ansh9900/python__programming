#* OOPS
#! class and object
# class car:
#     brand = "ford"
#     color = "black"
#     hp = 1000
# car1 = car()
# car2 = car()
# print(car1.brand)
# print(car1.color)
# print(car1.hp)
# car.color = "yellow"
# print(car1.brand)
# print(car1.color)
# print(car1.hp)
# car2.color = "green"
# print(car2.brand)
# print(car2.color)
# print(car2.hp)
#!methods - data managment
class car:
    brand = "Ford"
    hp = 2000
    color = "black"
    def detail(cls,name,seater):
        cls.name = name
        cls.seater = seater
        cls.price = 99
car1 = car()
car1.detail("mustang",5)
print(car1.name)