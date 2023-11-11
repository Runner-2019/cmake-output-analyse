#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import os
import sys

class Result:
    def __init__(self):
        self.current_index = -1
        self.total_index = -1
        self.object_name = "undefined"
        self.cpp_name = "undefined"
        self.elapsed_time = -1
        self.mode = "compile" # or link

    def __str__(self):
        return f"{self.current_index:>4}| {self.elapsed_time:>4}| {self.object_name:>70} | {self.cpp_name:<30}"


    def __lt__(self, other):
        return self.elapsed_time < other.elapsed_time

# Global variables.
results = []

# The format of first item is "[x/x]"
def valid_format_of_first_item(first_item:str) -> bool:
    if len(first_item) < 5:
        return False
    if first_item[0] != '[' or first_item[-1] != ']':
        return False
    if '/' not in first_item:
        return False
    return True

def extract_index_from_first_item(first_item:str)->(str,str):
    indexes = first_item.split('/')
    return (str(indexes[0][1:]), str(indexes[1][:-1]))

def find_item_after_this_item(items, item: str) -> str:
    if item not in items:
        return ""
    idx = items.index(item)
    if idx + 1 == len(items):
        print("Shouldn' be there")
        return ""
    return items[idx + 1]


# Return whether this line is compiled line.
# The compiled line should contain indexes, -o, -c.
def handle_compile_line(line:str) -> bool:
    items = line.split()

    # [x/x] -o object -c cpp_source
    if len(items) <= 5:
        return False
    
    first_item = items[0]
    if not valid_format_of_first_item(first_item):
        return False

    object_name = find_item_after_this_item(items, "-o")
    cpp_source = find_item_after_this_item(items, "-c")
    if object_name == "":
        # print("Doesn't find -o, not compiled line.\n")
        return False
    if cpp_source == "":
        # print("Doesn't find -c, not compiled line.\n")
        return False

    # Extrace informations from compile line.
    indexes = extract_index_from_first_item(first_item)

    result = Result()
    result.current_index =  indexes[0]
    result.total_index =  indexes[1]
    result.object_name = object_name.split('/')[-1]
    result.cpp_name = cpp_source.split('/')[-1]
    results.append(result)
    return True

def handle_elapsed_time_line(line:str) -> bool:
    if len(line) < 14 or line[:13] != "Elapsed time:":
        # print("Not elapsed time line.")
        return False

    # Elapsed time: 0 s.
    s_index = line.index('.') - 1
    time_str = line[13:s_index].strip()
    results[-1].elapsed_time = int(time_str)


def handle(file_path:str):
    file = open(file_path, "r")
    line = file.readline()
    while line:
        is_compile_line = handle_compile_line(line)
        if is_compile_line:
            line = file.readline()
            handle_elapsed_time_line(line)
        else:
            # read next line
            line = file.readline()

    # Print result informations.
    if len(results) == 0:
        print("Empty informations.")
        exit(3)
    results.sort()
    for result in results:
        print(str(result))
    print(f"Total objects number: {results[0].total_index}")


if __name__ == "__main__":
    # Check parameters
    if len(sys.argv) != 2:
        print("Usage: python3 analyse.py path-to-cmake-output-file")
        exit(1)
    file_path=sys.argv[1]
    if not os.path.exists(file_path):
        print("The file path: ", file_path, " not exists.\n")
        exit(2)
        
    # Handle
    print("Cmake output file path: ", file_path, "\n")
    handle(file_path)
