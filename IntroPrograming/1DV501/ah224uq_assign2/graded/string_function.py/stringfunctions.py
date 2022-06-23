#string concatnation
def concat(s,n):
  return (s * n)

#count the nummber of time a character x occurs in a string

def count(s, x):
    cot =0   
    for i in s:
        if i == x:
            cot= cot + 1
        return cot    

# A function reverse(s) that returns a string with all the characters in s in reverse order.
def reverse(s):
     return s[::-1] 

#A function first_last(s) that returns the first and last characters in the string s.
def first_last(s):
    x = ''
    for i in s:
        x = i + x
        return x

#A function has_two_X(s) that return True if the string contains exactly two instances of the character X, otherwise False.
def has_two_X(s): 
    x = ''
    no_of_X= 0
    for i in s:
        if i == 'X':
             no_of_X += 1
    if  no_of_X == 2:
        return True
    return False

#A function has_duplicates(s) that returns True if the string s contains any duplicate characters, otherwise False.    
def has_duplicates(s):
     for i in range(len(s)):
        for y in range(i + 1, len(s)):
            if s[i] == s[y]:
                return False
            return True
  

         


