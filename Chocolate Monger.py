x=int(input())
for i in range(x):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    arr=set(arr)
    rem=n-x
    if len(arr)>rem:
        print(rem)
    elif len(arr)<rem:
        print(len(arr))
    else:
        print(rem)
