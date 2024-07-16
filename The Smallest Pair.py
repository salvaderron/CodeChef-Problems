# cook your dish here
x=int(input())
for i in range(x):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(arr[0]+arr[1])
