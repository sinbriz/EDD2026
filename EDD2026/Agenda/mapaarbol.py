"""
Implementación de un Red-Black Tree basada en CLRS 4th Edition.
Funciona como un mapa/diccionario ordenado.
"""

class MapaArbolRojoNegro:
    """Árbol Rojo-Negro que funciona como diccionario ordenado."""
    
    RED = 0
    BLACK = 1
    
    class Node:
        """Nodo del árbol con clave, valor y color."""
        
        __slots__ = ('key', 'value', 'color', 'parent', 'left', 'right')
        
        def __init__(self, key, value, color=None):
            self.key = key
            self.value = value
            self.color = color if color is not None else MapaArbolRojoNegro.RED
            self.parent = None
            self.left = None
            self.right = None
        
        def __str__(self):
            color_str = "RED" if self.color == MapaArbolRojoNegro.RED else "BLACK"
            return f"{self.key}:{self.value}({color_str})"
    
    def __init__(self):
        """Inicializa un árbol vacío con centinela NIL."""
        self.NIL = self.Node(None, None, color=self.BLACK)
        self.root = self.NIL
        self._size = 0
    
    # ==================== UTILIDADES ====================
    
    def _is_red(self, node):
        return node is not None and node != self.NIL and node.color == self.RED
    
    def _is_black(self, node):
        return node is None or node == self.NIL or node.color == self.BLACK
    
    def _set_red(self, node):
        if node and node != self.NIL:
            node.color = self.RED
    
    def _set_black(self, node):
        if node and node != self.NIL:
            node.color = self.BLACK
    
    # ==================== ROTACIONES ====================
    
    def left_rotate(self, x):
        """LEFT-ROTATE(T, x)"""
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
        """RIGHT-ROTATE(T, x)"""
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
        """RB-INSERT - Inserta o actualiza un par clave-valor."""
        z = self.Node(key, value, color=self.RED)
        
        y = self.NIL
        x = self.root
        
        while x != self.NIL:
            y = x
            if z.key < x.key:
                x = x.left
            elif z.key > x.key:
                x = x.right
            else:
                # Clave existente: actualizar valor
                x.value = value
                return
        
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
        """RB-INSERT-FIXUP - Restaura propiedades después de insertar."""
        while self._is_red(z.parent):
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if self._is_red(y):
                    # Caso 1: tío rojo
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
            else:
                y = z.parent.parent.left
                if self._is_red(y):
                    self._set_black(z.parent)
                    self._set_black(y)
                    self._set_red(z.parent.parent)
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    self._set_black(z.parent)
                    self._set_red(z.parent.parent)
                    self.left_rotate(z.parent.parent)
        
        self._set_black(self.root)
    
    # ==================== ELIMINACIÓN ====================
    
    def delete(self, key):
        """RB-DELETE - Elimina un contacto por su nombre."""
        z = self._search_node(self.root, key)
        if z == self.NIL:
            return False
        
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
        return True
    
    def _transplant(self, u, v):
        """Reemplaza el subárbol u por v."""
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
    
    def _minimum(self, node):
        """Nodo con clave mínima en el subárbol."""
        while node.left != self.NIL:
            node = node.left
        return node
    
    def _delete_fixup(self, x):
        """RB-DELETE-FIXUP - Restaura propiedades después de eliminar."""
        while x != self.root and self._is_black(x):
            if x == x.parent.left:
                w = x.parent.right
                
                if self._is_red(w):
                    self._set_black(w)
                    self._set_red(x.parent)
                    self.left_rotate(x.parent)
                    w = x.parent.right
                
                if self._is_black(w.left) and self._is_black(w.right):
                    self._set_red(w)
                    x = x.parent
                else:
                    if self._is_black(w.right):
                        self._set_black(w.left)
                        self._set_red(w)
                        self.right_rotate(w)
                        w = x.parent.right
                    
                    w.color = x.parent.color
                    self._set_black(x.parent)
                    self._set_black(w.right)
                    self.left_rotate(x.parent)
                    x = self.root
            else:
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
        """Busca un contacto por su nombre (clave)."""
        node = self._search_node(self.root, key)
        if node != self.NIL:
            return node.value
        return None
    
    def contains(self, key):
        """Verifica si un contacto existe."""
        return self._search_node(self.root, key) != self.NIL
    
    # ==================== OPERACIONES DE DICCIONARIO ====================
    
    def __setitem__(self, key, value):
        self.insert(key, value)
    
    def __getitem__(self, key):
        node = self._search_node(self.root, key)
        if node != self.NIL:
            return node.value
        raise KeyError(f"Contacto '{key}' no encontrado")
    
    def __contains__(self, key):
        return self.contains(key)
    
    def __len__(self):
        return self._size
    
    # ==================== ITERACIÓN ORDENADA (INORDER) ====================
    
    def _inorder_traversal(self, node, result):
        """Recorrido inorder recursivo (claves ordenadas)."""
        if node != self.NIL:
            self._inorder_traversal(node.left, result)
            result.append((node.key, node.value))
            self._inorder_traversal(node.right, result)
    
    def items(self):
        """Devuelve lista de (nombre, contacto) en orden alfabético."""
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def keys(self):
        """Devuelve lista de nombres en orden alfabético."""
        return [k for k, v in self.items()]
    
    def values(self):
        """Devuelve lista de contactos en orden alfabético por nombre."""
        return [v for k, v in self.items()]
    
    def get_all_contacts(self):
        """Obtiene todos los contactos ordenados alfabéticamente."""
        return self.items()
    
    # ==================== VALIDACIÓN ====================
    
    def is_valid_red_black_tree(self):
        """Verifica que se cumplan todas las propiedades RBT."""
        if self.root == self.NIL:
            return True
        
        if self._is_red(self.root):
            return False
        
        return self._check_black_height(self.root) != -1
    
    def _check_black_height(self, node):
        """Verifica consistencia de altura negra."""
        if node == self.NIL:
            return 1
        
        left = self._check_black_height(node.left)
        right = self._check_black_height(node.right)
        
        if left == -1 or right == -1 or left != right:
            return -1
        
        return left + (1 if self._is_black(node) else 0)