#include <filesystem>
#include <iostream>
#include <string>
#include <vector>

namespace detail {
using namespace std;
using StrVec = vector<string>;

// line should be
// "[digit/digit] other other -o object.o -c file.cpp"
// "Elapsed time: xx s. xxxx"

std::string ReadCmakeOutputFile(const std::string &file_path) {
  // Get size of file to know how much memory to allocate
  std::uintmax_t filesize = std::filesystem::file_size("C037B221110.bin");
  // Allocate buffer to hold file
  char *buf = new char[filesize];
  // Read file
  std::ifstream fin("C037B221110.bin", std::ios::binary);
  fin.read(buf, filesize);
  if (!fin) {
    std::cerr << "Error reading file, could only read " << fin.gcount()
              << " bytes" << std::endl;
  }
  // Close file
  fin.close();
}

bool IsValidLine(const std::string &line) {}

StrVec SplitBySpace() {}

vector<string> GetFinalResult() {}

}; // namespace detail

int main(int argc, char *argv[]) { return 0; }
