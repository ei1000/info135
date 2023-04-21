#1 
#pre-order always starts on the root, therefore it has tobe A or B. Pre-order explores the deepness of the nodes on each side. 
#In other words it traverses the left side first, then the right side. 
#The correct answer is A 
print('\nPre-order starts on the root, goes left to the bottom, then right to the bottom. The correct answer is A')

#2
#For this code i borrowed the example solution in lab10 as part of compute_result. 
#I could have put it together into one function, but I split it into two sub functions, in case the class would be expanded and used in other general terms.
#I modified it to work with the task, and I have commented to show that I understand how it is implemented.
#The approach is quite similar to the knapsack problem, where each items weight and value is changed to question with time and points.


class QuizGift:
    def __init__(self, time) -> None:
        self.tasks = []
        self.times = []
        self.points = []
        self.time = time

    def add_question(self, task, points, times):
        self.tasks.append(task)
        self.points.append(points)
        self.times.append(times)
    
    def add_mul_questions(self, tasks, points, times):
        self.tasks.extend(tasks)
        self.points.extend(points)
        self.times.extend(times)
    
    def change_time(self, time):
        self.time = time
    
    def question_matrix(self):
        #Creating a 0-matrix with the amount of time as columns, so here it has 100 calums, and as many rows as questions.
        matrix = [[0 for _ in range(self.time + 1)] for _ in range(len(self.times) + 1)]
        
        #For every row and column
        #If the time of the task is less than or equal to the column, then you choose the maximum between including the task or not it (the colunm in the previous row).
        #Else put the column from the previous row as this column.
        
        #So the first row we get a 0 row.
        #The next row we continue with 0 to row 2 column times[1]. Here we compare points[1] + 0 to the same column in the row above.
        #The points[1] is larger, so it gets added for every element in the row.
        #The next row3, adds points[1] untill times[2] <= column. Then it chooses the max again and so on for every 
        for row in range(len(self.times) + 1):
            for column in range(self.time + 1):
                #Base case
                if row == 0 or column == 0:
                    matrix[row][column] = 0
                
                #To be or not to be
                elif self.times[row - 1] <= column:
                    matrix[row][column] = max(self.points[row - 1] + matrix[row - 1][column - self.times[row - 1]], matrix[row -
                    1][column])
                
                #Previous row.
                else:
                    matrix[row][column] = matrix[row - 1][column]
        
        #Returning the solution matrix.  
        return matrix

    #Returning the max points.
    def max_points(self):
        return self.question_matrix()[len(self.tasks)][self.time]

    def find_tasks(self):
        #Mapping the time and task on the strategy
        strategy_time = []
        strategy_task = []

        questions = len(self.points)

        #Creating a matrix like before.
        matrix = self.question_matrix()
        
        #Finding the best score
        temp_points = matrix[questions][self.time]
        
        #Variable for max time
        cap_time = self.time

        #For every question from last to first. If the amount of points is equal to The last column in the row numbered question.nr - 1, then go to the next question.
        #Either the value is from the top, or from an item that is included. Then if it is from included, you remove the value of the item, and continue.
        for i in range(questions, 0, -1):
           #I removed this breaker, because it would  
            if temp_points <= 0:
                break

            #If the item is at the top.
            if temp_points == matrix[i - 1][cap_time]:
                continue
            else:
                #else add the task to the strategy and remove the time. 
                    #Adding the time of the task to strategy times, and adding the task number to the strategy task. 
                    strategy_time.append(self.times[i-1])
                    #In case some questions is not named after whole numbers.
                    strategy_task.append(self.tasks[i-1])
                    
                    #Removing the points of the task from the max points. Same with the time from the max time.
                    temp_points = temp_points - self.points[i - 1]
                    cap_time = cap_time - self.times[i - 1]
        
        #Returning the times and tasks in a tuple of two lists.
        return strategy_time, strategy_task

    #I know this adds complexity because I find the solution 2 times. 1 time in max_points, and another time in find_tasks. But I have tried to split it in the spirit of OOP.
    def compute_result(self):
        points = self.max_points()
        times, tasks = self.find_tasks()
        time = self.time - sum(times)

        if points > 750:
            prize = 'a laptop'
        elif points > 250:
            prize = 'a smartphone'
        else:
            prize = 'a watch'

        return points, sorted(map(lambda x: f'question {x}',tasks)), time, prize
    
    def print_result(self):
        points, tasks, time, prize = self.compute_result()
        print(f'If Sara does the following: {", ".join(tasks)}.\nThen she can score {points} points in {self.time} minutes, with {time} minutes to spare.\nShe will then recieve {prize} as the prize\n')


quiz1 = QuizGift(100)
quiz1.add_mul_questions([1,2,3,4,5,6], [120, 200, 150, 350, 100, 90], [15, 20, 40, 50, 20, 10])
#print(f'Tasks: {quiz1.tasks} | Points: {quiz1.points} | Times: {quiz1.times} | Total time: {quiz1.time} min')
#print('Max points:', quiz1.max_points())
#print(quiz1.find_tasks())
quiz1.print_result()


#3
from math import pi, sqrt
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
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
print('')



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
    
    def sell(self, new_owner):
        self.owner = new_owner
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
        print('House renovated!')

    def print_info(self):
        print(f'Owner: {self.owner}, Condition: {self.condition}, Price:', '{} $'.format(self.price))


house1 = House('John', 'good', 100000)
house2 = House('Sara', 'bad', 250000)

house1.print_info()
house2.print_info()
house1.renovate(50000, 'great')
house1.sell('Leo')
house1.print_info()
print('Total number of houses:', house2.count)
