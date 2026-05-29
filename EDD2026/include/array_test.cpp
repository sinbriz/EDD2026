#include <iostream>
#include "array.hpp"

using namespace ed;

template <typename T>
void insertionSort(Array<T> &A)
{
    // Como firstIndex = 1, trabajamos con índices 1..length
    for (int j = 2; j <= A.getLength(); j++) {
        T key = A[j];
        int i = j - 1;

        while (i >= 1 && A[i] > key) {
            A[i + 1] = A[i];
            i = i - 1;
        }
        A[i + 1] = key;
    }
}

int main()
{
    ed::Array<int> a(10, 1);  // Array con índices 1..10

    // Llenar el array con valores descendentes para probar el ordenamiento
    for (int i = 1; i <= 10; i++)
        a[i] = 11 - i;  // 10, 9, 8, ..., 1

    cout << "Array original: " << a << endl;

    insertionSort(a);

    cout << "Array ordenado: " << a << endl;

    return 0;
}
