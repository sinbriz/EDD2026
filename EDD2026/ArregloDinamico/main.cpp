#include <iostream>

using namespace std;

template <typename T>
class Array {
public:
    //Función Constructora de la clase
    Array(int aiLength, int aiFirstIndex = 1)
    {
        this->length = aiLength;
        this->firstIndex = aiFirstIndex;
        this->data = new T[aiLength];
        for (int i = 0; i < this->length; i++)
            this->data[i] = 0;
    }

    Array(const Array<T>& B)
    {
        this->length = B.length;
        this->firstIndex = B.firstIndex;
        this->data = new T[B.length];
        T* dirBThis = this->data;
        T* dirBB = B.data;
        for (int i = 0; i < this->length; i++){
            *dirBThis = *dirBB;
            ++dirBThis;
            ++dirBB;
        }
    }
    ~Array()
    {
        delete [] this->data;
    }
    T& operator[](int i)
    {
        //Formula de direccionamiento
        return *(this->data + i - this->firstIndex);
       // return *(this->data + i − this->firstIndex);
    }

    T& operator[](int i) const
    {
        //Formula de direccionamiento
        return *(this->data + i - this->firstIndex);
       // return *(this->data + i − this->firstIndex);
    }

    int getLength() const
    {
        return this->length;
    }
    int getFirstIndex() const
    {
        return this->firstIndex;
    }
protected:
    int length;
    int firstIndex;
    T   *data;
    int numElem;
};

//Herencia

                //Parametros formales, en este contexto & es por referencia
void intercambia(int &a, int &b){ //Pasa por referencia, por valor no hace cambio
    int tmp= a;
    a = b;
    b = tmp;
}

int main()
{
    /*
    int a = 1;
    int b = 2;
//Parametros reales, valores concretos
    intercambia(a,b);
    cout << "a = " << a << " b = " << b << endl;*/

    Array<int>  A(20);

    A[1] =99;
    A[5] = 55;
    A[A.getLength()] = 77;

    cout << "A = "<< endl;
    for (int i = A.getFirstIndex(); i <= A.getLength(); i++)
           cout << A[i] << " ";
      cout << endl;

    cout << "B = "<< endl;
    Array<int>  B(A);
    for (int i = B.getFirstIndex(); i <= B.getLength(); i++)
           cout << B[i] << " ";
      cout << endl;

    return 0;
}
