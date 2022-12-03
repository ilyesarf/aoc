from get_input import get_input

input = get_input('1')

ns = [i for i, x in enumerate(input) if x == '\n']
print(ns)

scores = []
for i in range(len(ns)):
    
    if i == 0:
        score = sum([int(e.rstrip('\n')) for e in input[0:ns[i]]])
    else:
        score = sum([int(e.rstrip('\n')) for e in input[ns[i-1]+1:ns[i]]])
    
    scores.append(score)

scores = sorted(scores, reverse=True)
print(scores)
#Part 1
print(scores[0])

#Part 2
top3 = scores[:3]

print(sum(top3))
