
def gab(lst):
    diff= max(lst) - min(lst)
    return diff
  
#main
mylist = [21700, 28200 ,26300,  25100, 22600, 22800, 19900 ]  
print(gab(mylist))  
#  diff_list = []
 #   for i in range(len(lst)-1):
  #      diff_list.append(lst[i] -lst[i+1])
   # return str(diff_list)     
