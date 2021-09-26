#include <bits/stdc++.h>
#include <cassert>
using namespace std;

//time  --> o(nlogn)
//space --> o(n)
int main()
{
    int n, ans = 1e9;
    cin >> n;
    assert((n >= 2) && "The size of the array must be greater than or equal to 2");
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    sort(v.begin(), v.end());

    for (int i = 1; i < n; i++)
    {
        ans = min(ans, (v[i] - v[i - 1]));
    }
    cout << ans;
    return 0;
}