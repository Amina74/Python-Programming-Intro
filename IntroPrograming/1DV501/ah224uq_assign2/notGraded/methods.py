def has_XandY(str):
    x , y = False, False
    for c in str:
      if c == 'X' or c == 'x':
          x = True
      elif c == "Y" or c == 'y':
          y = True
    return x and y       

def test_and_print(s):
    if has_XandY(s):
        print(s, "Contains both X and Y")
    else:
        print(s, "doesnt contain both Xand Y")    

 #programs starts     
n = input("Enter a string ")

has_XandY(n)
test_and_print(n)
