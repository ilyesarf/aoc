from get_input import get_input
import os
import re

if not os.getenv('DEBUG'):
    inp = get_input('3', 2024, lines=False)
else:
    inp1 = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))" 
    inp2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def parser(text):
    tab = []
    funcs = []
    i = 0
    while i < len(text):
        if text[i:i+4] == "mul(":
            func = "" 
            for x in range(i+4, len(text)):
                if text[x] in "0123456789,)":
                    func+=text[x]
                    if text[x] == ')':
                        break
                else:
                    break

            if func[-1] == ')':
                funcs.append(func.replace(')', ''))
                i = x
            else:
                i+=4
        else:
            i+=1

    for f in funcs:
        ns = map(int, f.split(','))
        
        tab.append(list(ns)) 

    return tab

tab = parser(inp)

def part1(tab):
    return "part1",sum(x*y for x,y in tab)

print(part1(tab))

