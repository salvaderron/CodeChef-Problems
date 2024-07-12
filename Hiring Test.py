a=int(input())
for i in range(a):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    for j in range(n):
        arr=list(input())
        p=arr.count('P')
        f=arr.count('F')
        if f>=x:
            print(1,end="")
        elif f==(x-1) and p>=y:
            print(1,end="")
        else:
            print(0,end="")
    print()
