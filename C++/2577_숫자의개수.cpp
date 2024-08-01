#include<iostream>
#include<string>

using namespace std;


string mult(int A, int B, int C) {

    return to_string(A * B * C);
}

int main() {
    
    int A, B, C;
    int numarr[10] = {0};
    cin >> A >> B >> C;
    string result = mult(A, B, C);
    
    for (int i=0;i<result.length();i++) {
        numarr[result[i]-'0'] += 1;
    }
    for (int i=0; i<10;i++) {
        cout << numarr[i] << "\n";
    }
}