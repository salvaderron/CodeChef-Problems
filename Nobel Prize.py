x=int(input())
for i in range(x):
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))
    li=set(arr)
    if len(li)<m:
        print("Yes")
    else:
        print("No")
