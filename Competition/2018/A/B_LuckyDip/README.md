# Problem B: Lucky Dip

## Simplified Problem Description

In this Lucky Dip, there is a bag with N items. The i-th item in the bag has value $V_i$.

You will put your hand into the bag and draw one item at random; all items in the bag have an equal probability of being chosen.

You may only redip a maximum of $K$ times.

Play **optimally** to maximize the value of the item you will end the game with, what is the expected value of that item?

## Solution

> Not so much difference between small and large dataset in this problem

$E[k]$: the optimal **expected value** of the item drawn given k redips

If you can redip k times. The best strategy:

* If you get $v \geq E[k-1]$, you should keep it
* Otherwise, redip it.

### Recursive

Recursion to get $E[K]$: $E[k] = \sum \max(V_i, E[k-1]) / N$. Time Complexity is $O(NK)$

> in the "Analysis" part it said this time complexity is fast enough to pass the large dataset but I got TLE even in small dataset

### Iterative

Iteration to get $E[K]$. Time complexity is $O(N\log N + K \log N)$ (sorting + binary search)

1. sorting
2. binary search
