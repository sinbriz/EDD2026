class DisjointSet:
    # Inicialización
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find con compresión de caminos
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compresión
        return self.parent[x]

    # Unión por rango
    def union_sets(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
            print(f">>> Enlace establecido exitosamente entre {a} y {b}.")
        else:
            print(f">>> Alerta: Los nodos {a} y {b} ya poseen conexion.")

    def is_connected(self, a, b):
        return self.find(a) == self.find(b)

    def show_structure(self):
        print("Padres:", self.parent)


if __name__ == "__main__":
    total_servidores = 6
    red = DisjointSet(total_servidores)

    print("=========================================")
    print("SISTEMA DE GESTION DE REDES DINAMICAS (PYTHON)")
    print("=========================================\n")

    red.union_sets(0, 1)
    red.union_sets(1, 2)
    red.union_sets(3, 4)

    print("\n--- Verificacion de Canales de Comunicacion ---")
    print(f"Servidores 0 y 2: {'CONECTADOS' if red.is_connected(0, 2) else 'SIN CONEXION'}")
    print(f"Servidores 2 y 3: {'CONECTADOS' if red.is_connected(2, 3) else 'SIN CONEXION'}")

    print("\n--- Interconexion de Subredes (Enlazando 2 con 4) ---")
    red.union_sets(2, 4)

    print("\n--- Verificacion Final de Estado General ---")
    print(f"Servidores 0 y 3: {'CONECTADOS' if red.is_connected(0, 3) else 'SIN CONEXION'}")

    print("\n--- Estructura interna (parent) ---")
    red.show_structure()
