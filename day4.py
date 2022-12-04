from get_input import get_input 

input = [l.rstrip('\n') for l in get_input('4')]

def get_ranges(input):
    ranges = [range.split(',') for range in input]

    return ranges

def is_in(range1, range2):
    n = [i for i in range(int(range1.split('-')[0]), int(range1.split('-')[1])+1)]
    m = [i for i in range(int(range2.split('-')[0]), int(range2.split('-')[1])+1)]

    #return set(n) <= set(m) or set(m) <= set(n) #check if range contains another range (part1)
    return bool(set(n) & set(m)) #check if they overlap (part2)


ranges = get_ranges(input)
    
count = 0
for i in range(len(ranges)):
    range1 = ranges[i][0]
    range2 = ranges[i][1]

    if is_in(range1, range2):
        count += 1

print(count)
     
    
    
