cmake_minimum_required(VERSION 3.15)
project(ListLSProject LANGUAGES CXX)

# Configurar estándar C++
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Encontrar Python
find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development.Module)
message(STATUS "Python encontrado: ${Python_EXECUTABLE}")

# Detectar nanobind
execute_process(
    COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
    OUTPUT_STRIP_TRAILING_WHITESPACE
    OUTPUT_VARIABLE nanobind_ROOT
)
message(STATUS "nanobind_ROOT: ${nanobind_ROOT}")

# Si no se encuentra nanobind, usar ruta alternativa
if(NOT EXISTS "${nanobind_ROOT}" OR "${nanobind_ROOT}" STREQUAL "")
    set(nanobind_FALLBACK "C:/Users/brizi/AppData/Local/Python/pythoncore-3.14-64/Lib/site-packages/nanobind/cmake")
    message(STATUS "Usando ruta alternativa: ${nanobind_FALLBACK}")
    list(APPEND CMAKE_PREFIX_PATH "${nanobind_FALLBACK}")
endif()

# Importar nanobind
find_package(nanobind CONFIG REQUIRED)
message(STATUS "nanobind encontrado")

include_directories(${CMAKE_CURRENT_SOURCE_DIR})
nanobind_add_module(main main.cpp)

message(STATUS "Configuración completada exitosamente")