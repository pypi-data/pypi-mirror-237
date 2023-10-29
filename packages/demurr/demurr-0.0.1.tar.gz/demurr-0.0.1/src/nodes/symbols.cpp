#include "nodes/symbols.h"

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>
#include <llvm/Demangle/MicrosoftDemangle.h>

namespace py = pybind11;
namespace msdm = llvm::ms_demangle;

void define_symbol_nodes(
	py::class_<msdm::SymbolNode, msdm::Node> &symbol_class,
	py::class_<msdm::VariableSymbolNode, msdm::SymbolNode> &variable_symbol_class,
	py::module &m) {
    symbol_class
        .def_readonly("name", &msdm::SymbolNode::Name);
    
    py::class_<msdm::SpecialTableSymbolNode, msdm::SymbolNode>(m, "SpecialTableSymbolNode")
        .def_readonly("target_name", &msdm::SpecialTableSymbolNode::TargetName)
        .def_readonly("qualifiers", &msdm::SpecialTableSymbolNode::Quals);
    
    py::class_<msdm::LocalStaticGuardVariableNode, msdm::SymbolNode>(m, "LocalStaticGuardVariableNode")
        .def_readonly("visible", &msdm::LocalStaticGuardVariableNode::IsVisible);

    py::class_<msdm::EncodedStringLiteralNode, msdm::SymbolNode>(m, "EncodedStringLiteralNode")
        .def_readonly("decoded_string", &msdm::EncodedStringLiteralNode::DecodedString)
        .def_readonly("truncated", &msdm::EncodedStringLiteralNode::IsTruncated)
        .def_readonly("char_kind", &msdm::EncodedStringLiteralNode::Char);

    variable_symbol_class
        .def_readonly("storage_class", &msdm::VariableSymbolNode::SC)
        .def_readonly("type", &msdm::VariableSymbolNode::Type);

    py::class_<msdm::FunctionSymbolNode, msdm::SymbolNode>(m, "FunctionSymbolNode")
        .def_readonly("signature", &msdm::FunctionSymbolNode::Signature);
}
