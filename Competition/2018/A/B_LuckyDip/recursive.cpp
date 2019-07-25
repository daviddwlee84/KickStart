#include <iostream>
#include <iomanip> // needed to use manipulators with parameters (precision, width)
using namespace std;

// The E[k] function
double recursive(int N, double V[], int K)
{
    double summation = 0;
    for (int i = 0; i < N; i++){
        if (K == 0)
            summation += V[i];
        else
            summation += max(V[i], recursive(N, V, K-1));
    }
    return summation / N;
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
        cout << "Case #" << t << ": " << recursive(N, V, K) << endl;
        t++;
    }
    return 0;
}