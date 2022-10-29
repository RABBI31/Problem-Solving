for i in range(n):
    x,y = [int(x) for x in input().split()]
    if(x == 1):
        print('0')
    elif(x == 2 and y == 2):
        print('2')
    elif(x >= 2 ):
        print(y*2)