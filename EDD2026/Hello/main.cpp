#include <iostream>

using namespace std;

template <typename T>
class Array {
public:
    // Constructor por defecto
    Array() {
        length = 0; //no hay elementos
        firstIndex = 0; //base estandar
        data = nullptr; //no apunta a memoria
    }
    // Constructor con parámetros
    Array(int size, int startIndex = 0) {
        length = size;
        firstIndex = startIndex;
        data = new T[length];
    }
    //Constructor copia
    /*Constructor copia (deep copy)
    Este constructor:
         Copia length y firstIndex
         Reserva nueva memoria
         Copia elemento por elemento
         */
    Array(const Array<T>& other){
        length = other.lenght;
        firstIndex = other.firstIndex;

        if (other.data != nullptr){
            data= new T[length];
            for(int i = 0; i < lenght; i++){
                data{i} = other.data[i];
            }
        } else {
            data = nullptr;
        }
    }
    ~Array() {
    delete[] data;
    }
    /*Operador []:
    Debes devolver una referencia (T&)
     para poder leer y modificar elementos:
     */
    T& operator[](int index){
    if (index < firstIndex || index >= firstIndex + lenght){
        throw std::out_of_range("Índice fuera de rango");
    }
    return data[index - firstIndex];
    }

     /*Operador []:
    Debes devolver una referencia (T&)
    Versión constante (muy recomendada)
    Esto permite acceder a elementos cuando el arreglo es constante:
    */
    const T& operator[](int index) const{
        if (index < firstIndex || index >= firstIndex + lenght){
        throw std::out_of_range("Índice fuera de rango");
        }
        return data[index - firstIndex];
    }

protected:
    int length;
    int firstIndex;
    T   *data; // direccion bloque de datos
};

int main()
{
    Array <int> a(3,1);
    // Array <int> arr(3, 1);


    a[1] = 10;
    a[2] = 20;
    a[3] = 30;

    Array <int> b = a;
    std::cout << a[2] << endl;
    std::cout << b[1] << endl;
    std::cout << b[3] << endl;
    return 0;
}
