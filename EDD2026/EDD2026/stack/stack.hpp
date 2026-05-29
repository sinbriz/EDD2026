#ifndef __STACK_HPP__
#define __STACK_HPP__

#include <iostream>
#include <exception>
#include <sstream>
//#include <nanobind/nanobind.h>
#include "node.hpp"


using namespace std;
//namespace nb = nanobind;

namespace ed {

template <class T>
class Stack {
public:
    Stack():
        _head(nullptr), _size(0) {}

    ~Stack()
    {
        while ( !isEmpty() ) {
            Node<T>*  inode = _head;
            _head = _head->next;
            delete inode;
        }
        _head = nullptr;
    }

   //O(1)
    void push(T elem)
    {
         Node<T>*  newNode = new Node<T>(elem,_head);
        _head = newNode;
        _size++;
    }

    bool isEmpty() const
    {
        return (_head == nullptr);
    }

    T top()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: stack is empty";
            throw std::underflow_error(msj.str());
        }
        return _head->data;
    }

    /*rest: saca el primero de la lista
    */
    void pop()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: stack is empty";
            throw std::underflow_error(msj.str());
        }
        Node<T>*  inode = _head;
        _head = _head->next;
        delete inode;
        _size--;
    }

    int getSize() const
    {
        return _size;
    }

    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const ed::Stack<U>& ls);

protected:
    Node<T>* _head;
    int      _size;
};

template <typename U>
std::ostream& operator<<(std::ostream& os, const ed::Stack<U>& ls)
{
     Node<U>*  inode = ls._head;
    os << "[";
    while (inode != nullptr) {
        os << inode->data;
        inode = inode->next;
        if (inode != nullptr)
          os << ",";
    }
   os << "]";
   return os;
}

} //End namespace

#endif // __STACK_HPP__

/*
EL TDA

Sorts
  Stack
  Elem
  Bool
  Nat

Operaciones

Constructores
empty : → Stack  (Constructora)
push  : Stack × Elem → Stack (ok)

Observadores
pop    : Stack → Stack
top    : Stack → Elem
empty? : Stack → Bool
size   : Stack → Nat

Axiomas

Variables
s : Stack
x : Elem

Propiedades de pila vacía
empty?(empty) = true

size(empty) = 0
Propiedades después de insertar
empty?(push(s, x)) = false

size(push(s, x)) = size(s) + 1
Propiedad del elemento superior
top(push(s, x)) = x
Propiedad de eliminación
pop(push(s, x)) = s
Precondiciones
top(empty)  indefinido

pop(empty)  indefinido

*/
