#include <iostream>

using namespace std;

int main()
{
     /*  0xd7a57ff740   9               //Para la variable i
        0xd7a57ff741
        0xd7a57ff742
        0xd7a57ff743
        0xd7a57ff744   0xd7a57ff740   //Para la varible p
        ...
        0xD7A57FF754
        */
    int i = 7;
    int *p = &i;

    *p = 9;

    cout << i << endl;
    return 0;
}
