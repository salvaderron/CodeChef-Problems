# cook your dish here
x=int(input())
for i in range(0,x):
    n,p,x,y=map(int,input().split())
    arr=list(map(int,input().split()))
    time=0
    for j in range(0,p):
        if arr[j]==0:
            time=time+x
        else:
            time=time+y
    print(time)
