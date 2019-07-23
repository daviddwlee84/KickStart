#include <iostream>
using namespace std;

#define MAX_DIGIT 20 // if use 16 will not pass

#define INF_EARLY_STOP true // the greater case can be ignore if it need too many carry
#define INF -1

// get all digits into an array
#define GET_DIGITS(value, nums, digit) \
    digit = 0;                         \
    do                                 \
    {                                  \
        nums[digit++] = value % 10;    \
        value /= 10;                   \
    } while (value);

// from array to number
#define GET_ANSWER(ans, nums, digit)     \
    ans = 0;                             \
    for (int i = digit - 1; i >= 0; i--) \
    {                                    \
        ans = ans * 10 + nums[i];        \
    }

long long findNearestSmaller(long long value)
{
    int digit;
    int nums[MAX_DIGIT] = {0};
    GET_DIGITS(value, nums, digit);

    for (int i = digit - 1; i >= 0; i--)
    {
        // Find an odd number
        if (nums[i] & 1)
        {
            nums[i]--; // minus 1
            for (int j = i - 1; j >= 0; j--)
            {
                // Turn the rest of the number to 8
                nums[j] = 8;
            }
            break;
        }
    }

    long long ans;
    GET_ANSWER(ans, nums, digit);

    return ans;
}

long long findNearestGreater(long long value)
{
    int digit;
    int nums[MAX_DIGIT] = {0};
    GET_DIGITS(value, nums, digit);

    for (int i = digit - 1; i >= 0; i--)
    {
        // Find an odd number
        if (nums[i] & 1)
        {
            // Special case for number 9 (need carry)
            if (nums[i] == 9)
            {
#if INF_EARLY_STOP
                return INF;
#else
                int j = i + 1;
                while (nums[j] == 8)
                {
                    j++;
                }
                if (j >= digit)
                {
                    // got carry
                    digit++;
                }
                nums[j] += 2;
                while ((--j) >= 0)
                {
                    nums[j] = 0;
                }
#endif
            }
            else
            {
                nums[i]++; // plus 1
                for (int j = i - 1; j >= 0; j--)
                {
                    // Turn the rest of the number to 0
                    nums[j] = 0;
                }
            }
            break;
        }
    }

    long long ans;
    GET_ANSWER(ans, nums, digit);

    return ans;
}

long long greedy(long long N)
{
    long long greaterN = findNearestGreater(N);
    long long smallerN = findNearestSmaller(N);
#ifdef DEBUG
    // debug
    cout << "N: " << N << " greater: " << greaterN << " smaller: " << smallerN << endl;
#endif
#if INF_EARLY_STOP
    if (greaterN == INF) {
        return N - smallerN;
    }
#endif
    return min(greaterN - N, N - smallerN);
}

int main()
{
    int T, t = 1; // The number of test cases
    cin >> T;

    long long N; // The integer initialy displayed on the calculator
    while (T--)
    {
        cin >> N;

        cout << "Case #" << t << ": " << greedy(N) << endl;
        t++;
    }
    return 0;
}