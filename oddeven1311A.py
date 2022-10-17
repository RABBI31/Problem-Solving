n = int(input())
for i in range(n):
    x, y = [int(x) for x in input().split()]
    even = x-y
    odd = y-x
    if(x == y):
        print('0')
    elif((x>y and even%2==0) or (y>x and even%2!=0)):
        print('1')
    else:
        print('2')
    