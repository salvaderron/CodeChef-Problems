# cook your dish here
n=int(input())
for i in range(0,n):
    x=int(input())
    arr=list(map(int,input().split()))
    print(max(arr)-min(arr))
