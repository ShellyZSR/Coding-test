
#8.2.1 给属性指定默认值： self.属性名 =  默认值
#例：假设我们想在2020年也可以使用这个程序来进行汽车估价，怎么办？

#修改属性值方法一：对象的名称.属性名 = 修改值

# class Car():
#         '''汽车目前价值估计程序'''
#         def __init__(self,brand,model,year):
#
#                 self.brand = brand
#                 self.model = model
#                 self.year = year
#                 self.this_year = 2018 #this_year默认值为2018
#
#
#         def detection(self):
#                 duration = self.this_year - int(self.year) #改duration值
#                 price = 30 - 2 * duration
#                 long_name = '您的'+ self.brand +self.model + "到目前已经行驶了" + str(duration)+'年,' + "目前价值"+ \
#                             str(price) + '万。\n'
#                 return long_name
#         def information(self):
#                 information1 = '本公司感谢您咨询' + self.brand + self.model +'的估价！'
#                 return information1
# my_car = Car('Audi','A6','2012')
# my_car.this_year=2020 #在创建对象my_car时，强制给this_year一个值，于是2020将覆盖默认值2018
# result = my_car.detection()
# thanks = my_car.information()
# print(result,thanks)

#方法二：通过创建新的方法来修改

class Car():
        '''汽车目前价值估计程序'''
        def __init__(self,brand,model,year):

                self.brand = brand
                self.model = model
                self.year = year

        def mod_this_year(self,new_year): #new_year 2020
                self.this_year = new_year #将2020传递给this_year


        def detection(self):
                duration = self.this_year - int(self.year) #改duration值:2020-int(self.year)
                price = 30 - 2 * duration
                long_name = '您的'+ self.brand +self.model + "到目前已经行驶了" + str(duration)+'年,' + "目前价值"+ \
                            str(price) + '万。\n'
                return long_name
        def information(self):
                information1 = '本公司感谢您咨询' + self.brand + self.model +'的估价！'
                return information1
my_car = Car('Audi','A6','2012')
my_car.mod_this_year(2020) #将2020赋值给new_year,
result = my_car.detection()
thanks = my_car.information()
print(result,thanks)





























































