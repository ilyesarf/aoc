from get_input import get_input

input = get_input('1')

ns = [i for i, x in enumerate(input) if x == '\n']

scores = []
for i in range(len(ns)):
    
    if i == 0:
        score = sum([int(e.replace('\n', '')) for e in input[0:ns[i]]])
    else:
        score = sum([int(e.replace('\n', '')) for e in input[ns[i-1]+1:ns[i]]])
    
    scores.append(score)

top3 = sorted(scores, reverse=True)[:3]

print(sum(top3))
