#ifndef __C_LIST_TAIL__
#define __C_LIST_TAIL__

#include <iostream>
#include <exception>
#include <sstream>
#include "node.hpp"


using namespace std;

namespace ed {

template <class T>
class ListTail {
public:
    ListTail():
        _head(nullptr), _tail(nullptr), _size(0) {}

    ~ListTail()
    {
        while ( !isEmpty() ) {
            Node<T>*  inode = _head;
            _head = _head->next;
            delete inode;
        }
        _head = nullptr;
    }

   //O(1)
    void addHead(T data)
    {
         Node<T>*  newNode = new Node<T>(data,_head);

        if ( isEmpty()) {
          _tail = newNode;
        }
        _head = newNode;
        _size++;
    }
    //O(1)
    void addTail(T data)
    {
         Node<T>*  newNode = new Node<T>(data,nullptr);
         if (isEmpty()) {
            _head = newNode;
         }
         else {
           _tail->next = newNode;
         }
         _tail = newNode;
        _size++;
    }

    bool isEmpty() const
    {
        return (_head == nullptr);
    }

    T head()const
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: list is empty";
            throw std::underflow_error(msj.str());
        }
        return _head->data;
    }

    //Que puedo hacer para mejorar la complejidad de tail?
    //O(n)  --> O(1)
    //O(1) - constant time access to the last element
T tail() const
{
    if ( isEmpty() ) {
        std::ostringstream msj;
        msj <<  "ERROR: list is empty";
        throw std::underflow_error(msj.str());
    }

    return _tail->data;  // Fix: return tail's data, not head's data
}

    /*delHead
    */
    void delHead()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: list is empty";
            throw std::underflow_error(msj.str());
        }
        //caso 2: solo se tiene un data
        if (_head == _tail) {
            delete _head;
            _head = nullptr;
            _tail = nullptr;
        } //caso 3 Se tiene mas de un nodo
        else {
            Node<T>*  inode = _head;
            _head = _head->next;
            delete inode;
        }
        _size--;
    }

    void delTail()
    {
        if (isEmpty()) {
            std::ostringstream msj;
            msj << "ERROR: list is empty";
            throw std::underflow_error(msj.str());
        }

        // Si solo hay un nodo
        if (_head == _tail) {
            delete _head;
            _head = nullptr;
            _tail = nullptr;
        }
        else {
            Node<T>* temp = _head;
            // encontrar el nodo anterior al tail
            while (temp->next != _tail) {
               temp = temp->next;
            }
            delete _tail;
            _tail = temp;
            _tail->next = nullptr;
        }

        _size--;
    }

    int getSize() const
    {
        return _size;
    }

    template <typename U>
    friend std::ostream& operator<<(std::ostream& os, const ed::ListTail<U>& ls);

protected:
    Node<T>* _head;
    Node<T>* _tail;
    int      _size;
};

template <typename U>
std::ostream& operator<<(std::ostream& os, const ed::ListTail<U>& ls)
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

#endif // __C_LIST_TAIL__


