/* https://www.geeksforgeeks.org/how-to-begin-with-competitive-programming/
 * Linear Search: Given an integer array and an element x, find if element is present in array or not. If element is present, then print index of its first occurrence. Else print -1.
 * 
 * Input:
 * First line contains an integer, the number of test cases ‘T’. Each test case should be an integer. Size of the array ‘N’ in the second line. In the third line, input the integer elements of the array in a single line separated by space. Element X should be inputted in the fourth line, i.e., after entering the elements of array. Repeat the above steps second line onwards for multiple test cases.
 * 
 * Output:
 * Print the output in a separate line returning the index of the element X. If the element is not present, then print -1.
 * 
 * Constraints:
 * 1 <= T <= 100
 * 1 <= N <= 100
 * 1 <= Arr[i] <= 100
 **/

// A Sample C++ program for beginners with Competitive Programming
#include <iostream>
using namespace std;

// This function returns index of element x in arr[]
int search(int arr[], int n, int x)
{
    for (int i = 0; i < n; i++)
    {
        // Return the index of the element if the element
        // is found
        if (arr[i] == x)
            return i;
    }

    // return -1 if the element is not found
    return -1;
}

int main()
{
    // Note that size of arr[] is considered 100 according to
    // the constraints mentioned in problem statement.
    int arr[100], x, t, n;

    // Input the number of test cases you want to run
    cin >> t;

    // One by one run for all input test cases
    while (t--)
    {
        // Input the size of the array
        cin >> n;

        // Input the array
        for (int i = 0; i < n; i++)
            cin >> arr[i];

        // Input the element to be searched
        cin >> x;

        // Compute and print result
        cout << search(arr, n, x) << endl;
    }
    return 0;
}