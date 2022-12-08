#8.4导入类：
# Python可以将类存储在模块(不同文件)中，然后在主程序中导入所需要的模块。
#1. 导入单个类：from 模块名 import 类名
# from Car_file import Car
# from Car_file import ElectricCar
#
# my_car = Car("Audi","A6",2013)
# my_car.mod_this_year(2020)
# result = my_car.detection()
# print(my_car.year)
# print(result)
# my_tesla = ElectricCar('Tesla','model_s','2017')
# print(my_tesla.year)
# my_tesla.battery(100)
# my_tesla.this_year = 2021
# result1 = my_tesla.detection()
# print(result1)
#
# 2。从一个模块中导入多个类：from 模块名 import 类名1,类名2,…（回车）
from Car_file import Car,ElectricCar
my_car = Car("Audi","A6",2013)
my_car.mod_this_year(2020)
result = my_car.detection()
print(my_car.year)
print(result)
my_tesla = ElectricCar('Tesla','model_s','2017')
print(my_tesla.year)
my_tesla.battery(100)
my_tesla.this_year = 2021
result1 = my_tesla.detection()
print(result1)


#3。导入整个模块：
# import 模块名(给一个入口进入文件名）
# 模块名.A1()（类名，通过此使用类）
# 模块名.A2()

# import Car_file
# my_car = Car_file.Car("Audi","A6",2013) #通过模块名.类名A1使用类
# my_car.mod_this_year(2020)
# result = my_car.detection()
# print(result)
#
# my_tesla = Car_file.ElectricCar('Tesla','model_s','2017')
# my_tesla.battery(100)
# my_tesla.this_year = 2021
# result1 = my_tesla.detection()
# print(result1)

# 4。导入模块中的所有类：from 模块名 import *
from Car_file import *
#通过 * 号将模块名里的所有类一次性复制过来，但尽量不要使用这种方法，会使程序不稳定
my_car = Car("Audi","A6",2013) 
my_car.mod_this_year(2020)
result = my_car.detection()
print(result)

my_tesla = ElectricCar('Tesla','model_s','2017')
my_tesla.battery(100)
my_tesla.this_year = 2021
result1 = my_tesla.detection()
print(result1)































