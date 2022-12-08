#8.2 类（class)
class Car():
        '''汽车目前价值估计程序'''
        def __init__(self,brand,model,year):
                self.brand = brand
                self.model = model
                self.year = year
        def detection(self):
                duration = 2018 - int(self.year)
                price = 30 - 2 * duration
                long_name = '您的'+ self.brand +self.model + "到目前已经行驶了" + str(duration)+'年,' + "目前价值"+ \
                            str(price) + '万。\n'
                return long_name
        def information(self):
                information1 = '本公司感谢您咨询' + self.brand + self.model +'的估价！'
                return information1
my_car = Car('Audi','A6','2012')
result = my_car.detection()
thanks = my_car.information()
print(result,thanks)

your_car = Car('Mercedes-Benz','c200','2007')
result = your_car.detection()
thanks = your_car.information()
print(result,thanks)

# 您的AudiA6到目前已经行驶了6年,目前价值18万。
#  本公司感谢您咨询AudiA6的估价！
# 您的Mercedes-Benzc200到目前已经行驶了11年,目前价值8万。
#  本公司感谢您咨询Mercedes-Benzc200的估价！































