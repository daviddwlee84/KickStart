""" https://www.geeksforgeeks.org/how-to-begin-with-competitive-programming/
Linear Search: Given an integer array and an element x, find if element is present in array or not. If element is present, then print index of its first occurrence. Else print -1.

Input:
First line contains an integer, the number of test cases ‘T’. Each test case should be an integer. Size of the array ‘N’ in the second line. In the third line, input the integer elements of the array in a single line separated by space. Element X should be inputted in the fourth line, i.e., after entering the elements of array. Repeat the above steps second line onwards for multiple test cases.

Output:
Print the output in a separate line returning the index of the element X. If the element is not present, then print -1.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= Arr[i] <= 100
"""

# A Sample Python program for beginners with Competitive Programming

# Returns index of x in arr if it is present,
# else returns -1


def search(arr, x):
    for j in range(len(arr)):
        if (x == arr[j]):
            return j
    return -1


# Input number of test cases
t = int(input())

# One by one run for all input test cases
for i in range(0, t):

    # Input the size of the array
    n = int(input())

    # Input the array
    arr = list(map(int, input().split()))

    # Input the element to be searched
    x = int(input())

    print(search(arr, x))

    # The element can also be searched by index method
    # But you need to handle the exception when element is not found
    # Uncomment the below line to get that working.
    # arr.index(x)
