for _ in range(int(input())):
    n=input()
    s=input()
    a=0
    for i in s:
        if (i=='Q'): 
            a+=1
        else : 
            a=max(0,a-1)
    if(a>0):
        print('No')
    else:
        print("Yes")
    
    