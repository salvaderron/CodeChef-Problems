n=int(input())
for i in range(0,n):
    a=input()
    b=input()
    f=0
    for j in range(0,len(a)):
        if a[j]=='?' and b[j]=='?':
            pass
        elif a[j]!='?' and b[j]=='?':
            pass
        elif a[j]=='?' and b[j]!='?':
            pass
        elif a[j]==b[j]:
            pass
        else:
            f=1
            break
    if f==0:
        print("Yes")
    else:
        print("No")
        
