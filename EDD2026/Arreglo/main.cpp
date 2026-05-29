#include <iostream>

using namespace std;

int main()
{
    int a[] = {4,6,7,8,9,1,2,-1};
        //estrella *
        //Se declara una variable de tipo apuntador
        //sirve para guardar una direccion de memoria
        //de un entero
    int *iDirBaseArray = a;

    int elem5 = a[5]; // O(1)
    //array_addr + elem_size × (i − first_index)

                         // * operador para obtener el contenido de
                         // de esa direccion de memoria
                         //El operador de desreferencia
     cout << "elem5: " << *(iDirBaseArray + 5) << endl;

    cout << a << endl;
    cout << iDirBaseArray << endl;
    cout << "a[5] = " << elem5 << endl;
   // & es el operador de direccion
   // saber la direccion de memoria donde se guarda su dato
     cout << "Dir del elemnto 5: " << &elem5 << endl;

     for (int i = 0; i <= 6 ; i++) {
        cout << iDirBaseArray << ": " << *iDirBaseArray << endl;
        iDirBaseArray++;
     }
     cout << "\n\nsolo con apuntadores:\n";
     iDirBaseArray = a;
     while ( *iDirBaseArray != -1) {
        cout << iDirBaseArray << ": " << *iDirBaseArray << endl;
        iDirBaseArray++;
     }

    iDirBaseArray = a;
    cout << "iDirBaseArray [5]: " << iDirBaseArray[5] << endl;

    cout << "\n\nCambiar la dirección de inicio a 1\n" << endl;
    //Truco para hacer que el arreglo inicie en 1
    --iDirBaseArray;
    cout << "iDirBaseArray [1]: " << iDirBaseArray[1] << endl;
    cout << "iDirBaseArray [5]: " << iDirBaseArray[5] << endl;

    return 0;
}
