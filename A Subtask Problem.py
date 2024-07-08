# cook your dish here
x=int(input())
for i in range(0,x):
    n,m,k=map(int,input().split())
    arr=list(map(int,input().split()))
    one=arr.count(1)
    count=0
    if one==n:
        print(100)
    else:
        for j in range(0,m):
            if (arr[j]==1):
                count+=1
        if count==m:
            print(k)
        else:
            print(0)
