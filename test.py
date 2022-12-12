

from time import perf_counter
from collections import deque
from get_input import get_input

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = perf_counter()
        ret = method(*arg, **kw)
        print('Method ' + method.__name__ + ' took : ' +
              "{:2.5f}".format(perf_counter()-t) + ' sec')
        return ret
    return wrapper_method


def get_dist(grid, start, end):
    visited = {}
    visited[start] = 0

    to_visit = deque()
    to_visit.append(start)

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while to_visit:
        (cx, cy) = to_visit.popleft()
        current_steps = visited[(cx, cy)]

        for (dx, dy) in deltas:
            nx, ny = (cx+dx, cy+dy)
            if (nx, ny) in visited or nx in [-1, len(grid[0])] or ny in [-1, len(grid)]:
                continue
            if ord(grid[ny][nx]) - ord(grid[cy][cx]) <= 1:
                visited[(nx, ny)] = current_steps + 1
                to_visit.append((nx, ny))
                print(((nx, ny), grid[ny][nx]))
                if (nx, ny) == end:
                    return current_steps+1

    return None


@profiler
def part1():
    grid = []

    start = (-1, -1)
    end = (-1, -1)

    #in_map = open("input.txt").readlines()
    in_map = [l.rstrip('\n') for l in get_input('12')]

    for y in range(len(in_map)):
        grid.append(list(in_map[y].strip()))
        if "S" in in_map[y]:
            start = (in_map[y].index("S"), y)
        if "E" in in_map[y]:
            end = (in_map[y].index("E"), y)

    grid[start[1]][start[0]] = 'a'
    grid[end[1]][end[0]] = 'z'

    print(get_dist(grid, start, end))

part1()

