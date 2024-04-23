# # my_tuple = (1, 2)
# # # print(my_tuple[0])
# # # Pythonic
# from collections import namedtuple
#
# #
# # Point = namedtuple('Point', ['x', 'y'])
# # p1 = Point(3, 4)
# #
# # print(p1.y)
# # # print(type(namedtuple))
#
# person = ('John', 24, 'john@gmail.com')
#
# Person1 = namedtuple('Person', ['full_name', 'age', 'email'])
# john = Person1('John', 24, 'john@gmail.com')
# # print(john[0])
# john.name = 'Alisher'
# # print(Person1)
# # print(john)
#
# # class Person:
# #     def __init__(self, full_name, age, email):
# #         self.full_name = full_name
# #         self.age = age
# #         self.email = email
# #
# # Person2  = Person
# # print(Person2)


# from collections import namedtuple
#
# Point = namedtuple('Point', ['x', '_y'])
# p1 = Point(3, 4)
# print(p1)


# my_tuple = (10, 20, ('john', 'is_active'), 23)
# print(id(my_tuple))
# my_tuple[2].append('mike')
# print(id(my_tuple))
# print(hash(my_tuple))
from collections import namedtuple

# Person = namedtuple("Person", ['name', 'children'])
# p1 = Person('John Doe', ['Mike', 'Anna'])
# print(id(p1.children))
# p1.children.append('Tom')
# # print(p1)
# print(id(p1.children))

from collections import namedtuple

# Person = namedtuple('Person', ['full_name', 'age', 'gender'], defaults=[24, 'male'])
# john = Person('John')
# print(john)

# Person = namedtuple("Person", "name age height")
# l1 = [25,'Jane', 1.75]
# jane = (Person._make(l1))
# print(jane.height)
#
# print(jane._asdict())


Car = namedtuple('Car', ['model', 'color', 'year'])
# args = ['Mercedes', 'white', 2024]

# db = {'model': 'BMW', 'color': 'black', 'year': 2024}
# print(Car(**db))

# bmw = Car('Bmw', 'black', 2023)
# new_car = bmw._replace(color='white')
# print(new_car.color)


# my_list = [10, 20, 30]
# print(len(my_list))
# print(max(my_list))
# print(min(my_list))


# print(my_arr[1:]) # [20,30,40,50]

# print(my_arr[0:3]) # 10  , 20 ,30
# print(my_arr[0::2])  # my_arr[start:stop:step]
# print(my_arr[::-1])
# message = 'Hello'
# print(message[::-1])
# print(my_arr[-1::])

# print(my_arr[1:8:3])
# my_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# print(my_arr[-6:-1:2])
# t1 = [1, 2, 3]
# t2 = [1, 2, 3]
# print(id(t1))
# print(id(t2))

# number = ('Hello',)
# print(type(number))
#
# my_tuple1 = (10, 20, 30)
# my_tuple2 = tuple({40, 50})
# my_tuple1 = (my_tuple1 + my_tuple2)
# print(my_tuple1)
# db = (10,)
# for i in db:
#     print(i)
