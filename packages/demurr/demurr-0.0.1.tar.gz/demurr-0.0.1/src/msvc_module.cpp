#include "enums.h"
#include "nodes/array.h"
#include "nodes/types.h"
#include "nodes/identifiers.h"
#include "nodes/symbols.h"

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <array>
#include <string>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>
#include <llvm/Demangle/MicrosoftDemangle.h>

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace msdm = llvm::ms_demangle;
namespace py = pybind11;

PYBIND11_MODULE(MODULE_NAME, m) {
    m.doc() = "Internal module to interface with llvm::ms_demangle";

    m.attr("__version__") = VERSION_INFO;

    define_enums(m);
    py::class_<msdm::Node>(m, "Node")
        .def_property_readonly("kind", &msdm::Node::kind)
        .def("__str__", [](const msdm::Node &node) {
            return node.toString();
        });

    auto qualified_name_class = py::class_<msdm::QualifiedNameNode, msdm::Node>(m, "QualifiedNameNode");

    auto identifier_class = py::class_<msdm::IdentifierNode, msdm::Node>(m, "IdentifierNode");
    
    auto symbol_class = py::class_<msdm::SymbolNode, msdm::Node>(m, "SymbolNode");
    auto variable_symbol_class = py::class_<msdm::VariableSymbolNode, msdm::SymbolNode>(m, "VariableSymbolNode");

    define_type_nodes(m);
    define_identifier_nodes(identifier_class, m);

    qualified_name_class 
        .def_readonly("components", &msdm::QualifiedNameNode::Components);

    py::class_<msdm::TemplateParameterReferenceNode, msdm::Node>(m, "TemplateParameterReferenceNode")
        .def_readonly("symbol", &msdm::TemplateParameterReferenceNode::Symbol)
        .def_readonly("thunk_offset_count", &msdm::TemplateParameterReferenceNode::ThunkOffsetCount)
        .def_readonly("ThunkOffsets", &msdm::TemplateParameterReferenceNode::ThunkOffsets)
        .def_readonly("affinity", &msdm::TemplateParameterReferenceNode::Affinity)
        .def_readonly("is_member_pointer", &msdm::TemplateParameterReferenceNode::IsMemberPointer);

    py::class_<msdm::IntegerLiteralNode, msdm::Node>(m, "IntegerLiteralNode")
        .def_readonly("value", &msdm::IntegerLiteralNode::Value)
        .def_readonly("negative", &msdm::IntegerLiteralNode::IsNegative);

    define_symbol_nodes(symbol_class, variable_symbol_class, m);

    py::class_<msdm::Demangler>(m, "Demangler")
        .def(py::init<>())
        .def("parse", &msdm::Demangler::parse,
            py::keep_alive<1, 2>(),
            py::return_value_policy::reference)
        .def_readonly("error", &msdm::Demangler::Error);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
