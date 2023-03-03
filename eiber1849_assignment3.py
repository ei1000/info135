#1

'''
first str is 5
2nd str is 9
3rd is 16
4rth is 6.
'''

def hash_function(input_str, table_size):
    total = 0
    lenght = len(input_str)
    for char in input_str:
        total += ord(char) + lenght
    return total % table_size



#2
import random
import hashlib as hl

class HashClass:
    def __init__(self, id) -> None:
        self.id = id

    def hash_it(self):
        salt = random.randint(1,1000)
        hash_str = hl.sha1(repr(salt+self.id).encode()).hexdigest()
        return hash_str
    
    def print_it(self):
        print(self.hash_it())

hash_table = HashClass(2)
hash_table.print_it()

#3

list_of_tuples = [('lalalal', 5), ('abc', 2), ('bce', 3)]

def insertion_sort(list):
    for x in range(1, len(list)):
        key = list[x]
        y = x - 1
        while y >= 0 and key > list[y]:
            list[y+1] = list[y]
            y -= 1
            list[y + 1] = key



def sort_and_print(list):
    insertion_sort(list)
    print(f'The movie with the largest budget is:\n{list[0][0]}')

sort_and_print(list_of_tuples)

#4

def most_frequent_integer(list):
    #Makes an empty dictionary
    number_dict = {}
    #Makes a duple with the key and count
    most_frequent = ('',0)
    
    #Adds the number to the dictionary as a key, and everytime the key already exist, the value gets updated.
    for number in list:
        if str(number) in number_dict.keys():
            number_dict[str(number)] += 1
        else:
            number_dict[str(number)] = 0
    
    #Iterates through the entries in the dictionary
    for key, count in number_dict.items():
        if count > most_frequent[1]:
            most_frequent = (key, count)
    return most_frequent[0]

new_dict = {}


number_list= [1,1,1,1,1,1,0,0,0,4,3,2, 99, 420, 57,57,57,57,57,57,57,57]
result_freq = most_frequent_integer(number_list)
print(result_freq)


#5
'''
My plan to solve this task recursivly is to use combinatorics. If a word is 5 letters long, then it has 5! different permutations.
The first pass appends 5 permutations, the next 4 and so on.
This creates a tree structure where the combinations becomes smaller and smaller untill the base case.
'''


def magic_function(string):
    string = [*string]
    lenght = len(string)
    permutations = []

    #base case, returns a copy of the last letter.
    if lenght == 1:
        return [string]
    
    #Recursive call

    for num in range(lenght):
        char = string.pop(0)

        perms = magic_function(string)

        for perm in perms:
            perm.append(char)
        permutations.extend(perms)
        string.append(char)
    return permutations

def magic_function(string):
    string = [*string]
    lenght = len(string)
    permutations = []

    #base case, returns a copy of the last letter.
    if lenght == 1:
        return [string]
    
    #Recursive call

    for num in range(lenght):
        char = string.pop(0)

        perms = magic_function(string)

        for perm in perms:
            perm.append(char)
        permutations.extend(perms)
        string.append(char)
    return permutations

    

permutations = magic_function('abcd')
print(permutations)