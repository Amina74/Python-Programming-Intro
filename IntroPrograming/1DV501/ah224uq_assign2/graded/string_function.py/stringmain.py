from stringfunctions import first_last
import stringfunctions


#for testing string concatination
s = "Hello"
print("String 1:", s)
n = 5
str = s*n
h = stringfunctions.concat(s,n)
print(h)
 #count the nummber of time a character x occurs in a string
s = 'hello'
x = 'l' 
b = stringfunctions.count(s, x)
print(b)     
#A function reverse(s) that returns a string with all the characters in s in reverse order.
mytxt = stringfunctions.reverse("I wonder how this text looks like backwards")
print(mytxt)
#A function first_last(s) that returns the first and last characters in the string s.
s = "baby"
print(first_last(s)[0] + s[-1])
#A function has_two_X(s) that return True if the string contains exactly two instances of the character X, otherwise False.
s = "Xx"
print(stringfunctions.has_two_X(s))  
#A function has_duplicates(s) that returns True if the string s contains any duplicate characters, otherwise False.  
s = "hello"
if stringfunctions.has_duplicates(s):
    print("True")
else:
    print("False")