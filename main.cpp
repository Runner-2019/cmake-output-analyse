#include <fstream>
#include <iostream>
#include <optional>
#include <sstream>
#include <string>
#include <vector>

namespace detail {
using namespace std;

// line should be
// "[digit/digit] other other -o object.o -c file.cpp"
// "Elapsed time: xx s. xxxx"

std::string ReadCmakeOutputFile(const std::string &file_path) {
  ifstream ifs(file_path, ios::in);
  if (!ifs.is_open()) {
    cout << "open " << file_path << " fail." << endl;
    exit(0);
  }
  std::stringstream buffer{};
  buffer << ifs.rdbuf();
  ifs.close();
  return buffer.str();
}

bool IsValidLine(const std::string &line) {}

vector<string> SplitByChar(const std::string &content, char delim) {

  // for(int i = 0; i < )
}

vector<string> GetFinalResult() {}

}; // namespace detail

int main(int argc, char *argv[]) { return 0; }
