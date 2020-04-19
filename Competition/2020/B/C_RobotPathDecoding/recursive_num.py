def get_count(path: str):
    """ solve any pure path string """
    S = 0
    E = 0
    for c in path:
        if c == 'S':
            S += 1
        elif c == 'N':
            S -= 1
        elif c == 'E':
            E += 1
        elif c == 'W':
            E -= 1

    return E, S


def parser(path: str):
    if '(' not in path:
        # if string is pure path, then get its count
        return get_count(path)

    if '(' in path:
        # otherwise find any () pair
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

        # split each part, and get count
        E, S = parser(path[:start - 1])
        E2, S2 = parser(path[start+1:end])
        S2 *= int(path[start-1])
        E2 *= int(path[start-1])
        E3, S3 = parser(path[end+1:])

        # % 1000000000 in case of overflow => WA
        return (E + E2 + E3) % 1000000000, (S + S2 + S3) % 1000000000


def solve(E: int, S: int):
    S += 1
    E += 1

    if S < 1:
        S += 1000000000
    if E < 1:
        E += 1000000000

    return E, S


# Input number of test cases
t = int(input())

for i in range(t):

    raw_path = input()
    w, h = solve(*parser(raw_path))

    print('Case #{}:'.format(i+1), w, h)
