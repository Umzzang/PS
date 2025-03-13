#include<iostream>

using namespace std;

int main() {
    int first = 0;
    int num;
    for (int i=1; i<=9; i++) {
        int x;
        cin >> x;
        if (x > first) {
            first = x;
            num = i;
        }
    }
    cout << first << endl;
    cout << num;
}