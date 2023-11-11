cmake_minimum_required(VERSION 3.11)
project(cmake-output-analyse)

set(CMAKE_EXPORT_COMPILE_COMMANDS on)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_STANDARD 20)
set(SRC_LIST main.cpp)
add_executable(analyse ${SRC_LIST})

