t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    # your code goes here
    s.sort()
    
    # Initialize the minimum difference to a large number
    min_diff = float('inf')
    
    # Compare each pair of consecutive horses
    for i in range(1, n):
        min_diff = min(min_diff, s[i] - s[i-1])
    
    print(min_diff)
