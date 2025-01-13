for row in range(4):
    for col in range(3):
        if row==0 or row==3 or col==0: 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()