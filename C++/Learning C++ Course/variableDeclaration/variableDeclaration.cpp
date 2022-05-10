#include <iostream>

using namespace std;

int a, b= 5;

int main()
{
    bool myFlag;
    a = 7;
    myFlag = false;
    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "flag = " << myFlag << endl;
    myFlag = true;
    cout << "flag = " << myFlag << endl;
    cout << "a + b = " << a << endl;
    cout << "b - a = " << b << endl;
    return 0;
}