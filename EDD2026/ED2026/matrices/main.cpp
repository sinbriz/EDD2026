#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int A[3][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12}
    };
    cout << "A:" << endl;

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            cout << A[i][j] << "\t";
        }
        cout << endl;
    }
    int *p = &A[0][0];
    p++;

    cout << *p << endl;
    cout << A[1][2] << endl;

    return 0;
}
