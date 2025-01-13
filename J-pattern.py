for row in range(7):
    for col in range(5):
        if row==0 or col==2 or row-col==5: 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()