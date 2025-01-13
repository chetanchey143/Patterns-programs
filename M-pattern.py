for row in range(5):
    for col in range(6):
        if  col==1 or col==5 or row*col==2 or col-row==3 : 
            print("X",end=" ")
        else:
            print(" ",end=" ")
    print()