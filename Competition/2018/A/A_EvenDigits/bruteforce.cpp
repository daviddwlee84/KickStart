#include <iostream>
using namespace std;

int checkAllEven(int value)
{
    int lastnum;
    while (value > 0)
    {
        lastnum = value % 10;
        if (lastnum % 2 != 0)
        {
            return false;
        }
        value /= 10;
    }
    return true;
}

int bruteForce(int N)
{
    for (int i = 0;; i++)
    {
        if (checkAllEven(N - i) || checkAllEven(N + i))
        {
            return i;
        }
    }
}

int main()
{
    int T, t = 1; // The number of test cases
    cin >> T;

    int N; // The integer initialy displayed on the calculator
    while (T--)
    {
        cin >> N;

        cout << "Case #" << t << ": " << bruteForce(N) << endl;
        t++;
    }
    return 0;
}