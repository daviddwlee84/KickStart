# TLE on large cases


def parser(path: str) -> str:
    """ convert any path to pure path without ()s """
    if '(' not in path:
        return path

    i = 0
    while '(' in path:
        start = path.find('(')
        left_parathesis = 0
        for i in range(start + 1, len(path)):
            if path[i] == '(':
                left_parathesis += 1
            if path[i] == ')':
                if left_parathesis == 0:
                    break
                else:
                    left_parathesis -= 1
        end = i
        path = path[:start-1] + path[start+1:end] * \
            int(path[start-1]) + path[end+1:]

    return path


direction = {
    'N': (0, -1),
    'S': (0, 1),
    'E': (1, 0),
    'W': (-1, 0)
}


def solve(path: str):
    """ solve any pure path string """
    position = [1, 1]
    for i in range(len(path)):
        position[0] += direction[path[i]][0]
        position[1] += direction[path[i]][1]

    if position[0] < 1:
        position[0] += 1000000000
    if position[1] < 1:
        position[1] += 1000000000

    return position


# Input number of test cases
t = int(input())

for i in range(t):

    raw_path = input()
    w, h = solve(parser(raw_path))

    print('Case #{}:'.format(i+1), w, h)
