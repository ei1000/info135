




















































































































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