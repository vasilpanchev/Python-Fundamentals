class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * Circle.__pi

    def calculate_area(self):
        radius = self.diameter / 2
        return Circle.__pi * (radius ** 2)

    def calculate_area_of_sector(self, angle):
        part = angle / 360
        return self.calculate_area() * part


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
