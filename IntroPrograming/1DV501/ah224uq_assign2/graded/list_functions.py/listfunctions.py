from random import randint 
#A function random_list(n) that returns a list containing n random integers in the interval 1 to 100.
def random_list(n):
    n = []
    for i in range (10):
        rnd = randint(1,100)
        n.append(rnd)
    return n   

#A function average(lst) returning the average (a rounded off integer) of all values in the list lst.
def average(lst):
    avrg = round(sum(lst) / len(lst))
    return avrg

#A function only_odd(lst) that returns a new list containing only the odd integers in lst.
def only_odd(lst):
    count = []
    for i in lst:
        if i % 2 == 1:
           count.append(i)
    return count      

# A function to_string(lst) that returns a comma separated string representation (a single string) of the elements in lst.
def to_string(lst):
    nums = []
    for num in lst:
        nums.append(str(num))
    string = ",".join(nums)
    string = "[" + string + "]"
    return string

#A function contains(lst,a,b) that returns True if a is directly followed by b anywhere in the list lst.
def contains(lst, a, b):
    for num in lst:
        if num == a:
            if lst[lst.index(a) + 1] == b:
                return True
    return False



#A function has_duplicates(lst) that returns True if the list lst contains any duplicate elemments, otherwise False.
def has_duplicates(lst):
    for i in lst:
        if lst.count(i) >1:
            return True
    return False        

