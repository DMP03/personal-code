#include <iostream>
#include <string>

using namespace std;

int main(){
    string str;
    cout << "Enter your name: ";
    cin >> str;     //cin only works for single words
    cout << "Nice to meet you, " << str << "!" << endl;
    return(0);
}