# cook your dish here
x=int(input())
for i in range(x):
    n,k=map(int,input().split())
    s=list(map(int,input().split()))
    m,t=[],[]
    for j in range(n):
        if (j+1)%2==0:
            t.append(s[j])
        else:
            m.append(s[j])
    j=0
    while(j<k):
        a=max(m)
        b=min(t)
        m.remove(a)
        t.append(a)
        t.remove(b)
        m.append(b)
        j+=1
    if(sum(m)<sum(t)):
        print('YES')
    else:
        print('NO')
    
        
