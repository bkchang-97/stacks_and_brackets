import random, copy
from collections import deque

def generate(data):
    
    open_count = 0
    stack = deque()
    open = ["(", "{", "["]
    close = [")", "}", "]"]
    brackets = ""
    numbers = []
    
    while open_count != 6:
        if not stack:
            rcs = random.randint(0, 2)
            stack.append(open[rcs])
            brackets += open[rcs]
            open_count += 1
            numbers.append(len(stack))
        else:
            oc = random.randint(1, 2)
            if oc == 1:
                rcs= random.randint(0, 2)
                stack.append(open[rcs])
                brackets += open[rcs]
                open_count += 1
                numbers.append(len(stack))
            else:
                pos = open.index(stack.pop())
                brackets += close[pos]
    while stack:
        pos = open.index(stack.pop())
        brackets += close[pos]
        

    # Put these two integers into data['params']
    data['params']['brackets'] = brackets
    data['params']['ans1'] = False
    data['params']['ans2'] = False
    data['params']['ans3'] = False
    data['params']['ans4'] = False
    data['params']['ans5'] = False
    data['params']['ans6'] = False
    
    ans = max(numbers)
    if ans == 1:
        data['params']['ans1'] = True
    elif ans == 2:
        data['params']['ans2'] = True
    elif ans == 3:
        data['params']['ans3'] = True
    elif ans == 4:
        data['params']['ans4'] = True
    elif ans == 5:
        data['params']['ans5'] = True
    elif ans == 6:
        data['params']['ans6'] = True
