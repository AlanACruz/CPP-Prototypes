from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
# from conan.tools.cmake import CMake, cmake_layout


class TestMd5Conan(ConanFile):
    name = "TestMd5"
    version = "0.1"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    # generators = "CMakeToolchain", "CMakeDeps"
    
    # options = {"shared": [True, False], "fPIC": [True, False]}
    # default_options = {"shared": False, "fPIC": True}

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def requirements(self):
        # self.requires("gcc/15.2.0")
        self.requires("poco/1.15.2")
        self.requires("gtest/1.17.0")

    def build_requirements(self):
        self.tool_requires("cmake/4.2.3")

    # def config_options(self):
    #     if self.settings.os == "Windows":
    #         del self.options.fPIC

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hello"]
