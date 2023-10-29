#pragma once

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>

namespace msdm = llvm::ms_demangle;

void define_identifier_nodes(pybind11::class_<msdm::IdentifierNode, msdm::Node> &identifier_class, pybind11::module &m);