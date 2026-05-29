cmake_minimum_required(VERSION 3.15)
project(m_array)

# Detect the installed nanobind package and import it into CMake
execute_process(
COMMAND "${Python_EXECUTABLE}" -m nanobind --cmake_dir
OUTPUT_STRIP_TRAILING_WHITESPACE
OUTPUT_VARIABLE nanobind_ROOT
)
list(APPEND CMAKE_PREFIX_PATH "${nanobind_ROOT}")

#Si no detecta a nanobin con los pasos anteriores, incluirlo  manualmente
#el path donde esta instalado anobin,r lo general es en la carpeta de Users
# 
list(APPEND CMAKE_PREFIX_PATH "C:/Users/brizi/AppData/Local/Python/pythoncore-3.14-64/Lib/site-packages/nanobind/cmake")

# Try to import all Python components potentially needed by nanobind
find_package(Python 3.8 REQUIRED COMPONENTS Interpreter Development.Module OPTIONAL_COMPONENTS Development.SABIModule)

# Import nanobind through CMake's find_package mechanism
find_package(nanobind CONFIG REQUIRED)

#El nombre el debe ser exactamente igual al del código fuente 
#checar el nombre  en NB_MODULE(example_module, m) { ... } 
#en este ejemplo se llama "example_module"
#

# Add 
include_directories(C:/ed2026/include)
nanobind_add_module(m_array MODULE m_array.cpp)
 


#cmake -DPYTHON_EXECUTABLE=C:/Users/hbrob/AppData/Local/Python/bin/python3.exe
## Set CMAKE_PREFIX_PATH when configuring your project
#cmake -DCMAKE_PREFIX_PATH="/opt/local;/home/user/libs" ..


# Add "include" subdirectory to the search path for 'my_target'
#target_include_directories(my_target PRIVATE 
#    ${CMAKE_CURRENT_SOURCE_DIR}/include
#)

# Add an absolute or relative path to an external library's headers
#target_include_directories(my_target PUBLIC
#    /path/to/external/library/include
#)