#8.3继承：
# 当一个机器人的功能不能满足现在的需求，我们可以保留原有功能，并开发升级新功能，这时就可以使用继承
#1。当编写的类是另一个现成类的特殊版本，可使用继承
#2。一个类继承另一个类时，它将自动获得另一个类的所有属性（e.g. self.brand = brand)和方法(e.g. detection(self))
#3. 原来的类称为父类，而新的类称为子类
#4. 父类代码必须写在子类代码前，且父类和子类必须同在一个文件里面

class Car(): #父类
        '''汽车目前价值估计程序'''
        def __init__(self,brand,model,year):

                self.brand = brand #可通过对象访问的变量称为属性
                self.model = model
                self.year = year
                self.this_year = 2018

        # def mod_this_year(self,new_year):
        #         self.this_year = new_year

        def detection(self):
                # duration = self.this_year - int(self.year)
                duration = int(self.this_year) - int(self.year)
                price = 30 - 2 * duration
                long_name = '您的'+ self.brand +self.model + "到目前已经行驶了" + str(duration)+'年,' + "目前价值"+ \
                            str(price) + '万。\n'
                return long_name

        def information(self):
                information1 = '本公司感谢您咨询' + self.brand + self.model +'的估价！'
                return information1

# my_car = Car("Audi","A6",2013)
# my_car.mod_this_year(2020)
# result = my_car.detection()
# print(my_car.year)
# print(result)
# # 2013
# # 您的AudiA6到目前已经行驶了7年,目前价值16万。

class ElectricCar(Car): #子类 父类需位于子类前
        def __init__(self,brand,model,year): #参数跟父类名参数一样
            super().__init__(brand,model,year) #关联子类和父类
#通过这两行代码，对子类进行初始化，使子类具备父类所有功能（属性和方法）

        def battery(self,capacity):
                self.capacity_num = capacity
                print("您选择的电池容量为：",self.capacity_num,'kWh')
        #5. 在子类里定义的方法，只能通过子类创建的对象中使用该方法，不能在通过父类创建的对象中使用
        #6。父类定义的方法，子类都可以使用

        def detection(self): #想要更改方法detection()，重写父类即可，父类中的该方法将会被覆盖
            duration = int(self.this_year) - int(self.year)
            price = 30-duration-(500/self.capacity_num)
            long_name = '您的' + self.brand + self.model + "到目前已经行驶了" + str(duration) + '年,' + "目前价值" + \
                    str(price) + '万。\n'
            return long_name



my_tesla = ElectricCar('Tesla','model_s','2017')
print(my_tesla.year)
my_tesla.battery(100)
my_tesla.this_year = 2021
result1 = my_tesla.detection()
print(result1)
















































