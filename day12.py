from get_input import get_input
import os
import numpy as np

if not os.getenv('DEBUG'):
    input = [l.rstrip('\n') for l in get_input('12')]
else:
    input = [l.rstrip('\n') for l in """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()]

class Square:
    def __init__(self, char, id):
        self.char = char
        self.id = id
    
    def get_height(self):
        return ord(self.char)

    def get_neighbors(self, grid):
        i, j = self.id
        up = grid[i-1, j] if (i-1) >= 0 else None
        down = grid[i+1, j] if (i+1) <= len(grid)-1 else None
        left = grid[i, j-1] if (j-1) >= 0 else None
        right= grid[i, j+1] if (j+1) <= len(grid[i])-1 else None
        
        neighbors = {'up': up, 'down': down, 'right': right, 'left': left}
        
        return neighbors 
   


def to_nparr(input):
    N = len(input)
    M = len(input[0])
    start_points = []
    end=None

    grid = np.zeros((N, M), dtype=object)
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                start = (i, j)
                char = 'a'
                grid[i, j] = Square(char, start)
                start_points.append(start)

            elif input[i][j] == 'E':
                end = (i, j)
                char = 'z'
                grid[i, j] = Square(char, end)
            else:

                grid[i, j] = Square(input[i][j], (i, j))
            
            if input[i][j] == 'a':
                start_points.append((i, j))

    return grid, start_points, end

def bfs(grid, start, end):
    visited = {}
    visited[start] = 0

    queue = []
    queue.append(start)

    while len(queue) > 0:
        point = queue.pop(0)
        steps = visited[point]

        neighbors = point.get_neighbors(grid)
        for neighbor in neighbors.values():
            if neighbor in visited or neighbor == None:
                continue

            if neighbor.get_height() - point.get_height() <= 1:
                visited[neighbor] = steps+1
                queue.append(neighbor)
                if neighbor == end:
                    return steps+1
    
    return None

def part1(grid, start, end):
    start_point, end_point = grid[(start)], grid[(end)]

    steps = bfs(grid, start_point, end_point)
    print(f"Part 1: {steps}")   

def part2(grid, start_points, end):
    
    all_steps = []
    for start_point_id in start_points:
        start_point = grid[start_point_id]
        steps = bfs(grid, start_point, grid[end])
        if steps:
            all_steps.append(steps)
    
    print(f'Part 2: {min(all_steps)}')

grid, start_points, end = to_nparr(input)

part1(grid, start_points[0], end)
part2(grid, start_points, end)