for row in range(5):
    for col in range(4):
        if row==2 or col==0 or col==3: 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()