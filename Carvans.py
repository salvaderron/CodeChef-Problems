# cook your dish here
x=int(input())
for i in range(x):
    n=int(input())
    arr=list(map(int,input().split()))
    test=arr.copy()
    j=0
    count=0
    while(j!=(n-1)):
        if arr[j]>=arr[j+1]:
            j+=1
        else:
            arr[j+1]=arr[j]
            j+=1
    for k in range(0,n):
        if arr[k]==test[k]:
            count+=1
    print(count)
                
