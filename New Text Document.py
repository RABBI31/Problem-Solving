t = int(input())
for i in range(0,t):
    n = int(input())
    s = input()
    ForQ = s.count("Q")
    ForA = s.count("A")
    if(ForQ <= ForA):
        print("Yes")
    else:
        print("No")
    