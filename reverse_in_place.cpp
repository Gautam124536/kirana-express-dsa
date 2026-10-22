#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int a[] = {40, 25, 60, 15, 30};
    int left = 0, right = 4;

    while (left < right) {
        swap(a[left], a[right]);
        left++;
        right--;
    }

    for (int x : a) {
        cout << x << " ";
    }

    cout << '\n';
    return 0;
}
