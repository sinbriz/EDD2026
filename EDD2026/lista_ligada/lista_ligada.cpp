#include <nanobind/nanobind.h>
#include <nanobind/stl/string.h>
#include <nanobind/stl/vector.h>
#include <nanobind/make_iterator.h>
#include "listls.hpp"

namespace nb = nanobind;
using namespace nb::literals;
using namespace ed;

template <typename T>
void bind_list_methods(nb::module_ &m, const std::string &type_name) {
    std::string class_name = "List" + type_name;

    // Binding de la clase ListLS
    nb::class_<ListLS<T>>(m, class_name.c_str())
        // Constructor
        .def(nb::init<>())

        // Métodos funcionales (cons, head, tail)
        .def("cons", &ListLS<T>::cons, "data"_a)
        .def("isEmpty", &ListLS<T>::isEmpty)
        .def("head", &ListLS<T>::head)
        .def("tail", &ListLS<T>::tail)
        .def("length", &ListLS<T>::length)

        // Métodos Python estándar
        .def("__len__", &ListLS<T>::length)
        .def("__bool__", [](const ListLS<T>& ls) { return !ls.isEmpty(); })

        // Representación como string
        .def("__repr__", [](const ListLS<T>& ls) {
            std::ostringstream oss;
            oss << ls;
            return oss.str();
        })

        // Convertir a lista de Python
        .def("to_list", [](const ListLS<T>& ls) {
            nb::list result;
            auto current = ls;  // Copia
            while (!current.isEmpty()) {
                result.append(current.head());
                current = current.tail();
            }
            return result;
        })

        // Constructor desde lista de Python
        .def_static("from_list", [](const nb::list& lst) {
            ListLS<T> result;
            // Agregar en orden inverso para mantener el orden
            for (int i = lst.size() - 1; i >= 0; i--) {
                result.cons(nb::cast<T>(lst[i]));
            }
            return result;
        })

        // Operador de índice (acceso por posición)
        .def("__getitem__", [](const ListLS<T>& ls, int index) {
            if (index < 0 || index >= ls.length()) {
                throw std::out_of_range("Indice fuera de rango");
            }
            auto current = ls;
            for (int i = 0; i < index; i++) {
                current = current.tail();
            }
            return current.head();
        });

    // Binding de Node (opcional, para exponer la estructura interna)
    std::string node_name = "Node" + type_name;
    nb::class_<Node<T>>(m, node_name.c_str())
        .def_ro("data", &Node<T>::data)
        .def_prop_ro("next", [](Node<T>* node) {
            return node->next;
        });
}

// Módulo principal
NB_MODULE(m_listls, m) {
    // Bind para enteros
    bind_list_methods<int>(m, "Int");

    // Bind para strings (opcional)
    bind_list_methods<std::string>(m, "String");

    // Registrar excepciones
    nb::exception<std::underflow_error>(m, "UnderflowError");
    nb::exception<std::out_of_range>(m, "OutOfRangeError");

    // Documentación del módulo
    m.doc() = "Modulo de listas ligadas implementadas en C++";
}
