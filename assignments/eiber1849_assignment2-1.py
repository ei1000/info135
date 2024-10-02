#1

"""
original list = [ 1001, 1030, 1050, 1020, 300, 1080, 1100]
algo = insertion

1st_pass = [ 300, 1030, 1050, 1020, 1001, 1080, 1100]
2nd_pass = [ 300, 1001, 1050, 1020, 1030, 1080, 1100]

#Answer
3rd_pass = [ 300, 1001, 1020, 1050, 1030, 1080, 1100]

"""

#2

"""
original list = [ 210, 15, 111, 90, 45, 120, 150, 200, 100, 140 ]
algo = bubble

1st_pass = [ 15, 111, 90, 45, 120, 150, 200, 100, 140, 210 ]
2nd_pass = [ 15, 90, 45, 111, 120, 150, 100, 140, 200, 210 ]

#Answer
3rd_pass = [ 15, 45, 90, 111, 120, 100, 140, 150, 200, 210 ]
"""

#3

#Implementerer inscertion sort, slik som er gjort i presentasjonen.
def insertion_sort(list):
    for x in range(1, len(list)):
        key = list[x]
        y = x - 1
        while y >= 0 and key < list[y]:
            list[y+1] = list[y]
            y -= 1
            list[y + 1] = key


#Lager funksjonen som sorterer og fjerner duplikater.
def sort_and_rem_dup(liste):
    #For å ikke modifisere den originale listen, så lager jeg en kopi
    ny_liste = liste[:]

    #Bruker insertion_sort funksjonen her
    insertion_sort(ny_liste)

    #Lager en ny liste som ikke skal ha duplikater
    no_dupe_liste = []

    #Itererer gjennomden sorterte listen 'ny_liste', og legger til elementet i iterasjonen, hvis det ikke allerede er i listen uten duplikater.
    #Man kan også gjøre dette med å lage et dictionary, men dette er den enkleste måten.
    for x in ny_liste:
        if x not in no_dupe_liste: 
            no_dupe_liste.append(x)
    return no_dupe_liste

liste = [1,6,7,2,9,9,9]
liste = [5,4,3,2,1,2,3,4,5]
ny_liste = sort_and_rem_dup(liste)

print(liste)
print(ny_liste)


#4

#Implementerer stack, med nodvendige metoder.
class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

#Implementerer queue, med nodvendige metoder.
class Queue:
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()


"""
Stack vil plassere forste element pa bunnen, og "stacke" opp paa dem. Queue vil plassere forste fremst, og legge til etter. 

Da er queue lik stack baklengs. Ved aa bruke pop metoden vil siste element i stacken returneres og fjernes, ved dequeue vil forste element returneres og fjernes.

Om disse to elementene er like for alle posisjonene av ordet, saa er det et palindrom. Hvis det som dequeues og poppes er forksjellig, saa er det ikke et palindrom  

stack = ['e', 'i', 'n', 'a', 'r']
queue = ['r', 'a', 'n', 'i', 'e']

'einar' er ikke et palindrom
"""

#Implementerer check_palindrome funksjonen
def check_palindrome(word):
    
    #Lager klasse objekt.
    word_stack = Stack()
    word_queue = Queue()

    #Bygger dem med bokstavene fra ordet
    for x in word.lower().strip(): #Incase the word has unwanted symbols or capital letters.
        word_stack.push(x)
        word_queue.enqueue(x)

    #Checking if the pop values compare.
    for x in range(0, len(word)):
        if word_stack.pop() != word_queue.dequeue():
            return 'Not Palindrome'
    return 'Palindrome'

result = check_palindrome('hello')
print(result)
result = check_palindrome('civic')
print(result)

