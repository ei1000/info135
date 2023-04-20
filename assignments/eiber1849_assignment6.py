#1 
#pre-order always starts on the root, therefore it has tobe A or B. Pre-order explores the deepness of the nodes on each side. 
#In other words it traverses the left side first, then the right side. 
#The correct answer is A 


#3
from math import pi, sqrt

class Shape:
    def compute_area(self):
        pass

class Square(Shape):
    def __init__(self, side) -> None:
        self.side = side

    def compute_area(self):
        print(f'The area of the square is: {self.side*self.side}')
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def compute_area(self):
        print('The are of the circle is: %0.2f' % ((self.radius**2)*pi))

class Triangle(Shape):
    def __init__(self, side_one, side_two, side_three) -> None:
        self.a = side_one
        self.b = side_two
        self.c = side_three

    def compute_area(self):
        s = (self.a+self.b+self.c)/2
        area = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        print(f'The area of the triangle is: {area}')

my_square = Square(2)
my_circle = Circle(2)
my_triangle = Triangle(5, 4, 3)
print('Area of square:', end=' ')
my_square.compute_area()
print('Area of circle:', end=' ')
my_circle.compute_area()
print('Area of triangle:', end=' ')
my_triangle.compute_area()

#4

class House:
    count = 0
    def __init__(self, owner, condition, price) -> None:
        self.owner = owner
        self.price = price
        self.condition = condition

        self.cost = 0
        self.sold = False
        House.count += 1
    
    def sell(self, new_ownser):
        self.owner = new_ownser
        self.sold = True
        profit = self.price-self.cost
        print('House has been sold! Profit: ', profit)

    def change_price(self, new_price):
        if self.sold == True:
            print('House has been sold!')
        else:
            self.price = new_price
    
    def renovate(self, expense, new_condition):
        self.cost += expense
        self.condition = new_condition
        print('House has ben renovated!')

    def print_info(self):
        print(self.owner, self.condition, self.price)


house1 = House('John', 'good', 100000)
house2 = House('Sara', 'bad', 250000)

house1.print_info()
house2.print_info()
house1.renovate(50000, 'great')
house1.sell('Leo')
house1.print_info()
print(house2.count)
