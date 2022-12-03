from get_input import get_input

input = [l.rstrip('\n') for l in get_input('3')]
#input = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"] #test


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#for i, char in enumerate(chars):
#    print((char, i+1))

#split items

def part1(input, chars):
    c1 = []
    c2 = []

    for bag in input:
        items1 = "".join(set(bag[:len(bag)//2])) #cut str in half & remove duplicates
        items2 = "".join(set(bag[len(bag)//2:]))

        c1.append(items1)
        c2.append(items2)

    scores = 0
    for i in range(len(c1)):
        for char in c1[i]:
            if char in c2[i]:
                #print(((c1[i], c2[i]), char))
                #print()
                scores += chars.index(char)+1 
    
    return scores

print(f'Part 1: {part1(input, chars)}')

def part2(input, chars):
    groups = [input[n:n+3] for n in range(0, len(input), 3)]
    
    scores = 0
    for i in range(len(groups)):
        for char in ''.join(set(groups[i][0])):
            
            if char in groups[i][1] and char in groups[i][2]:
                #print(((groups[i][0], groups[i][1], groups[i][2]), char))
                scores += chars.index(char)+1

    return scores

print(f'Part 2: {part2(input, chars)}')
