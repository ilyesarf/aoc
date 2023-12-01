from get_input import get_input
import os

if not os.getenv('DEBUG'):
    input = [l.rstrip('\n') for l in get_input('7')]
else:
    input = [l.rstrip('\n') for l in """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()]


directories = {}
list_of_directories = []
cd = ''
for x in input:
    if '$ cd' in x and '..' not in x:
        dir = x.removeprefix('$ cd ')
        cd += dir
        if cd not in directories:
            directories[cd] = []
        list_of_directories.append(dir)

    elif '$ cd' in x and '..' in x:
        cd = cd.removesuffix(list_of_directories[len(list_of_directories)-1])
        list_of_directories.pop(len(list_of_directories)-1)

    elif '$ cd' not in x and '$ ls' not in x:
        if 'dir' in x:
            dir = x.removeprefix('dir ')
            directories[cd+dir] = []
        else:
            size, name = x.split()
            directories[cd].append((int(size), name))

total_size = {directory: 0 for directory in directories}

for directory in directories:
    for item in directories[directory]:
        if type(item) == tuple:
            total_size[directory] += item[0]

for key in total_size.keys():
    for directory in directories:
        if key in directory and key != directory:
            total_size[key] += total_size[directory]

# Part 1
total = 0

# Part 2
empty_space = 70_000_000 - max(total_size.values())
space_needed = 30_000_000 - empty_space
temp = []

for directory in total_size:
    # Part 1
    if total_size[directory] <= 100_000:
        total += total_size[directory]
    # Part 2
    if total_size[directory] >= space_needed:
        temp.append(total_size[directory])

print(total)
print(min(temp))
