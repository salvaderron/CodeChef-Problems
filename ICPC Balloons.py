# cook your dish here
x=int(input())
for i in range(0,x):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    sam=[1,2,3,4,5,6,7]
    for j in range(n):
        if arr[j] in sam:
            count+=1
        if count==7:
            print(j+1)
            break
