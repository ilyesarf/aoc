from get_input import get_input
import os
import math

if not os.getenv('DEBUG'):
    input = list(filter(None, get_input('11', lines=False).split('\n')))
else:
    input = list(filter(None, open('ex', 'r').read().split('\n')))


class Parser:
    def __init__(self, input):
        self.input = input
    
    def parse_input(self):
        monkeys = []
        for i in range(0, len(self.input), 6):
            monkey = [l.lstrip(' ') for l in self.input[i:i+6]]
            if len(monkey) > 0:
                monkeys.append(monkey)
        
        return monkeys

    def parse_monkeys(self):
        monkeys = self.parse_input()

        data = {str(id): {} for id in range(len(monkeys))}
        for id in data.keys():
            monkey = monkeys[int(id)]

            items = self.parse_items(monkey[1])
            data[id]['items'] = items

            op = self.parse_op(monkey[2])
            data[id]['op'] = op

            test = self.parse_test(monkey[3:])
            data[id]['test'] = test
        
        return data

    def parse_items(self, str_items):
        items = []

        for item in str_items.split(': ')[1].split(', '):
            items.append(int(item))

        return items

    def parse_op(self, str_op):
        op = []
        for x in str_op.split('= ')[1].split(' ')[1:]:
            op.append(''.join(x))

        return op
    
    def parse_test(self, str_test):
        #[divisor, true_throw, false_throw]
        test = []

        divisor = str_test[0].split('by ')[1]
        test.append(int(divisor))

        for line in str_test[1:]:
            throw = line.split('monkey ')[1]
            test.append(throw)

        return test

parser = Parser(input)
data = parser.parse_monkeys()

def op(old, op_type, factor):
    if factor == 'old':
        factor = str(old)

    op = str(old) + op_type + factor

    return eval(op)

def test(worry, divisor):
    return worry % divisor == 0

def throw(data, worry, state, throw_true, throw_false):

    if state:
        data[throw_true]['items'].append(worry)
    else:
        data[throw_false]['items'].append(worry)
    
    return data

def round(data, scores, lcm=0):
    for id in data.keys():
        monkey = data[id]
        items = monkey['items']

        for item_id in range(len(items)):
            item = items[item_id]
            scores[int(id)] += 1
            new = op(item, monkey['op'][0], monkey['op'][1])
            if lcm == 0:
                worry = new // 3
            else:
                worry = new % lcm

            state = test(worry, monkey['test'][0])
            
            data = throw(data, worry, state, monkey['test'][1], monkey['test'][2])
        
        monkey['items'] = []
        

    return data, scores

def part1(data):
    scores = [0]*len(data.keys())
    for i in range(20):
        data, scores = round(data, scores)

    top2 = sorted(scores, reverse=True)[:2]
    print(f"Part 1: {top2[0] * top2[1]}")

part1(data)

#reset data
data = parser.parse_monkeys()
def part2(data):
    lcm = math.lcm(*(data[id]['test'][0] for id in data.keys()))
    scores = [0]*len(data.keys())
    for i in range(10000):
        data, scores = round(data, scores, lcm)

    top2 = sorted(scores, reverse=True)[:2]
    print(f"Part 2: {top2[0] * top2[1]}")

part2(data)
                    



