# cook your dish here
x=int(input())
for i in range(x):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    s.sort()
    
    for j in range(n):
        if k > 0 and s[j] < 0:
            s[j] = -s[j]
            k -= 1
    
    
    max_sum = sum(value for value in s if value > 0)
    
    print(max_sum)
        
