n = int(input())
for i in range(n):
    num = input()
    res = [int(x) for x in str(num)]
    sum1 = sum(res[:3])
    sum2 = sum(res[3:])
    if(sum1 == sum2 ):
        print("YES")
    else:
        print("NO")