cmake_minimum_required(VERSION 3.15)
project(m_listls LANGUAGES CXX)

# Configurar estándar C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Buscar Python
find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development.Module)

# Detectar nanobind
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE nanobind_ROOT
)
list(APPEND CMAKE_PREFIX_PATH "${nanobind_ROOT}")

# Ruta manual de nanobind
list(APPEND CMAKE_PREFIX_PATH "C:/Users/brizi/AppData/Local/Python/pythoncore-3.14-64/Lib/site-packages/nanobind/cmake")

# Buscar nanobind
find_package(nanobind CONFIG REQUIRED)

# Incluir directorio actual
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# Crear el módulo (VERIFICA QUE bind_list.cpp EXISTE)
nanobind_add_module(m_listls lista_ligada.cpp)

message(STATUS "Configuración completada para m_listls")