class Rectangle:

    def __init__(self,width,length):
        self.width = width
        self.length = length
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.length)
    

class Square:
    
    def __init__(self,s1):
        self.s1 = s1
    
    def calculate_perimeter(self):
        return 4* self.s1



#write width first and then length in the parameters
rect1 = Rectangle(3,4)
print(rect1.calculate_perimeter())
sq1 = Square(7)
print(sq1.calculate_perimeter())