#include "c_listls.hpp"
#include "c_listtail.hpp"
#include <iostream>

using namespace std;

int main() {
    cout << " Probando ListLS " << endl;
    ed::ListLS<int> ls1;

    // Agregar elementos
    ls1.cons(10);
    ls1.cons(20);
    ls1.cons(30);

    cout << "Lista LS: " << ls1 << endl;
    cout << "Head: " << ls1.head() << endl;
    cout << "Tail: " << ls1.tail() << endl;
    cout << "Size: " << ls1.getSize() << endl;

    ls1.rest();
    cout << "Despues de rest(): " << ls1 << endl;

    cout << "\n Probando ListTail " << endl;
    ed::ListTail<int> ls2;

    // Agregar elementos
    ls2.addHead(10);
    ls2.addHead(20);
    ls2.addHead(30);
    ls2.addTail(40);
    ls2.addTail(50);

    cout << "Lista Tail: " << ls2 << endl;
    cout << "Head: " << ls2.head() << endl;
    cout << "Tail: " << ls2.tail() << endl;
    cout << "Size: " << ls2.getSize() << endl;

    ls2.delHead();
    cout << "Despues de delHead(): " << ls2 << endl;

    ls2.delTail();
    cout << "Despues de delTail(): " << ls2 << endl;

    return 0;
}
