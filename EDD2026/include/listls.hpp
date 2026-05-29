#ifndef __LISTLS__
#define __LISTLS__

#include <iostream>
#include <exception>
#include <sstream>


using namespace std;

namespace ed {

// Definition of node
template <class T>
struct Node {
    Node(T aData, Node<T>* aNext):
         data(aData), next(aNext)
    {}
    T data;
    Node<T>* next;
};

template <class T>
using ListLS = Node<T>*;


template <class T>
ListLS<T>  empty()
{
    return nullptr;
}

template <class T>
ListLS<T> cons(T data, ListLS<T> ls)
{
    Node<T>*  newNode = new Node<T>(data,ls);
    return newNode;
}

template <class T>
inline bool isEmpty(ListLS<T> ls)
{
    return (ls == nullptr);
}


template <class T>
T head(ListLS<T> ls)
{
    if ( isEmpty(ls) ) {
      std::ostringstream msj;
       msj <<  "ERROR: list is empty";
      throw std::underflow_error(msj.str());
    }
    return ls->data;
}

/*O(n)
*/
template <class T>
T tail(ListLS<T> ls)
{
    if ( isEmpty(ls) ) {
      std::ostringstream msj;
       msj <<  "ERROR: list is empty";
      throw std::underflow_error(msj.str());
    }
    if (isEmpty(rest(ls)))
        return head(ls);
    return tail(rest(ls));

}

template <class T>
inline ListLS<T> rest(ListLS<T> ls)
{
    if ( isEmpty(ls) ) {
      std::ostringstream msj;
       msj <<  "ERROR: list is empty";
      throw std::underflow_error(msj.str());
    }
    return ls->next;
}

template <class T>
ListLS<T> deleteLS(ListLS<T> ls)
{
    while ( !isEmpty(ls) ) {
        Node<T>*  inode = ls;//head(ls);
        ls = rest(ls);
        delete inode;
    }
    return empty<T>();
}

template <class T>
std::ostream&  operator << ( std::ostream &out, ListLS<T> ls)
{
   out << "[";
    while (!isEmpty(ls)) {
        out << head(ls);
        ls = rest(ls);
        if (!isEmpty(ls))
          out << ",";
    }
   out << "]";
   return out;
}

} //End namespace

#endif // __LISTLS__
