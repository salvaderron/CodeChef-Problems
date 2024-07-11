# cook your dish here
n=int(input())
for i in range(n):
    s=list(input())
    count=0
    last_char = s[0]
    # If the first door is closed, we need at least one flip
    if last_char == '0':
        count += 1
    # Traverse the rest of the string
    for char in s[1:]:
        if char != last_char:
            count += 1
            last_char = char

    print(count)
