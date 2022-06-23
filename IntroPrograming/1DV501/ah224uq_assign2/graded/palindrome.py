# function to check string is
# palindrome or not
def is_palindrome(s):
    s = s.lower()
    s = remove(s)
    length = len(s)
    quit = length // 2
    for n in range(quit):
        equal = s[n] == s[length - (n + 1)]
        if equal:
            continue
        return False
    else:
        return True


def remove(s):
    for x in range(100):
        s = s.replace(chr(x), '')
    return s


print(is_palindrome("Was it a rat I saw?"))
print(is_palindrome("A nut for a jar of tuna"))
print(is_palindrome("Madam"))
print(is_palindrome("java"))
