from AreaCalcul import Rectangle, Square, Circle

Rect_1 = Rectangle(5, 10)
Rect_2 = Rectangle(1, 3)

print(Rect_1.get_area_rectangle())
print(Rect_2.get_area_rectangle())

Square_1 = Square(2)
Square_2 = Square(4)

print(Square_1.get_area_square())
print(Square_2.get_area_square())

Circle_1 = Circle(2)
Circle_2 = Circle(4)

print(Circle_1.get_area_cricle())
print(Circle_2.get_area_cricle())

figures = [Square_1, Circle_2, Rect_1, Circle_1, Square_2, Rect_2]

for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_area_rectangle())

    elif isinstance(figure, Square):
        print(figure.get_area_square())

    else:
        print(figure.get_area_cricle())


