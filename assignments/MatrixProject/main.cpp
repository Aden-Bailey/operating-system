#include <iostream>
#include <vector>
#include <chrono>
#include "matrix_math.h"

static volatile double sink = 0.0;

int main() {
    MatrixProcessor processor;

    const size_t size = 1'000'000;
    std::vector<double> a(size, 1.0);
    std::vector<double> b(size, 2.0);

    auto start = std::chrono::high_resolution_clock::now();
    std::vector<double> result = processor.addVectors(a, b);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;

    sink += result[0]; // prevents optimizer removing work

    std::cout << "Vector size: " << size << "\n";
    std::cout << "Time (s): " << elapsed.count() << "\n";
    std::cout << "Throughput (million adds/sec): "
        << (size / elapsed.count()) / 1e6 << "\n";

    return 0;
}