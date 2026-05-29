"""
Agenda de Contactos con Red-Black Tree y Tkinter.
Estructuras de Datos Avanzadas
"""

import tkinter as tk
from tkinter import ttk, messagebox
from mapaarbol import MapaArbolRojoNegro


class Contacto:
    """Clase que representa un contacto."""
    
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):
        return f"{self.nombre} - {self.telefono} - {self.email}"


class AgendaContactosApp:
    """Aplicación principal de agenda de contactos."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contactos - Red-Black Tree")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Instanciar el Red-Black Tree
        self.agenda = MapaArbolRojoNegro()
        
        # Configurar la interfaz
        self._setup_ui()
        
        # Cargar contactos de prueba
        self._cargar_contactos_prueba()
        
        # Actualizar la tabla
        self.actualizar_tabla()
    
    def _setup_ui(self):
        """Configura todos los elementos de la interfaz."""
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configurar pesos para que la ventana sea responsive
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        # ========== TÍTULO ==========
        titulo = ttk.Label(main_frame, text="📒 Agenda de Contactos", 
                          font=('Arial', 16, 'bold'))
        titulo.grid(row=0, column=0, pady=10)
        
        # ========== FRAME DE ENTRADA ==========
        input_frame = ttk.LabelFrame(main_frame, text="Datos del Contacto", padding="10")
        input_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=10)
        input_frame.columnconfigure(1, weight=1)
        
        # Campo Nombre
        ttk.Label(input_frame, text="Nombre:*").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        self.nombre_entry = ttk.Entry(input_frame, textvariable=self.nombre_var, width=30)
        self.nombre_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Campo Teléfono
        ttk.Label(input_frame, text="Teléfono:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.telefono_var = tk.StringVar()
        self.telefono_entry = ttk.Entry(input_frame, textvariable=self.telefono_var, width=30)
        self.telefono_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Campo Email
        ttk.Label(input_frame, text="Email:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(input_frame, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # ========== BOTONES ==========
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, pady=10)
        
        self.btn_agregar = ttk.Button(button_frame, text="Agregar Contacto", 
                                      command=self.agregar_contacto)
        self.btn_agregar.grid(row=0, column=0, padx=5)
        
        self.btn_buscar = ttk.Button(button_frame, text="Buscar Contacto", 
                                     command=self.buscar_contacto)
        self.btn_buscar.grid(row=0, column=1, padx=5)
        
        self.btn_eliminar = ttk.Button(button_frame, text="Eliminar Contacto", 
                                       command=self.eliminar_contacto)
        self.btn_eliminar.grid(row=0, column=2, padx=5)
        
        self.btn_actualizar = ttk.Button(button_frame, text="Actualizar Tabla", 
                                         command=self.actualizar_tabla)
        self.btn_actualizar.grid(row=0, column=3, padx=5)
        
        # ========== TABLA DE CONTACTOS ==========
        table_frame = ttk.LabelFrame(main_frame, text="Contactos (Ordenados Alfabéticamente)", padding="10")
        table_frame.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)
        table_frame.columnconfigure(0, weight=1)
        table_frame.rowconfigure(0, weight=1)
        
        # Treeview con scrollbar
        tree_frame = ttk.Frame(table_frame)
        tree_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        tree_frame.columnconfigure(0, weight=1)
        tree_frame.rowconfigure(0, weight=1)
        
        scrollbar = ttk.Scrollbar(tree_frame)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        self.tree = ttk.Treeview(tree_frame, columns=("nombre", "telefono", "email"), 
                                  show="headings", yscrollcommand=scrollbar.set)
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.config(command=self.tree.yview)
        
        # Configurar columnas
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("telefono", text="Teléfono")
        self.tree.heading("email", text="Email")
        
        self.tree.column("nombre", width=200)
        self.tree.column("telefono", width=150)
        self.tree.column("email", width=250)
        
        # Bind para seleccionar contacto de la tabla
        self.tree.bind('<<TreeviewSelect>>', self._on_select_contacto)
        
        # ========== BARRA DE ESTADO ==========
        self.status_var = tk.StringVar()
        self.status_var.set("Listo ^^ | Estructura: Red-Black Tree")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=5)
        
        # Configurar eventos de teclado
        self.nombre_entry.bind('<Return>', lambda e: self.agregar_contacto())
    
    def _cargar_contactos_prueba(self):
        """Carga los contactos de prueba especificados en el ejercicio."""
        contactos_prueba = [
            ("Juan", "111111", "juan@email.com"),
            ("Ana", "222222", "ana@email.com"),
            ("Carlos", "333333", "carlos@email.com"),
            ("Maria", "444444", "maria@email.com"),
            ("Luis", "555555", "luis@email.com"),
        ]
        
        for nombre, telefono, email in contactos_prueba:
            contacto = Contacto(nombre, telefono, email)
            self.agenda[nombre] = contacto
        
        self.status_var.set(f"Cargados {len(contactos_prueba)} contactos de prueba")
    
    def agregar_contacto(self):
        """Agrega un nuevo contacto al Red-Black Tree."""
        nombre = self.nombre_var.get().strip()
        telefono = self.telefono_var.get().strip()
        email = self.email_var.get().strip()
        
        # Validación: nombre no vacío
        if not nombre:
            messagebox.showwarning("Campo requerido", "El nombre es obligatorio")
            return
        
        # Crear el contacto
        contacto = Contacto(nombre, telefono, email)
        
        # Insertar en el árbol
        self.agenda[nombre] = contacto
        
        # Actualizar interfaz
        self.actualizar_tabla()
        self._limpiar_campos()
        
        self.status_var.set(f"Contacto '{nombre}' agregado correctamente")
        
        # Opcional: mostrar información del árbol
        self._mostrar_info_arbol()
    
    def buscar_contacto(self):
        """Busca un contacto por su nombre."""
        nombre = self.nombre_var.get().strip()
        
        if not nombre:
            messagebox.showinfo("Búsqueda", "Ingrese un nombre para buscar")
            return
        
        contacto = self.agenda.search(nombre)
        
        if contacto:
            # Mostrar en campos
            self.nombre_var.set(contacto.nombre)
            self.telefono_var.set(contacto.telefono)
            self.email_var.set(contacto.email)
            
            # Seleccionar en la tabla
            self._seleccionar_en_tabla(nombre)
            
            self.status_var.set(f"Contacto '{nombre}' encontrado")
            
            # Mostrar mensaje con detalles
            messagebox.showinfo("Contacto Encontrado", 
                               f"Nombre: {contacto.nombre}\n"
                               f"Teléfono: {contacto.telefono}\n"
                               f"Email: {contacto.email}")
        else:
            messagebox.showwarning("No encontrado", f"No existe el contacto '{nombre}'")
            self.status_var.set(f"Contacto '{nombre}' no encontrado")
    
    def eliminar_contacto(self):
        """Elimina el contacto seleccionado o el ingresado en el campo nombre."""
        nombre = self.nombre_var.get().strip()
        
        if not nombre:
            # Intentar obtener selección de la tabla
            seleccion = self.tree.selection()
            if seleccion:
                nombre = self.tree.item(seleccion[0])['values'][0]
            else:
                messagebox.showinfo("Eliminar", "Seleccione un contacto o ingrese un nombre")
                return
        
        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", f"¿Eliminar contacto '{nombre}'?"):
            if self.agenda.delete(nombre):
                self._limpiar_campos()
                self.actualizar_tabla()
                self.status_var.set(f"Contacto '{nombre}' eliminado correctamente")
            else:
                messagebox.showwarning("Error", f"No se pudo eliminar '{nombre}'")
    
    def actualizar_tabla(self):
        """Actualiza la tabla Treeview con los contactos en orden alfabético."""
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obtener todos los contactos ordenados (inorder del RBT)
        contactos_ordenados = self.agenda.get_all_contacts()
        
        # Insertar en la tabla
        for nombre, contacto in contactos_ordenados:
            self.tree.insert("", tk.END, values=(contacto.nombre, contacto.telefono, contacto.email))
        
        total = len(contactos_ordenados)
        self.status_var.set(f"Mostrando {total} contactos ordenados alfabéticamente")
    
    def _limpiar_campos(self):
        """Limpia los campos de entrada."""
        self.nombre_var.set("")
        self.telefono_var.set("")
        self.email_var.set("")
        self.nombre_entry.focus()
    
    def _on_select_contacto(self, event):
        """Maneja la selección de un contacto en la tabla."""
        seleccion = self.tree.selection()
        if seleccion:
            valores = self.tree.item(seleccion[0])['values']
            if valores:
                self.nombre_var.set(valores[0])
                self.telefono_var.set(valores[1])
                self.email_var.set(valores[2])
    
    def _seleccionar_en_tabla(self, nombre):
        """Selecciona un contacto en la tabla por su nombre."""
        for item in self.tree.get_children():
            if self.tree.item(item)['values'][0] == nombre:
                self.tree.selection_set(item)
                self.tree.see(item)
                break
    
    def _mostrar_info_arbol(self):
        """Muestra información del árbol (opcional)."""
        es_valido = self.agenda.is_valid_red_black_tree()
        if es_valido:
            self.status_var.set(self.status_var.get() + " | RBT válido")
        else:
            self.status_var.set(self.status_var.get() + " | RBT inválido")


def main():
    """Función principal para ejecutar la aplicación."""
    root = tk.Tk()
    app = AgendaContactosApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()