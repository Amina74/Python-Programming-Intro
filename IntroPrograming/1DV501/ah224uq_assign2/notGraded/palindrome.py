 # str is text to be checked,
# p and q are first and last positions in text 
def is_palindrome_rec(str, p, q):
    if q <= p:
        return True
    elif str[p] != str[q]:
        return False
    else:
        return is_palindrome_rec(str, p+1, q-1)
# Programs starts
s = input("Enter a string ")

if is_palindrome_rec(s, 0, 4):
    print(s, " is a simple palindrome")
else:
    print(s, " is not a simple palindrome")
