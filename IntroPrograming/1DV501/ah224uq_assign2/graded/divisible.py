count = 0
for i in range (100,200):
    if (i % 4 == 0 and i % 5 != 0) or(i % 5 ==0 and i % 4 !=0) :
        count += 1
        print(i, end=" ")
        if count % 10 == 0:
            print()
        
       
