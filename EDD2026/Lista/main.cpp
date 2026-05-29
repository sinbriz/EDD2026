#include <iostream>

using namespace std;

// Definition of node
struct Node {
    Node(char aData, Node* aNext):
         data(aData), next(aNext)
    {

    }
    char data;
    Node* next;
};
using ListLS = Node;

void imprimir(ListLS* l) {
    Node *node  = l;
    if (node == nullptr) {
        cout << "NULL" << endl;
        return;
    }

    cout << node->data << " -> ";
    imprimir(node->next);
}

void imp(ListLS* l) {
    Node *node = l;

    if (node == nullptr) {
        // cout << "NULL" << endl;
        cout << endl;
        return;
    }

    cout << node->data << ", ";
    imp(node->next);
}
int len(ListLS* l) {
    Node *node = l;

    if (node == nullptr)
        return 0;

    return 1 + len(node->next);
}

int main()
{
    ListLS *l = new Node('A', new Node('H', new Node('U', nullptr)));

    cout << "l: "; imprimir(l);
    cout << "len(l): " << len(l) << endl;

    return 0;
}
