#include <iostream>
#include <iomanip> // needed to use manipulators with parameters (precision, width)
#include <algorithm> // std::sort
using namespace std;

// The E[k] function
double iterative(int N, double V[], int K)
{
    double *sum = new double[N + 1];
    double *dp = new double[K + 1];

    // sorting the array
    sort(V, V + N);

    // pre-calculate the summation
    sum[N] = 0;
    for (int i = N - 1; i >= 0; i--)
        sum[i] = sum[i+1] + V[i];

    // Dynamic Programming
    dp[0] = sum[0] / N; // case E[0]
    // case E[1] to E[K]
    for (int i = 1; i <= K; i++) {
        // find how many number is begger than dp[i]
        int bigger = upper_bound(V, V + N, dp[i - 1]) - V;
        // sum the bigger numbers
        dp[i] = (bigger * dp[i-1] + sum[bigger]) / N;
    }
    return dp[K];
}

int main()
{
    int T, t = 1; // The number of test cases
    cin >> T;

    int N; // The the number of item in the bag
    int K; // The maximum number of times you may redip
    while (T--)
    {
        cin >> N >> K;
        double *V = new double[N];
        for (int i = 0; i < N; i++) cin >> V[i];

        cout << fixed << setprecision(6);
        cout << "Case #" << t << ": " << iterative(N, V, K) << endl;
        t++;
    }
    return 0;
}