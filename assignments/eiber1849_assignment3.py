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
        key_value = list[x][1]
        y = x - 1
        while y >= 0 and key_value > list[y]:
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
My plan to solve this task recursivly is to use backtracking. If a word is 5 letters long, then it has 5! unique permutations.
The first pass appends 5 permutations, the next 4 and so on.
This creates a tree structure where the combinations becomes smaller and smaller untill the base case.

My plan is to take out the first letter of the string, keep the rest of the letters in their positions(the stems), and place the letter in all possible positions in the stems.

For example 'abc' -> 'a' and 'bc', 'cb' -> 'abc', 'bac', 'bca', 'acb', 'cab', 'cba'

I used this video to get a better understanding: https://www.youtube.com/watch?v=4lIQCoG4MnY
'''

#Hardcode example off how the process works on a 3 letter word.
def permutations_abc(string):
    combinations = []

    if len(string) == 1:
        return [string]
    
    for char in string:
        string = string[:]
        trunk = string.replace(char, "", 1)
        
        if char + trunk[:2] not in combinations:
            combinations.append(char + trunk[:2])
        if trunk[1:] + char + trunk[:1] not in combinations:
            combinations.append(trunk[1:] + char + trunk[:1])
        if (trunk[:2] + char) not in combinations:
            combinations.append(trunk[:2] + char)
    
    return combinations

#The magic function that finds permutations

def magic_function(string):
    
    #Base case, if the lenght of the string is 1, then return the string in a list, which is the letter.
    if len(string) == 1:
        return [string]
    
    #Sets the bottom_stem to a base case. If the string is 'abc', then bottom_stem would be 'c'.
    permutations = []
    stems = magic_function(string[1:])
    letter = string[0]
    
    #Iterates through the characters in the stems. The it takes the index in a range based on the lenght of the stem and adds 1. The index can be 0,1,2.
    for stem in stems:
        for ind in range(len(stem)+1):
            permutations.append(stem[:ind] + letter + stem[ind:])

    return permutations

'''
The firt stem becomes 'c', and letter becomes 'b', it then creates the permutations 'cb' and 'bc'.
Then stems is equal to the permutations ['cb', 'bc'], and the letter is 'a'. 
It then goes throug the double loop and creates 3 permutations from 'cb' with 'a', and the same with 'bc'
Then it returns the permutations
'''
            
    

permutations = magic_function('abc')
print(permutations)