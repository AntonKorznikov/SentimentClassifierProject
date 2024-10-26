#include <iostream>
#include <filesystem>
#include <string>

namespace fs = std::filesystem;

const std::string INPUT_RAW_DIR = "examples/input_raw";
const std::string INPUT_DIR = "examples/input";

void preprocess() {
    // Check if the input directory exists; if not, create it
    if (!fs::exists(INPUT_DIR)) {
        fs::create_directories(INPUT_DIR);
    }

    // Iterate through the files in the input_raw directory
    for (const auto& entry : fs::directory_iterator(INPUT_RAW_DIR)) {
        if (entry.is_regular_file() && entry.path().extension() == ".txt") {
            // Copy the file to the input directory
            fs::copy(entry.path(), INPUT_DIR + "/" + entry.path().filename().string());
        }
    }

    std::cout << "Preprocessing completed." << std::endl;
}

int main() {
    preprocess();
    return 0;
}
