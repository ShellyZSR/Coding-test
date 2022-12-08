class Car():
    '''汽车目前价值估计程序'''

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.this_year = 2018

    def mod_this_year(self, new_year):
        self.this_year = new_year

    def detection(self):
        # duration = self.this_year - int(self.year)
        duration = int(self.this_year) - int(self.year)
        price = 30 - 2 * duration
        long_name = '您的' + self.brand + self.model + "到目前已经行驶了" + str(duration) + '年,' + "目前价值" + \
                    str(price) + '万。\n'
        return long_name

    def information(self):
        information1 = '本公司感谢您咨询' + self.brand + self.model + '的估价！'
        return information1




class ElectricCar(Car):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def battery(self, capacity):
        self.capacity_num = capacity
        print("您选择的电池容量为：", self.capacity_num, 'kWh')

    def detection(self):
        duration = int(self.this_year) - int(self.year)
        price = 30 - duration - (500 / self.capacity_num)
        long_name = '您的' + self.brand + self.model + "到目前已经行驶了" + str(duration) + '年,' + "目前价值" + \
                        str(price) + '万。\n'
        return long_name