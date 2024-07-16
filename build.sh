cd ~/git/CPP-Prototypes

mkdir build
cd build

# https://docs.conan.io/1/getting_started.html
conan profile new default --detect  # Generates default profile detecting GCC and sets old ABI
conan profile update settings.compiler.libcxx=libstdc++11 default  # Sets libcxx to C++11 ABI

conan install ..

cmake .. -G "Unix Makefiles" -DCMAKE_BUILD_TYPE=Release
cmake --build .

# https://docs.conan.io/1/creating_packages/getting_started.html
conan build .