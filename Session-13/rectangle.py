from shape import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height



small_rectangle = Rectangle(2.34,0.75)
area = small_rectangle.area()

print(f"The Small rectangle has an ara of {area:.3f}")