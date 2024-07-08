# cook your dish here
x=int(input())
for i in range(x):
    n=int(input())
    arr=list(map(int,input().split()))
    dist=0
    gas=arr[0]
    for j in range(1,n):
        if gas==0:
            break
        else:
            gas=gas-1+arr[j]
            dist+=1
    print(dist+gas)
