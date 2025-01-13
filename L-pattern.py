for row in range(5):
    for col in range(3):
        if  col==0 or row==4 : 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()