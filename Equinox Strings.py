x=int(input())
for i in range(x):
    n,a,b=map(int,input().split())
    word=list("EQUINOX")
    anu=0
    sar=0
    for j in range(n):
        arr=list(input())
        if arr[0] in word:
            sar=sar+a
        else:
            anu=anu+b
    if sar>anu:
        print("SARTHAK")
    elif sar<anu:
        print("ANURADHA")
    else:
        print("DRAW")
