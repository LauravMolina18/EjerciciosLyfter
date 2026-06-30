#Cree una clase de Circle con:
#Un atributo de radius (radio).
#Un método de get_area que retorne su área.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.1416 * self.radius ** 2
        return area
    
circle1 = Circle(4)
print(circle1.get_area())
        
