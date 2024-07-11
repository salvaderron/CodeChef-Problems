# cook your dish here
n=int(input())
for i in range(0,n):
    a=input()
    if '010' in a or '101' in a:
        print("Good")
    else:
        print("Bad")
