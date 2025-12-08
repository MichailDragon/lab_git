class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius

circle = Circle(10)
print("Радиус: ", circle.get_radius())

try:
    new_radius = float(input("Введите новый радиус круга: "))
    circle.set_radius(new_radius)
    print("Новый радиус круга:", circle.get_radius())
except ValueError:
    print("Ошибка: введено не число!")

