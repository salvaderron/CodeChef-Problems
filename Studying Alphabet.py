# cook your dish here
x=list(input())
n=int(input())
for i in range(n):
    a=list(input())
    count=0
    for j in range(len(a)):
        if a[j] in x:
            count+=1
    if count==len(a):
        print("Yes")
    else:
        print("No")
