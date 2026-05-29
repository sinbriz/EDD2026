#include <iostream>
#include <stdexcept>

template <typename T>
class Array {
public:
    // Constructor por defecto
    Array() : length(0), firstIndex(0), data(nullptr) {}

    // Constructor con parámetros
    Array(int size, int startIndex = 0) : length(size), firstIndex(startIndex) {
        data = new T[length];
    }

    // Constructor copia
    Array(const Array<T>& other) : length(other.length), firstIndex(other.firstIndex) {
        if (other.data != nullptr) {
            data = new T[length];
            for (int i = 0; i < length; i++) {
                data[i] = other.data[i];
            }
        } else {
            data = nullptr;
        }
    }

    // Move constructor
    Array(Array<T>&& other) noexcept : length(other.length), firstIndex(other.firstIndex), data(other.data) {
        other.length = 0;
        other.firstIndex = 0;
        other.data = nullptr;
    }

    // Destructor
    ~Array() {
        delete[] data;
    }

    // Operador de asignación copia
    Array<T>& operator=(const Array<T>& other) {
        if (this == &other) return *this;

        delete[] data;

        length = other.length;
        firstIndex = other.firstIndex;

        if (other.data != nullptr) {
            data = new T[length];
            for (int i = 0; i < length; i++) {
                data[i] = other.data[i];
            }
        } else {
            data = nullptr;
        }

        return *this;
    }

    // Move assignment
    Array<T>& operator=(Array<T>&& other) noexcept {
        if (this == &other) return *this;

        delete[] data;

        length = other.length;
        firstIndex = other.firstIndex;
        data = other.data;

        other.length = 0;
        other.firstIndex = 0;
        other.data = nullptr;

        return *this;
    }

    // Operador de acceso con verificación de límites
    T& operator[](int index) {
        if (index < firstIndex || index >= firstIndex + length) {
            throw std::out_of_range("Índice fuera de rango");
        }
        return data[index - firstIndex];
    }

    // Versión const
    const T& operator[](int index) const {
        if (index < firstIndex || index >= firstIndex + length) {
            throw std::out_of_range("Índice fuera de rango");
        }
        return data[index - firstIndex];
    }

    int size() const {
        return length;
    }

    // Friend para operador de salida
    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const Array<U>& arr);

protected:
    int length;
    int firstIndex;
    T* data;
};

// Operador de salida
template <typename T>
std::ostream& operator<<(std::ostream& os, const Array<T>& arr) {
    os << "[ ";
    for (int i = 0; i < arr.length; i++) {
        os << arr.data[i];
        if (i < arr.length - 1) {
            os << ", ";
        }
    }
    os << " ]";
    return os;
}

// Clase derivada con control de elementos
template <typename T>
class ManagedArray : public Array<T> {
public:
    using Array<T>::Array; // hereda constructores

    // Constructor adicional para inicializar count
    ManagedArray(int size, int startIndex = 0) : Array<T>(size, startIndex), count(0) {}

    // Agregar al inicio
    void push_front(const T& value) {
        if (count >= this->length) {
            throw std::overflow_error("Arreglo lleno");
        }

        // recorrer a la derecha
        for (int i = count; i > 0; i--) {
            this->data[i] = this->data[i - 1];
        }

        this->data[0] = value;
        count++;
        this->firstIndex--; // mantiene coherencia lógica
    }

    // Agregar al final
    void push_back(const T& value) {
        if (count >= this->length) {
            throw std::overflow_error("Arreglo lleno");
        }
        this->data[count] = value;
        count++;
    }

    // Insertar en cualquier posición lógica (medio)
    void insert(int index, const T& value) {
        if (count >= this->length) {
            throw std::overflow_error("Arreglo lleno");
        }
        if (index < this->firstIndex || index > this->firstIndex + count) {
            throw std::out_of_range("Índice fuera de rango");
        }

        int pos = index - this->firstIndex;

        // mover elementos a la derecha
        for (int i = count; i > pos; i--) {
            this->data[i] = this->data[i - 1];
        }

        this->data[pos] = value;
        count++;
    }

    // Saber cuántos elementos hay realmente
    int size() const {
        return count;
    }

protected:
    int count; // número de elementos almacenados
};

// Ejemplo de uso
int main() {
    ManagedArray<int> arr(5, 0); // capacidad 5, índice inicial 0

    arr.push_back(10);
    arr.push_back(20);
    arr.push_front(5);
    arr.insert(2, 15);

    std::cout << arr << std::endl;
    std::cout << "Elementos ocupados: " << arr.size() << std::endl;

    return 0;
}
