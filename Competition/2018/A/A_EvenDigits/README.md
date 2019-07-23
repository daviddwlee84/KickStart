# Problem A: Even Digits

## Simplified Problem Description

Determine the minimum number of bottom presses to make with no odd digits. A button press can increase the number by 1 or decrease the number by 1

**Examples**:

```txt
42 => 0 (42 has no odd digits)
11 => 3 (11 - 3 = 8)
1 => 1 (1 - 1 = 0 or 1 + 1 = 2)
2018 => 2 (2018 + 2 = 2020)
```

**Limits**:

* Small dataset: 1 ≤ N ≤ 10^5
* Large dataset: 1 ≤ N ≤ 10^16

## Solution

### Brute force

> Only work for small dataset. Will TLE in large dataset.

### Improved: Greedy

Beautiful integer: has only even digits in its decimal representation

In this problem, we can try to find:

* the largest beautiful integer that is still no greater than N
  * Example
    * 22**3**4424 => 22**2**8888
    * **1**222886 => **0**8888888
    * 246202 => 246202
* the smallest beautiful integer that is still no smaller than N
  * Example
    * 22**3**4424 => 22**4**0000
    * **1**2422886 => **2**0000000
    * 204**7**0 => 204**8**0
    * 424**9**231 => 4260000 (9 => +1 will cause carry)
    * 428**9**231 => 4400000
    * 888**9**231 => 20000000 (8 => 0)

Just like a Hex (五進制)
