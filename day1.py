from get_input import get_input
import os

if not os.getenv('DEBUG'):
    input = get_input('1')

else:
    input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

ns = [i for i, x in enumerate(input) if x == '\n']

scores = []
for i in range(len(ns)):
    
    if i == 0:
        score = sum([int(e.rstrip('\n')) for e in input[0:ns[i]]])
    else:
        score = sum([int(e.rstrip('\n')) for e in input[ns[i-1]+1:ns[i]]])
    
    scores.append(score)

scores = sorted(scores, reverse=True)
#Part 1
print(f'Part 1: {scores[0]}')

#Part 2
top3 = scores[:3]

print(f'Part 2: {sum(top3)}')
