class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area_calcul(self):
        return self.width * self.height / 2


Trial_1 = Triangle(5, 10)

print(Trial_1.area_calcul())
