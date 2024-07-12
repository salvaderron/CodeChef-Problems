n = int(input())
for i in range(n):
    s = input()
    l = len(s)
    if l % 2 == 0:
        left_half = s[:l//2]
        right_half = s[l//2:]
    else:
        left_half = s[:l//2]
        right_half = s[l//2 + 1:]
    
    # Count character frequencies in both halves
    from collections import Counter
    if Counter(left_half) == Counter(right_half):
        print("YES")
    else:
        print("NO")
