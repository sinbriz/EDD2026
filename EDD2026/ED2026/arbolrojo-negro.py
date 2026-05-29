"""
Implementación de un Red-Black Tree basada en el pseudocódigo de CLRS 4th Edition.
Estructuras de Datos - Práctica: Árboles Rojo-Negro
"""

class RedBlackTree:
    """Implementación de un árbol Rojo-Negro"""
    
    # Colores para los nodos
    RED = 0
    BLACK = 1
    
    class Node:
        """Clase interna que representa un nodo del árbol."""
        
        __slots__ = ('key', 'value', 'color', 'parent', 'left', 'right')
        
        def __init__(self, key, value, color=None):
            self.key = key
            self.value = value
            # Usar RedBlackTree.RED en lugar de RED directamente
            self.color = color if color is not None else RedBlackTree.RED
            self.parent = None
            self.left = None
            self.right = None
        
        def __str__(self):
            color_str = "RED" if self.color == RedBlackTree.RED else "BLACK"
            return f"{self.key}:{self.value}({color_str})"
    
    def __init__(self):
        """
        Inicializa un árbol Rojo-Negro vacío.
        Se utiliza un nodo centinela NIL para simplificar las operaciones.
        """
        self.NIL = self.Node(None, None, color=self.BLACK)
        self.root = self.NIL
        self._size = 0
    
    # ==================== UTILIDADES BÁSICAS ====================
    
    def _is_red(self, node):
        """Verifica si un nodo es rojo."""
        if node is None or node == self.NIL:
            return False
        return node.color == self.RED
    
    def _is_black(self, node):
        """Verifica si un nodo es negro."""
        if node is None or node == self.NIL:
            return True
        return node.color == self.BLACK
    
    def _set_red(self, node):
        """Colorea un nodo de rojo."""
        if node and node != self.NIL:
            node.color = self.RED
    
    def _set_black(self, node):
        """Colorea un nodo de negro."""
        if node and node != self.NIL:
            node.color = self.BLACK
    
    # ==================== ROTACIONES ====================
    
    def left_rotate(self, x):
        """
        LEFT-ROTATE(T, x)
        Realiza una rotación izquierda en el nodo x.
        """
        if x == self.NIL or x.right == self.NIL:
            return
        
        y = x.right
        x.right = y.left
        
        if y.left != self.NIL:
            y.left.parent = x
        
        y.parent = x.parent
        
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        y.left = x
        x.parent = y
    
    def right_rotate(self, x):
        """
        RIGHT-ROTATE(T, x)
        Realiza una rotación derecha en el nodo x.
        """
        if x == self.NIL or x.left == self.NIL:
            return
        
        y = x.left
        x.left = y.right
        
        if y.right != self.NIL:
            y.right.parent = x
        
        y.parent = x.parent
        
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y
    
    # ==================== INSERCIÓN ====================
    
    def insert(self, key, value):
        """
        RB-INSERT(T, z)
        Inserta un nuevo nodo con la clave y valor especificados.
        """
        z = self.Node(key, value, color=self.RED)
        
        y = self.NIL
        x = self.root
        
        # Encontrar la posición de inserción
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                # La clave ya existe, actualizar el valor
                x.value = value
                return
        
        # Insertar el nuevo nodo
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        
        z.left = self.NIL
        z.right = self.NIL
        z.color = self.RED
        
        self._size += 1
        self._insert_fixup(z)
    
    def _insert_fixup(self, z):
        """
        RB-INSERT-FIXUP(T, z)
        Restaura las propiedades del árbol Rojo-Negro después de la inserción.
        """
        while self._is_red(z.parent):
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # tío
                if self._is_red(y):
                    # Caso 1: el tío es rojo
                    self._set_black(z.parent)
                    self._set_black(y)
                    self._set_red(z.parent.parent)
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        # Caso 2: z es hijo derecho
                        z = z.parent
                        self.left_rotate(z)
                    # Caso 3: z es hijo izquierdo
                    self._set_black(z.parent)
                    self._set_red(z.parent.parent)
                    self.right_rotate(z.parent.parent)
            else:  # simétrico: z.parent es hijo derecho
                y = z.parent.parent.left  # tío
                if self._is_red(y):
                    # Caso 1: el tío es rojo
                    self._set_black(z.parent)
                    self._set_black(y)
                    self._set_red(z.parent.parent)
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # Caso 2: z es hijo izquierdo
                        z = z.parent
                        self.right_rotate(z)
                    # Caso 3: z es hijo derecho
                    self._set_black(z.parent)
                    self._set_red(z.parent.parent)
                    self.left_rotate(z.parent.parent)
        
        self._set_black(self.root)
    
    # ==================== ELIMINACIÓN ====================
    
    def _transplant(self, u, v):
        """
        RB-TRANSPLANT(T, u, v)
        Reemplaza el subárbol con raíz u por el subárbol con raíz v.
        """
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        """Encuentra el nodo con la clave mínima en el subárbol."""
        while node.left != self.NIL:
            node = node.left
        return node
    
    def _maximum(self, node):
        """Encuentra el nodo con la clave máxima en el subárbol."""
        while node.right != self.NIL:
            node = node.right
        return node
    
    def delete(self, key):
        """
        RB-DELETE(T, z)
        Elimina el nodo con la clave especificada.
        """
        z = self._search_node(self.root, key)
        if z == self.NIL:
            return
        
        y = z
        y_original_color = y.color
        x = None
        
        if z.left == self.NIL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == self.BLACK:
            self._delete_fixup(x)
        
        self._size -= 1
    
    def _delete_fixup(self, x):
        """
        RB-DELETE-FIXUP(T, x)
        Restaura las propiedades del árbol Rojo-Negro después de la eliminación.
        """
        while x != self.root and self._is_black(x):
            if x == x.parent.left:
                w = x.parent.right  # hermano
                
                if self._is_red(w):
                    # Caso 1: el hermano es rojo
                    self._set_black(w)
                    self._set_red(x.parent)
                    self.left_rotate(x.parent)
                    w = x.parent.right
                
                if self._is_black(w.left) and self._is_black(w.right):
                    # Caso 2: ambos hijos del hermano son negros
                    self._set_red(w)
                    x = x.parent
                else:
                    if self._is_black(w.right):
                        # Caso 3: hijo derecho del hermano es negro
                        self._set_black(w.left)
                        self._set_red(w)
                        self.right_rotate(w)
                        w = x.parent.right
                    
                    # Caso 4: hijo derecho del hermano es rojo
                    w.color = x.parent.color
                    self._set_black(x.parent)
                    self._set_black(w.right)
                    self.left_rotate(x.parent)
                    x = self.root
            else:  # simétrico: x es hijo derecho
                w = x.parent.left
                
                if self._is_red(w):
                    self._set_black(w)
                    self._set_red(x.parent)
                    self.right_rotate(x.parent)
                    w = x.parent.left
                
                if self._is_black(w.right) and self._is_black(w.left):
                    self._set_red(w)
                    x = x.parent
                else:
                    if self._is_black(w.left):
                        self._set_black(w.right)
                        self._set_red(w)
                        self.left_rotate(w)
                        w = x.parent.left
                    
                    w.color = x.parent.color
                    self._set_black(x.parent)
                    self._set_black(w.left)
                    self.right_rotate(x.parent)
                    x = self.root
        
        self._set_black(x)
    
    # ==================== BÚSQUEDA ====================
    
    def _search_node(self, node, key):
        """Busca un nodo por su clave."""
        while node != self.NIL:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return self.NIL
    
    def search(self, key):
        """Busca una clave y devuelve su valor, o None si no existe."""
        node = self._search_node(self.root, key)
        if node != self.NIL:
            return node.value
        return None
    
    def contains(self, key):
        """Verifica si una clave existe en el árbol."""
        return self._search_node(self.root, key) != self.NIL
    
    # ==================== OPERACIONES DE DICCIONARIO ====================
    
    def __setitem__(self, key, value):
        """Soporta tree[key] = value."""
        self.insert(key, value)
    
    def __getitem__(self, key):
        """Soporta value = tree[key]."""
        node = self._search_node(self.root, key)
        if node != self.NIL:
            return node.value
        raise KeyError(f"Key {key} not found")
    
    def __contains__(self, key):
        """Soporta key in tree."""
        return self.contains(key)
    
    def __len__(self):
        """Soporta len(tree)."""
        return self._size
    
    # ==================== ITERACIÓN ORDENADA ====================
    
    def _inorder_traversal(self, node, result):
        """Recorrido inorder recursivo."""
        if node != self.NIL:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)
    
    def items(self):
        """Devuelve una lista de tuplas (clave, valor) en orden ascendente."""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def keys(self):
        """Devuelve una lista de claves en orden ascendente."""
        return [k for k, v in self.items()]
    
    def values(self):
        """Devuelve una lista de valores en orden de clave ascendente."""
        return [v for k, v in self.items()]
    
    def minimum(self):
        """Devuelve la clave mínima."""
        if self.root == self.NIL:
            return None
        return self._minimum(self.root).key
    
    def maximum(self):
        """Devuelve la clave máxima."""
        if self.root == self.NIL:
            return None
        return self._maximum(self.root).key
    
    # ==================== IMPRESIÓN DEL ÁRBOL ====================
    
    def print_tree(self):
        """Imprime una representación visual del árbol."""
        if self.root == self.NIL:
            print("Árbol vacío")
            return
        
        self._print_tree_recursive(self.root, "", True)
    
    def _print_tree_recursive(self, node, prefix, is_left):
        """Método recursivo para imprimir el árbol."""
        if node == self.NIL:
            return
        
        # Determinar el carácter para la conexión
        connector = "L----" if is_left else "R----"
        color_str = "RED" if node.color == self.RED else "BLACK"
        
        # Imprimir el nodo actual
        print(f"{prefix}{connector}{node.key}({color_str})")
        
        # Preparar el prefijo para los hijos
        new_prefix = prefix + ("|    " if not is_left else "     ")
        
        # Imprimir hijos
        self._print_tree_recursive(node.left, new_prefix, True)
        self._print_tree_recursive(node.right, new_prefix, False)
    
    # ==================== VALIDACIÓN ====================
    
    def _validate_red_black_properties(self):
        """Valida las propiedades del árbol Rojo-Negro."""
        if self.root == self.NIL:
            return True
        
        # Propiedad 1: La raíz debe ser negra
        if self._is_red(self.root):
            print("ERROR: La raíz es roja")
            return False
        
        # Propiedad 2: No debe haber dos rojos consecutivos
        if not self._validate_no_consecutive_reds(self.root):
            print("ERROR: Dos nodos rojos consecutivos encontrados")
            return False
        
        # Propiedad 3: Altura negra consistente
        black_height = self._get_black_height(self.root)
        if black_height == -1:
            print("ERROR: Altura negra inconsistente")
            return False
        
        print("Todas las propiedades del árbol Rojo-Negro se cumplen ^^")
        return True
    
    def _validate_no_consecutive_reds(self, node):
        """Valida que no haya dos nodos rojos consecutivos."""
        if node == self.NIL:
            return True
        
        if self._is_red(node):
            if self._is_red(node.left) or self._is_red(node.right):
                return False
        
        return (self._validate_no_consecutive_reds(node.left) and 
                self._validate_no_consecutive_reds(node.right))
    
    def _get_black_height(self, node):
        """Calcula la altura negra del árbol."""
        if node == self.NIL:
            return 1
        
        left_height = self._get_black_height(node.left)
        right_height = self._get_black_height(node.right)
        
        if left_height == -1 or right_height == -1 or left_height != right_height:
            return -1
        
        return left_height + (1 if self._is_black(node) else 0)


