#1
 #The Big O complexity of the function is O(n^3)

#2

#The constant c is the upper bound of the function.
#That means that for when n is equal to 1 or more. The upper bound has to be equal or bigger.
#I found the constant by putting T(n) = O(f(n)) => T(n) = c*f(n) => then n = 1 => 16 = c.
#The constant is 16. 


#3

#a
#my_func1 has a nested while loop inside the for loop
#The while loop compares j with the the lenght of the inputs.
#Inside the while loop it doubles j for each iteration. J represents an index in the inputs.
#It goes from index 1 to 2 to 4 to 8 and so on.
#Henceworth the while loop is not O(n) but O(logn)
#The for loop is O(n)
#As a whole the function is O(nlogn)


#b #bubble sort function
#my_func2 has a nested for loop inside a for loop. 
#The function compares an element to every other element in the list whilst moving it up if it is bigger.
#Worst case it has to move every element.
#The O notation is O(n^2)


#4

s = [1, 2, 3]
def solve_problem_n2(s_list):
    n = len(s_list)
    a_list = []
    #The total list of As
    for i in range(n):
        #The A[i]
        a_stack = s_list[i]
        for j in range(i):
            a_stack += s_list[j]
        a_stack /= i+1
        a_list.append(round(a_stack, 2))
    return a_list

def solve_problem_n(s_list):
    n = len(s_list)
    a_list = [s_list[0]]

    for i in range(1, n):
        a_stack = s_list[i]
        a_stack += a_list[i-1]*(i)
        a_stack /= i+1
        a_list.append(round(a_stack, 2))
    return a_list

#I made this in O(n^2). For every n-th element, i add i elements to eachother and divide on the n-th number.
#For n = 2 I have 3 outer iterations. i=0 add the 0-th element of the list and divides on i+1. Then for the next. 

#I made the 2nd one n time. It stores the formulas, and one the next one it adds the previous but undos the division, then divides again.
print(solve_problem_n2(s))
print(solve_problem_n(s))
