# cook your dish here
n,d=map(int,input().split())
arr=[]
for i in range(n):
    t=int(input())
    arr.append(t)
arr.sort()
pair = 0
i = 0
# Traverse the sorted array
while i < n - 1:
    if arr[i + 1] - arr[i] <= d:
        pair += 1
        i += 2  # Move to the next pair
    else:
        i += 1  # Move to the next stick

print(pair)