# ==================== PROGRAMA DE PRUEBA ====================

def main():
    print("=" * 60)
    print("PRUEBA DE RED-BLACK TREE")
    print("=" * 60)
    
    # Crear el árbol
    tree = RedBlackTree()
    
    print("\nInsertando elementos: 41, 38, 31, 12, 19, 8")
    print("-" * 40)
    
    elementos = [41, 38, 31, 12, 19, 8]
    for elem in elementos:
        tree[elem] = f"Valor_{elem}"
        print(f"Insertado: {elem}")
    
    # Imprimir el árbol después de las inserciones
    print("\nÁrbol después de inserciones:")
    print("-" * 40)
    tree.print_tree()
    
    # Validar propiedades
    print("\nValidando propiedades del árbol...")
    print("-" * 40)
    tree._validate_red_black_properties()
    
    # Mostrar el tamaño del árbol
    print(f"\nTamaño del árbol: {len(tree)} elementos")
    
    # Mostrar elementos ordenados
    print("\nRecorrido inorder (claves ordenadas):")
    print("-" * 40)
    for key, value in tree.items():
        print(f"  {key} -> {value}")
    
    # Pruebas de búsqueda
    print("\nPruebas de búsqueda:")
    print("-" * 40)
    print(f"contains(31): {tree.contains(31)}")
    print(f"search(31): {tree.search(31)}")
    print(f"contains(100): {tree.contains(100)}")
    
    # Operador []
    print(f"tree[19]: {tree[19]}")
    
    # Eliminar nodos: 8, 12, 19
    print("\nEliminando nodos: 8, 12, 19")
    print("-" * 40)
    
    for elem in [8, 12, 19]:
        print(f"Eliminando: {elem}")
        tree.delete(elem)
        print(f"Árbol actualizado:")
        tree.print_tree()
        print()
    
    # Mostrar el árbol final
    print("\nÁrbol final después de eliminaciones:")
    print("-" * 40)
    tree.print_tree()
    
    # Validar propiedades finales
    print("\nValidando propiedades del árbol final...")
    print("-" * 40)
    tree._validate_red_black_properties()
    
    # Mostrar elementos restantes
    print(f"\nTamaño final del árbol: {len(tree)} elementos")
    print("\nElementos restantes en orden:")
    print("-" * 40)
    for key, value in tree.items():
        print(f"  {key} -> {value}")

if __name__ == "__main__":
    main()