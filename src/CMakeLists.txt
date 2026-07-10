add_executable(md5 md5.cpp)

find_package(Poco REQUIRED)

# target_link_libraries(md5 ${CONAN_LIBS})
target_link_libraries(md5 Poco::Poco)
# target_link_libraries(${PROJECT_NAME} Poco::Poco)