import listfunctions
#A function random_list(n) that returns a list containing n random integers in the interval 1 to 100.
mylist = listfunctions.random_list(10)
print(mylist)
print()
# A function average(lst) returning the average (a rounded off integer) of all values in the list lst.   
myls= [1,4,6,7,6,3,8,9,0,4,3,2,4]
s = listfunctions.average(myls)
print(s)
print()
#main
mylst = [1,4,7,8,9,5,3]
new_list = listfunctions.only_odd(mylst)
print(new_list)

# converting list of integers to single string
mylist = [1,2,4,5]
print(listfunctions.to_string(mylist))

#main contains(lst,a,b)
print(listfunctions.contains([1, 2, 3, 4], 2, 4))    

#main has_duplicates(lst)
listOfElems = ['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']
result = listfunctions.has_duplicates(listOfElems)
print(result)

