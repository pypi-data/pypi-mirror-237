#include "nodes/identifiers.h"
#include "nodes/array.h"

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>
#include <llvm/Demangle/MicrosoftDemangle.h>

namespace py = pybind11;
namespace msdm = llvm::ms_demangle;

void define_identifier_nodes(py::class_<msdm::IdentifierNode, msdm::Node> &identifier_class, py::module &m) {
	identifier_class
        .def_readonly("template_params", &msdm::IdentifierNode::TemplateParams);

    py::class_<msdm::VcallThunkIdentifierNode, msdm::IdentifierNode>(m, "VcallThunkIdentifierNode")
        .def_readonly("offset_in_vtable", &msdm::VcallThunkIdentifierNode::OffsetInVTable);
    
    py::class_<msdm::DynamicStructorIdentifierNode, msdm::IdentifierNode>(m, "DynamicStructorIdentifierNode")
        .def_readonly("variable", &msdm::DynamicStructorIdentifierNode::Variable)
        .def_readonly("name", &msdm::DynamicStructorIdentifierNode::Name)
        .def_readonly("is_destructor", &msdm::DynamicStructorIdentifierNode::IsDestructor);

    py::class_<msdm::NamedIdentifierNode, msdm::IdentifierNode>(m, "NamedIdentifierNode")
        .def_readonly("name", &msdm::NamedIdentifierNode::Name);

    py::class_<msdm::IntrinsicFunctionIdentifierNode, msdm::IdentifierNode>(m, "IntrinsicFunctionIdentifierNode")
        .def_readonly("operator", &msdm::IntrinsicFunctionIdentifierNode::Operator);

    py::class_<msdm::LiteralOperatorIdentifierNode, msdm::IdentifierNode>(m, "LiteralOperatorIdentifierNode")
        .def_readonly("name", &msdm::LiteralOperatorIdentifierNode::Name);
    
    py::class_<msdm::LocalStaticGuardIdentifierNode, msdm::IdentifierNode>(m, "LocalStaticGuardIdentifierNode")
        .def_readonly("is_thread", &msdm::LocalStaticGuardIdentifierNode::IsThread)
        .def_readonly("scope_index", &msdm::LocalStaticGuardIdentifierNode::ScopeIndex);
    
    py::class_<msdm::ConversionOperatorIdentifierNode, msdm::IdentifierNode>(m, "ConversionOperatorIdentifierNode")
        .def_readonly("target_type", &msdm::ConversionOperatorIdentifierNode::TargetType);
    
    py::class_<msdm::StructorIdentifierNode, msdm::IdentifierNode>(m, "StructorIdentifierNode")
        .def_readonly("class_", &msdm::StructorIdentifierNode::Class)
        .def_readonly("is_destructor", &msdm::StructorIdentifierNode::IsDestructor);

    py::class_<msdm::RttiBaseClassDescriptorNode, msdm::IdentifierNode>(m, "RttiBaseClassDescriptorNode")
        .def_readonly("nv_offset", &msdm::RttiBaseClassDescriptorNode::NVOffset)
        .def_readonly("vbptr_offset", &msdm::RttiBaseClassDescriptorNode::VBPtrOffset)
        .def_readonly("vbtable_offset", &msdm::RttiBaseClassDescriptorNode::VBTableOffset)
        .def_readonly("flags", &msdm::RttiBaseClassDescriptorNode::Flags);
} 