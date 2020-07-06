import math
class Quadratic:
    
    def __init__(self, a = 0, b = 0, c = 0):
        self.a = a
        self.b = b
        self.c = c
        
    def roots(self):
        root_1 = (-self.b + math.sqrt(self.b**2 - 4 * self.a * self.c)) / (2 * self.a)
        root_2 =  (-self.b - math.sqrt(self.b**2 - 4 * self.a * self.c)) / (2 * self.a)
        
        return round(root_1, 2), round(root_2, 2)
    
    def sum_of_roots(self):
        result = -(self.b / self.a)
        
        return round(result, 2)
    
    def product_of_roots(self):
        result = self.c / self.a
        
        return round(result, 2)
    
    def sum_of_squared_roots(self):
        result = (self.sum_of_roots()**2) - (2 * self.product_of_roots())
        
        return round(result, 2)
    
    def inverse_of_roots(self):
        result = self.sum_of_roots() / self.product_of_roots()
        
        return round(result, 2)