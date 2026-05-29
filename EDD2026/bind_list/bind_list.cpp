#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h> // Para manejo de excepciones y strings
#include "listls.hpp"

namespace nb = nanobind;
using namespace nb::literals; // <--- ESTA LÍNEA CORRIGE EL ERROR
using namespace ed;

// Helper para instanciar el módulo para un tipo T específico
template <typename T>
void bind_list_methods(nb::module_ &m, const std::string &type_name) {
    std::string class_name = "List" + type_name;

    // Registramos el Nodo (ListLS es un alias de Node<T>*)
    nb::class_<Node<T>>(m, class_name.c_str())
        .def_ro("data", &Node<T>::data)
        .def_ro("next", &Node<T>::next)
        // Mapeo del operator << a Python __repr__
        .def("__repr__", [](ListLS<T> ls) {
            std::ostringstream oss;
            oss << ls; // Llama a ed::operator<<
            return oss.str();
        });

    // Registramos las funciones del namespace ed
    //m.def("empty", &empty<T>);
    // En lugar de: m.def("empty", &empty<T>);
    // Usa una lambda para evitar ambigüedades:
    m.def("empty", []() {
      return ed::empty<T>();
    });
   // m.def("cons", &cons<T>, "data"_a, "ls"_a);
    m.def("cons", [](int data, Node<int>* ls) {
        return ed::cons(data, ls);
     }, "data"_a, "ls"_a = nb::none()); // Permite que sea None por defecto
    m.def("is_empty", &isEmpty<T>, "ls"_a);
    m.def("head", &head<T>, "ls"_a);
    m.def("rest", &rest<T>, "ls"_a);
    m.def("tail", &tail<T>, "ls"_a);
    /*
    El error en m.def("delete_ls", &deleteLS<T>, "ls"_a); se debe a una incompatibilidad de tipos y un conflicto de gestión de memoria entre Python y C++:
Paso de None: Al igual que con cons, si intentas pasar una lista vacía (None en Python) a delete_ls, Nanobind lo rechazará porque el argumento ls no permite valores nulos por defecto.
Doble liberación (Double Free): Si la lista fue creada en Python, Nanobind asume la propiedad del objeto. Si C++ ejecuta delete sobre esos nodos y luego Python intenta recolectar la basura (garbage collection), el programa fallará (segmentation fault) al intentar liberar memoria ya liberada.
Uso de alias: ListLS<T> es un alias de Node<T>*. Nanobind a veces tiene dificultades para deducir automáticamente la conversión de punteros crudos (raw pointers) si no se especifica explícitamente cómo manejar la propiedad del objeto.
nanobind documentation
nanobind documentation
 +4
    */
   // m.def("delete_ls", &deleteLS<T>, "ls"_a);
   m.def("delete_ls", [](ListLS<T> ls) {
    return ed::deleteLS<T>(ls);
}, "ls"_a.none()); // Permite pasar None (lista vacía)
}

NB_MODULE(m_listls, m) {
    // Instanciamos la lista para enteros (puedes añadir más tipos aquí)
    bind_list_methods<int>(m, "Int");

    // Opcional: registrar la excepción de subflujo
    //nb::register_exception<std::underflow_error>(m, "UnderflowError");
    nb::exception<std::underflow_error>(m, "UnderflowError");
}
