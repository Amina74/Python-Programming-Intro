def odd(lst):
    n = []
    for i in lst:
        if i % 2 == 1:
          n.append(i) 
    return n           
#main
mylst = [1,4,7,8,9,5,3]
new_list = odd(mylst)
print(new_list)

