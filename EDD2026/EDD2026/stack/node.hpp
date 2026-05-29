#ifndef __NODE_HPP__
#define  __NODE_HPP__

#include <iostream>
#include <exception>
#include <sstream>


namespace ed {

template <class T>
struct Node {
    Node(T aData, Node<T>* aNext):
         data(aData), next(aNext)
    {}
    T data;
    Node<T>* next;
};

} //end namespace

#endif //__NODE_HPP__
