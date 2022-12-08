from get_input import get_input
import numpy as np
import os

if not os.getenv('DEBUG'):
    input = [l.rstrip('\n') for l in get_input('8')]
else:
    input = "30373\n25512\n65332\n33549\n35390".splitlines()

def extract_trees(input):
    
    trees = []
    for row in input:
        trees.append([int(tree) for tree in list(row)])

    return np.array(trees)

trees = extract_trees(input)

in_trees = trees[1:len(trees[0, :])-1, 1:len(trees[:, 0])-1]

def is_visible(trees, row_i, col_i):
    tree1 = trees[row_i, col_i]
    
    right = trees[row_i, col_i+1:]
    left = trees[row_i, :col_i]
    down = trees[row_i+1:, col_i]
    up = trees[:row_i, col_i]

    return all(tree1 > tree2 for tree2 in right) \
            or all(tree1 > tree2 for tree2 in left) \
            or all(tree1 > tree2 for tree2 in down) \
            or all(tree1 > tree2 for tree2 in up)

    
def part1(input, trees, in_trees):
    score = (2*(len(trees[:, 0]) + len(trees[0, :])))-4 #initial score = (2 * (n trees on edge (column) + n trees on edge (row)))-n corners (4)
    
    for id, _ in np.ndenumerate(in_trees):

            row_i, col_i = id[0]+1, id[1]+1

            if is_visible(trees, row_i, col_i):
                score += 1 

    return score

def calc_scenic(trees, row_i, col_i):
    tree1 = trees[row_i, col_i]
    
    right = trees[row_i, col_i+1:]
    left = reversed(trees[row_i, :col_i])
    down = trees[row_i+1:, col_i]
    up = reversed(trees[:row_i, col_i])
    
    scenic_score = 1
    for view in [right, left, down, up]:
        score = 0
        for tree2 in view:
            if tree1 > tree2:
                score += 1
            else:
                score += 1
                break
        scenic_score *= score
    
    return scenic_score

def part2(input, trees, in_trees):
    scores = []
    
    for id, _ in np.ndenumerate(in_trees):
        row_i, col_i = id[0]+1, id[1]+1
        score = calc_scenic(trees, row_i, col_i)
        scores.append(score)

    return max(scores)

print(f"Part1: {part1(input, trees, in_trees)}")
print(f"Part2: {part2(input, trees, in_trees)}")
