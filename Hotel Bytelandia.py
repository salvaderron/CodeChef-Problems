# cook your dish here
x=int(input())
for i in range(x):
    n=int(input())
    arr=list(map(int,input().split()))
    dep=list(map(int,input().split()))
    events=[]
    for arrival in arr:
        events.append((arrival, 'arrival'))
    for departure in dep:
        events.append((departure, 'departure'))
    events.sort(key=lambda x: (x[0], x[1] == 'arrival'))
    current_guests = 0
    max_guests = 0
    
    for event in events:
        if event[1] == 'arrival':
            current_guests += 1
            if current_guests > max_guests:
                max_guests = current_guests
        else:
            current_guests -= 1
    
    print(max_guests)
