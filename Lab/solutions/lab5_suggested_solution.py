#TASK 1
class MiniBank:

    def __init__(self, money):
        self.money = money

    # Sorting method that uses merge sort as seen in lectures
    def sort_bills(self, bills):
        if len(bills) > 1:
            mid = len(bills) // 2
            left = bills[:mid]
            right = bills[mid:]
            self.sort_bills(left)
            self.sort_bills(right)
            i = j = k = 0
            while i < len(left) and j < len(right):

                if left[i][1] > right[j][1]:
                    bills[k] = left[i]
                    i += 1
                else:
                    bills[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                bills[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                bills[k] = right[j]
                j += 1
                k += 1

    # Method that access the list and compares to a class variable money
    # Here there are alot of possible answers as long as your answer works correctly it is fine
    def pay_bill(self, bills):
        self.sort_bills(bills)
        i = 0
        while i != len(bills):
            if self.money < bills[i][1]:
                print("You cant pay the bill from", bills[i], 
                      " With your current balance of: ", self.money)
                i += 1
            elif self.money >= bills[i][1]:
                self.money -= bills[i][1]
                print("we pay the bill to", bills[i], " which amount to: ", bills[i][1],
                      " Current balance: ", self.money)
                i += 1
            



# def put_in_Money(self, amount): maybe add a method so that you can put in money to the system?
# def pay_a_friend(self, amount, friend): Maybe you want to pay a friend or a specific person?


bills = [("Strøm", 1234), ("Leie", 5000), ("Wolfram alpha", 200), ("Velvære", 5000)]
joe = MiniBank(6000)
joe.sort_bills(bills)
print(bills)
joe.pay_bill(bills)



#TASK 2
#A recursive method for the fibonacci list, not effective at all is O(2^N)
#Would be better if we could let this method have some sort of way of remembering....
def recur_fibo(n):

    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)

nterms = 7

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))



#TASK 3
#A
N = 15

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j -1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')


#B
def a_space_classic(n):
    z=n-1
    x=1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
        for i in range(0,x):
            print('+',end='')
        for i in range(0,z):
            print(' ',end='')
        x=x+2
        z=z-1
        print()
a_space_classic(5)


#EXTRA TASK
class Fridge:
    def __init__(self):
        self.temperature = 3
        self.open = False
        self.items = []

    def openFridge(self):
        self.open = True
        print ('The fridge is open.')

    def closeFridge(self):
        self.open = False
        print ('The fridge is closed.')

    def add(self, fridgeItem):
        if self.open == True:
            self.items.append(fridgeItem)
            print (f'{fridgeItem.name} is added.')

    def remove(self, fridgeItem):
        if self.open == True:
            self.items.remove(fridgeItem)
            print (f'{fridgeItem.name} has been removed.')

    def decreaseTemperature(self):
        self.temperature -= 1
        print (f'The temperature is set to {self.temperature}.')

    def increaseTemperature(self):
        self.temperature += 1
        print (f'The temperature is set to {self.temperature}.')


class FridgeItem:
    def __init__(self, name, date):
        self.name = name
        self.date = date


my_fridge = Fridge()

milk = FridgeItem('milk', '10.03.23')
cheese = FridgeItem('cheese', '12.04.23')
jam = FridgeItem('jam', '02.12.23')

my_fridge.increaseTemperature()

my_fridge.openFridge()
my_fridge.add(milk)
my_fridge.add(cheese)
my_fridge.add(jam)
my_fridge.remove(milk)
my_fridge.closeFridge() 

print(f'The items in the fridge are: {[item.name for item in my_fridge.items]}')

# for item in my_fridge.items:
#     print (item.name)