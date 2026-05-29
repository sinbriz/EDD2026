#ifndef __C_LISTLS__
#define __C_LISTLS__

#include <iostream>
#include <exception>
#include <sstream>
#include "node.hpp"


using namespace std;

namespace ed {

template <class T>
class ListLS {
public:
    ListLS():
        _head(nullptr), _size(0) {}

    ~ListLS()
    {
        while ( !isEmpty() ) {
            Node<T>*  inode = _head;
            _head = _head->next;
            delete inode;
        }
        _head = nullptr;
    }

   //O(1)
    void cons(T data)
    {
         Node<T>*  newNode = new Node<T>(data,_head);
        _head = newNode;
        _size++;
    }

    bool isEmpty()
    {
        return (_head == nullptr);
    }

    T head()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: list is empty";
            throw std::underflow_error(msj.str());
        }
        return _head->data;
    }

    //Que puedo hacer para mejorar la complejidad de tail?
    T tail()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: list is empty";
            throw std::underflow_error(msj.str());
       }
       Node<T>*  inode = _head;
       while (inode->next != nullptr) {
        inode = inode->next;

       }
       return inode->data;
    }

    /*rest: saca el primero de la lista
    */
    void rest()
    {
        if ( isEmpty() ) {
            std::ostringstream msj;
            msj <<  "ERROR: list is empty";
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
    friend std::ostream& operator<<(std::ostream& os, const ed::ListLS<U>& ls);

protected:
    Node<T>* _head;
    int      _size;
};

template <typename U>
std::ostream& operator<<(std::ostream& os, const ed::ListLS<U>& ls)
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

#endif // __C_LISTLS__


