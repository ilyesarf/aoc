from get_input import get_input
import os

if not os.getenv('DEBUG'):
    inp = get_input('2', 2024)
else:
    inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".split('\n')

def normalize(str_arr):
    print(str_arr)
    return [[int(i) for i in l.split(' ')] for l in str_arr]

inp = normalize(inp)

def check(arr):
    valid = True
    increase = (arr[0]-arr[1])<0
    i = 0
    while i<len(arr)-1 and valid!=False:
        diff = arr[i]-arr[i+1]
        valid = ((diff < 0) == increase) and (1 <= abs(diff) <= 3)
        i+=1

    return valid, i-1

def dampener(arr, i_faulty):
    for remove_i in range(len(arr)):
        fixed_arr = [arr[x] for x in range(len(arr)) if x != remove_i]
        valid, _ = check(fixed_arr)
        if valid:
            return True, remove_i

    return False, None

part = int(input("part: "))
valid_sum = 0
for arr in inp:
    valid, i = check(arr)
    if valid:
        print(arr, "valid from the start")
        valid_sum+=1
    else:
        if part==2:
            fixed, remove_i = dampener(arr, i)
            if fixed:
                print(arr, "valid after removing", arr[remove_i])
                valid_sum+=1
            else:
                print(arr, f"{arr[i]} {arr[i+1]} is faulty")

print(valid_sum)
