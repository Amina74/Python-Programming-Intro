identifier =input("Enter a chess square identifier:")

positive = int(identifier[1])
colum = identifier[0]



if colum in 'a' 'b''c' 'd''e' 'f''g' 'h' and (positive %2 ==0 and positive <=8) :
    print(identifier,"is white")


elif colum in 'a' 'b''c' 'd''e' 'f''g' 'h' and (positive %2 ==1 and positive <=8) :
    print(identifier,"is black")
else:
    print("Not a valid entry")    