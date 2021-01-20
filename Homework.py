class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


Rectangle_1 = Rectangle(5, 10, 50, 100)

Test = [str(Rectangle_1.x), str(Rectangle_1.y), str(Rectangle_1.width), str(Rectangle_1.height)]
print(Test)
