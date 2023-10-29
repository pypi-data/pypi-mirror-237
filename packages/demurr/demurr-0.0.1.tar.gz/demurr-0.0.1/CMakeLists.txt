cmake_minimum_required(VERSION 3.17)
project(demurr VERSION 0.0.1)
set(PY_VERSION_SUFFIX "")
set(PY_FULL_VERSION ${PROJECT_VERSION}${PY_VERSION_SUFFIX})

# Make sure that the Python and CMake versions match
if (DEFINED PY_BUILD_CMAKE_PACKAGE_VERSION)
    if (NOT "${PY_BUILD_CMAKE_PACKAGE_VERSION}" MATCHES "^${PY_FULL_VERSION}$")
        message(FATAL_ERROR "Version number does not match "
                             "(${PY_BUILD_CMAKE_PACKAGE_VERSION} - ${PY_FULL_VERSION}).")
    endif()
endif()

if (WIN32)
  add_definitions(-D_CRT_SECURE_NO_WARNINGS)  # The LLVM build sets this.
endif()

# Find the pybind11 package
include(cmake/QueryPythonForPybind11.cmake)
find_pybind11_python_first()

include_directories(src/include)
include_directories(src/third_party/llvm/include)

# Compile the example Python module
pybind11_add_module(_msvc_module MODULE
                    "src/msvc_module.cpp"
                    "src/enums.cpp"
                    "src/nodes/types.cpp"
                    "src/nodes/identifiers.cpp"
                    "src/nodes/symbols.cpp"
                    "src/third_party/llvm/lib/Demangle/MicrosoftDemangle.cpp"
                    "src/third_party/llvm/lib/Demangle/MicrosoftDemangleNodes.cpp")

target_compile_features(_msvc_module PRIVATE cxx_std_17)
target_compile_definitions(_msvc_module PRIVATE
    MODULE_NAME=$<TARGET_FILE_BASE_NAME:_msvc_module>
    VERSION_INFO="${PY_FULL_VERSION}"
)
set_target_properties(_msvc_module PROPERTIES
    CXX_VISIBILITY_PRESET "hidden"
    VISIBILITY_INLINES_HIDDEN true)
if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    target_link_options(_msvc_module PRIVATE "LINKER:--exclude-libs,ALL")
endif()

# Install the Python module
install(TARGETS _msvc_module
        EXCLUDE_FROM_ALL
        COMPONENT python_modules
        DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME})
# Install the debug file for the Python module (Windows only)
if (WIN32)
    install(FILES $<TARGET_PDB_FILE:_msvc_module>
            EXCLUDE_FROM_ALL
            COMPONENT python_modules
            DESTINATION ${PY_BUILD_CMAKE_MODULE_NAME}
            OPTIONAL)
endif()

# Generate stubs for the Python module
option(WITH_PY_STUBS
    "Generate Python stub files (.pyi) for the Python module." On)
if (WITH_PY_STUBS AND NOT CMAKE_CROSSCOMPILING)
    include(cmake/Pybind11Stubgen.cmake)
    pybind11_stubgen(_msvc_module)
    pybind11_stubgen_install(_msvc_module ${PY_BUILD_CMAKE_MODULE_NAME})
endif()