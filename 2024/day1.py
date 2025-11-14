from get_input import get_input
import os

if not os.getenv('DEBUG'):
    input = get_input('1', 2024,lines=False).strip()

else:
    input = "3   4\n4   3\n2   5\n1   3\n3   9\n3   3"

def normalize(str_arr):
    return [int(i) for i in str_arr.replace("   ", "|").replace("\n", "|").split("|")]

input=normalize(input)

print(input)

tab1, tab2 = [], []
for i in range(len(input)):
    if i%2==0:
        tab1.append(input[i])
    else:
        tab2.append(input[i])

tab1.sort()
tab2.sort()

print(tab1)
print(tab2)
dest = []

for i in range(len(tab1)):
    dest.append(abs(tab1[i]-tab2[i]))
print(dest)
print(sum(dest))
