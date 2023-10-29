#include "nodes/types.h"
#include "nodes/array.h"

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>
#include <llvm/Demangle/MicrosoftDemangle.h>

namespace py = pybind11;

void define_type_nodes(py::module &m) {
    py::class_<msdm::TypeNode, msdm::Node>(m, "TypeNode")
        .def_readonly("qualifiers", &msdm::TypeNode::Quals);

    py::class_<msdm::PrimitiveTypeNode, msdm::TypeNode>(m, "PrimitiveTypeNode")
        .def_readonly("primitive_kind", &msdm::PrimitiveTypeNode::PrimKind);

    py::class_<msdm::FunctionSignatureNode, msdm::TypeNode>(m, "FunctionSignatureNode")
        .def_readonly("affinity", &msdm::FunctionSignatureNode::Affinity)
        .def_readonly("call_convention", &msdm::FunctionSignatureNode::CallConvention)
        .def_readonly("function_class", &msdm::FunctionSignatureNode::FunctionClass)
        .def_readonly("ref_qualifier", &msdm::FunctionSignatureNode::RefQualifier)
        .def_readonly("return_type", &msdm::FunctionSignatureNode::ReturnType)
        .def_readonly("variadic", &msdm::FunctionSignatureNode::IsVariadic)
        .def_readonly("params", &msdm::FunctionSignatureNode::Params)
        .def_readonly("noexcept", &msdm::FunctionSignatureNode::IsNoexcept);

    auto thunk_signature_node_class = py::class_<msdm::ThunkSignatureNode, msdm::FunctionSignatureNode>(m, "ThunkSignatureNode");
    
    py::class_<msdm::ThunkSignatureNode::ThisAdjustor>(thunk_signature_node_class, "ThisAdjustor")
        .def_readonly("static_offset", &msdm::ThunkSignatureNode::ThisAdjustor::StaticOffset)
        .def_readonly("vbptr_offset", &msdm::ThunkSignatureNode::ThisAdjustor::VBPtrOffset)
        .def_readonly("vboffset_offset", &msdm::ThunkSignatureNode::ThisAdjustor::VBOffsetOffset)
        .def_readonly("vtordisp_offset", &msdm::ThunkSignatureNode::ThisAdjustor::VtordispOffset);

    thunk_signature_node_class
        .def_readonly("this_adjust", &msdm::ThunkSignatureNode::ThisAdjust);

    py::class_<msdm::PointerTypeNode, msdm::TypeNode>(m, "PointerTypeNode")
        .def_readonly("affinity", &msdm::PointerTypeNode::Affinity)
        .def_readonly("class_parent", &msdm::PointerTypeNode::ClassParent)
        .def_readonly("pointee", &msdm::PointerTypeNode::Pointee);

    py::class_<msdm::TagTypeNode, msdm::TypeNode>(m, "TagTypeNode")
        .def_readonly("qualified_name", &msdm::TagTypeNode::QualifiedName)
        .def_readonly("tag", &msdm::TagTypeNode::Tag);

    py::class_<msdm::ArrayTypeNode, msdm::TypeNode>(m, "ArrayTypeNode")
        .def_readonly("dimensions", &msdm::ArrayTypeNode::Dimensions)
        .def_readonly("element_type", &msdm::ArrayTypeNode::ElementType);

    py::class_<msdm::CustomTypeNode, msdm::TypeNode>(m, "CustomTypeNode")
        .def_readonly("identifier", &msdm::CustomTypeNode::Identifier);
}