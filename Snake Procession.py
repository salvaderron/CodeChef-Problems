def is_valid_report(arr):
    state = 0  # 0 means expecting 'H' or '.', 1 means expecting 'T'
    
    for char in arr:
        if char == 'H':
            if state != 0:
                return "Invalid"
            state = 1
        elif char == 'T':
            if state != 1:
                return "Invalid"
            state = 0
    
    if state == 1:
        return "Invalid"
    
    return "Valid"

# Main code to read input and process each report
x = int(input())
for _ in range(x):
    n = int(input())
    arr = input()
    result = is_valid_report(arr)
    print(result)
