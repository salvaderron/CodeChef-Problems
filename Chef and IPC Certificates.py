# cook your dish here
n,m,k=map(int,input().split())
count=0
for i in range(0,n):
    arr=list(map(int,input().split()))
    que=arr.pop(k)
    if (sum(arr)>=m) and que<=10:
        count+=1
print(count)
