for row in range(5):
    for col in range(5):
        if  col==0 or col==4 or col-row==0 : 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()