#include <iostream>
#include "listls.hpp"

using namespace std;
using namespace ed;

int main()
{
    ListLS<int> ls = empty<int>();


    ls = cons(1,ls);
    ls = cons(2,ls);
    ls = cons(3,ls);

    cout << ls << endl;

    ls = deleteLS(ls);

    cout << ls << endl;


    ls = cons(4,ls);
    ls = cons(5,ls);
    ls = cons(6,ls);

    cout << ls << endl;


    return 0;
}
