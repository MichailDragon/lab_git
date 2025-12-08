class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return F'Марка: {self.make}, Модель: {self.model}'
    
class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        ggget_info = super().get_info()  
        return f"{ggget_info}, Тип топлива: {self.fuel_type}"

make = "Dodge"
model = "Challenger SRT Hellcat"
fuel_type = "Бензин"

carcar = Vehicle(make, model)
print(carcar.get_info())

carcarcar = Car(make, model, fuel_type)
print(carcarcar.get_info())





