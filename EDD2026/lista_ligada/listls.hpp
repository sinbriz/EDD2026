#ifndef __C_LISTLS__
#define __C_LISTLS__

#include <iostream>
#include <exception>
#include <sstream>
#include <stdexcept>

using namespace std;

namespace ed {

template <class T>
struct Node {
    Node(T aData, Node<T>* aNext = nullptr):
         data(aData), next(aNext)
    {}
    T data;
    Node<T>* next;
};

template <class T>
class ListLS {
public:
    // Constructor por defecto
    ListLS() : _head(nullptr) {}

    // Constructor copia (deep copy)
    ListLS(const ListLS<T>& other) {
        _head = copyList(other._head);
    }

    // Destructor
    ~ListLS() {
        clear();
    }

    // Operador de asignación
    ListLS<T>& operator=(const ListLS<T>& other) {
        if (this != &other) {
            clear();
            _head = copyList(other._head);
        }
        return *this;
    }

    // Agregar elemento al inicio (cons)
    void cons(T data) {
        _head = new Node<T>(data, _head);
    }

    // Verificar si está vacía
    bool isEmpty() const {
        return _head == nullptr;
    }

    // Obtener primer elemento (head)
    T head() const {
        if (isEmpty()) {
            throw std::underflow_error("Lista vacia - no hay head");
        }
        return _head->data;
    }

    // Obtener el resto de la lista (tail)
    ListLS<T> tail() const {
        if (isEmpty()) {
            throw std::underflow_error("Lista vacia - no hay tail");
        }
        ListLS<T> result;
        result._head = copyList(_head->next);
        return result;
    }

    // Longitud de la lista
    int length() const {
        int count = 0;
        Node<T>* current = _head;
        while (current != nullptr) {
            count++;
            current = current->next;
        }
        return count;
    }

    // Getter para _head (necesario para el binding)
    Node<T>* getHead() const {
        return _head;
    }

    // Operador << para impresión
    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const ListLS<U>& list);

protected:
    Node<T>* _head;

private:
    // Función auxiliar para copiar lista - HACERLA CONST
    Node<T>* copyList(Node<T>* other) const {  // <--- Agregar 'const' aquí
        if (other == nullptr) return nullptr;

        Node<T>* newHead = new Node<T>(other->data);
        Node<T>* currentNew = newHead;
        Node<T>* currentOther = other->next;

        while (currentOther != nullptr) {
            currentNew->next = new Node<T>(currentOther->data);
            currentNew = currentNew->next;
            currentOther = currentOther->next;
        }
        return newHead;
    }

    // Limpiar lista
    void clear() {
        while (_head != nullptr) {
            Node<T>* temp = _head;
            _head = _head->next;
            delete temp;
        }
    }
};

// Implementación del operador <<
template <typename T>
std::ostream& operator<<(std::ostream& os, const ListLS<T>& list) {
    os << "[ ";
    Node<T>* current = list._head;
    while (current != nullptr) {
        os << current->data;
        if (current->next != nullptr) {
            os << ", ";
        }
        current = current->next;
    }
    os << " ]";
    return os;
}

} //End namespace

#endif // __C_LISTLS__
