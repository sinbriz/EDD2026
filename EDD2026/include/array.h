#ifndef __ARRAY_HPP__
#define __ARRAY_HPP__

#include <iostream>
#include <stdexcept>
#include <exception>
#include <sstream>

using namespace std;

namespace ed {

template <typename T>
class Array {
public:
    // Constructor por defecto
    Array() {
        length = 0;
        firstIndex = 0;
        data = nullptr;
    }

    // Constructor con parámetros
    Array(int size, int startIndex = 0) {
        length = size;
        firstIndex = startIndex;
        data = new T[length];
    }

    // Constructor copia (deep copy)
    Array(const Array<T>& other) {
        length = other.length;
        firstIndex = other.firstIndex;

        if (other.data != nullptr) {
            data = new T[length];
            T* dirBThis = this->data;
            T* dirBB = other.data;
            for (int i = 0; i < this->length; i++) {
                *dirBThis = *dirBB;
                ++dirBThis;
                ++dirBB;
            }
        } else {
            data = nullptr;
        }
    }

    // Move Constructor
    Array(Array<T>&& other) noexcept {
        length = other.length;
        firstIndex = other.firstIndex;
        data = other.data;

        other.length = 0;
        other.firstIndex = 0;
        other.data = nullptr;
    }

    // Destructor
    ~Array() {
        delete[] data;
    }

    // Operador [] (versión no constante)
    T& operator[](int index) {
        if (index < firstIndex || index >= firstIndex + length) {
            throw std::out_of_range("Índice fuera de rango");
        }
        return data[index - firstIndex];
    }

    // Operador [] (versión constante)
    const T& operator[](int index) const {
        if (index < firstIndex || index >= firstIndex + length) {
            throw std::out_of_range("Índice fuera de rango");
        }
        return data[index - firstIndex];
    }

    // Operador de asignación (copy assignment)
    Array<T>& operator=(const Array<T>& other) {
        if (this == &other) {
            return *this;
        }

        if (data != nullptr) {
            delete[] data;
        }

        length = other.length;
        firstIndex = other.firstIndex;

        if (other.data != nullptr) {
            data = new T[length];
            T* dirBThis = this->data;
            T* dirBB = other.data;
            for (int i = 0; i < this->length; i++) {
                *dirBThis = *dirBB;
                ++dirBThis;
                ++dirBB;
            }
        } else {
            data = nullptr;
        }
        return *this;
    }

    // Move Assignment Operator
    Array<T>& operator=(Array<T>&& other) noexcept {
        if (this == &other) {
            return *this;
        }

        if (data != nullptr) {
            delete[] data;
        }

        length = other.length;
        firstIndex = other.firstIndex;
        data = other.data;

        other.length = 0;
        other.firstIndex = 0;
        other.data = nullptr;

        return *this;
    }

    // Getters
    int getLength() const {
        return length;
    }

    int getFirstIndex() const {
        return firstIndex;
    }

    // Friend function para operator<<
    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const ed::Array<U>& arr);

protected:
    int length;      // Cantidad de elementos
    int firstIndex;  // Índice de inicio
    T* data;         // Puntero al bloque de datos
};

// Implementación del operador <<
template <typename T>
std::ostream& operator<<(std::ostream& os, const Array<T>& arr) {
    os << "[ ";
    T* dirBThis = arr.data;
    for (int i = 0; i < arr.length; i++) {
        os << *dirBThis;
        ++dirBThis;
        if (i < arr.length - 1) {
            os << ", ";
        }
    }
    os << " ]";
    return os;
}

} // namespace ed

#endif // __ARRAY_HPP__
