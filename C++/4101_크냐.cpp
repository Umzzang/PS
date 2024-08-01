#include<iostream>


using namespace std;

int main() {
    int x, y;
    while (1) {
        cin >> x >> y;
        if (x == 0 && y == 0) {
            break;
        }
        else {
            if (x > y) {
                cout << "Yes" << "\n";
            }
            else {
                cout << "No" << "\n";
            }
        }
    }
}