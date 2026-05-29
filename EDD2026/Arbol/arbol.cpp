#include <iostream>
#include <algorithm>
using namespace std;

template <class Elem>
class ArbolBin {
private:
    struct Nodo {
        Elem elem;
        Nodo* izq;
        Nodo* der;
        Nodo(Nodo* i, Elem e, Nodo* d) : izq(i), elem(e), der(d) {}
    };
    Nodo* raiz;

public:
    // Constructor nulo
    ArbolBin() : raiz(nullptr) {}

    // Constructor nodo
    ArbolBin(ArbolBin* i, Elem e, ArbolBin* d) {
        raiz = new Nodo(i->raiz, e, d->raiz);
    }

    // Constructor interno para nodos hoja
    ArbolBin(Elem e) {
        raiz = new Nodo(nullptr, e, nullptr);
    }

    bool es_nulo() { return raiz == nullptr; }

    bool es_hoja() {
        if (es_nulo()) return false;
        return raiz->izq == nullptr && raiz->der == nullptr;
    }

    bool es_ult() {
        if (es_nulo()) return false;
        return (raiz->izq == nullptr || raiz->der == nullptr);
    }

    int num_nodos() { return num_nodos(raiz); }
    int num_nodos(Nodo* n) {
        if (!n) return 0;
        return 1 + num_nodos(n->izq) + num_nodos(n->der);
    }

    int altura() { return altura(raiz); }
    int altura(Nodo* n) {
        if (!n) return 0;
        return 1 + max(altura(n->izq), altura(n->der));
    }

    int camino_min() { return camino_min(raiz); }
    int camino_min(Nodo* n) {
        if (!n) return 0;
        return 1 + min(camino_min(n->izq), camino_min(n->der));
    }

    bool es_completo() {
        return altura() == camino_min();
    }

    int num_hojas() { return num_hojas(raiz); }
    int num_hojas(Nodo* n) {
        if (!n) return 0;
        if (!n->izq && !n->der) return 1;
        return num_hojas(n->izq) + num_hojas(n->der);
    }

    void imprimir_preorden() { imprimir_preorden(raiz); cout << endl; }
    void imprimir_preorden(Nodo* n) {
        if (!n) { cout << "null "; return; }
        cout << n->elem << " ";
        imprimir_preorden(n->izq);
        imprimir_preorden(n->der);
    }
};

int main() {
    // Construcción del árbol:
    //       3
    //      / \
    //     8   5
    //    /   / \
    //   2   1   6
    //      /
    //     9

    ArbolBin<int>* nulo = new ArbolBin<int>();

    ArbolBin<int>* nodo2 = new ArbolBin<int>(nulo, 2, nulo);
    ArbolBin<int>* nodo8 = new ArbolBin<int>(nodo2, 8, nulo);

    ArbolBin<int>* nodo9 = new ArbolBin<int>(nulo, 9, nulo);
    ArbolBin<int>* nodo1 = new ArbolBin<int>(nulo, 1, nulo);
    ArbolBin<int>* nodo6 = new ArbolBin<int>(nodo9, 6, nulo);
    ArbolBin<int>* nodo5 = new ArbolBin<int>(nodo1, 5, nodo6);

    ArbolBin<int>* arbol = new ArbolBin<int>(nodo8, 3, nodo5);

    // Demostración
    cout << "=== ARBOL BINARIO ===" << endl;
    cout << "Preorden: ";
    arbol->imprimir_preorden();

    cout << "Es nulo? " << (arbol->es_nulo() ? "Sí" : "No") << endl;
    cout << "Número de nodos: " << arbol->num_nodos() << endl;
    cout << "Número de hojas: " << arbol->num_hojas() << endl;
    cout << "Altura: " << arbol->altura() << endl;
    cout << "Camino mínimo: " << arbol->camino_min() << endl;
    cout << "Es completo? " << (arbol->es_completo() ? "Sí" : "No") << endl;

    return 0;
}
