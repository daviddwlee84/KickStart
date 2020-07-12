from functools import lru_cache
# MLE on large case


def solve(n: int, a: int, b: int, parents):
    @lru_cache(None)
    def dfs_from_node(node: int):
        path = [node]
        while node != 1:
            node = parents[node - 2]
            path.append(node)
        return path

    def pick_ith(path, ith):
        return path[::ith]

    paint = 0

    for node_a in range(1, n + 1):
        for node_b in range(1, n + 1):
            path_a = dfs_from_node(node_a)
            path_b = dfs_from_node(node_b)
            Amadea_picks = pick_ith(path_a, a)
            Bilva_picks = pick_ith(path_b, b)
            paint += len(set(Amadea_picks) | set(Bilva_picks))

    return paint / (n * n)


# Input number of test cases
t = int(input())

for i in range(t):

    n, a, b = list(map(int, input().split()))
    parents = list(map(int, input().split()))

    print('Case #{}:'.format(i+1), solve(n, a, b, parents))
