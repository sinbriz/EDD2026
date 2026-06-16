#include <iostream>
#include <vector>
using namespace std;

class DisjointSet {
private:
    vector<int> parent;
    vector<int> rank;

public:
    // Inicialización: cada nodo es su propia raíz
    DisjointSet(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    // Find con compresión de caminos (recursivo)
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Compresión
        }
        return parent[x];
    }

    // Unión por rango
    void unionSets(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA != rootB) {
            if (rank[rootA] < rank[rootB]) {
                parent[rootA] = rootB;
            } else if (rank[rootA] > rank[rootB]) {
                parent[rootB] = rootA;
            } else {
                parent[rootB] = rootA;
                rank[rootA]++;
            }
            cout << ">>> Enlace establecido exitosamente entre " << a << " y " << b << "." << endl;
        } else {
            cout << ">>> Alerta: Los nodos " << a << " y " << b << " ya poseen conexion." << endl;
        }
    }

    // Consulta de conectividad
    bool isConnected(int a, int b) {
        return find(a) == find(b);
    }

    // Mostrar estructura interna
    void showStructure() {
        cout << "Padres: ";
        for (int i = 0; i < parent.size(); i++) {
            cout << parent[i] << " ";
        }
        cout << endl;
    }
};

int main() {
    int total_servidores = 6;
    DisjointSet red(total_servidores);

    cout << "=========================================" << endl;
    cout << "SISTEMA DE GESTION DE REDES DINAMICAS (C++)" << endl;
    cout << "=========================================\n" << endl;

    red.unionSets(0, 1);
    red.unionSets(1, 2);
    red.unionSets(3, 4);

    cout << "\n--- Verificacion de Canales de Comunicacion ---" << endl;
    cout << "Servidores 0 y 2: " << (red.isConnected(0, 2) ? "CONECTADOS" : "SIN CONEXION") << endl;
    cout << "Servidores 2 y 3: " << (red.isConnected(2, 3) ? "CONECTADOS" : "SIN CONEXION") << endl;

    cout << "\n--- Interconexion de Subredes (Enlazando 2 con 4) ---" << endl;
    red.unionSets(2, 4);

    cout << "\n--- Verificacion Final de Estado General ---" << endl;
    cout << "Servidores 0 y 3: " << (red.isConnected(0, 3) ? "CONECTADOS" : "SIN CONEXION") << endl;

    // Mostrar estructura interna
    cout << "\n--- Estructura interna (parent) ---" << endl;
    red.showStructure();

    return 0;
}
