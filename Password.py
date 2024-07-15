# cook your dish here
n=int(input())
for i in range(n):
    arr=input()
    u=l=dig=spc=0
    if len(arr)<10:
        print("NO")
    else:
        l = any(c.islower() for c in arr)
        u = any(c.isupper() for c in arr[1:-1])
        dig = any(c.isdigit() for c in arr[1:-1])
        spc = any(c in '@#%&?' for c in arr[1:-1])
    
        if l and u and dig and spc:
            print("YES")
        else:
            print("NO")
    
        
