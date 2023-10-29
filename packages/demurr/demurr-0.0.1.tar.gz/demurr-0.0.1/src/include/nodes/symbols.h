#pragma once

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>

namespace msdm = llvm::ms_demangle;

void define_symbol_nodes(
	pybind11::class_<msdm::SymbolNode, msdm::Node> &symbol_class,
	pybind11::class_<msdm::VariableSymbolNode, msdm::SymbolNode> &variable_symbol_class,
	pybind11::module &m);