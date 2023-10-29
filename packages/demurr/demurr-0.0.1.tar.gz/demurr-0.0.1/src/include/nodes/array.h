#pragma once

#include <pybind11/pybind11.h>
#include <llvm/Demangle/MicrosoftDemangleNodes.h>
#include <llvm/Demangle/MicrosoftDemangle.h>

namespace msdm = llvm::ms_demangle;

namespace pybind11 {
namespace detail {
    template <> struct type_caster<msdm::NodeArrayNode> {
		using value_conv = make_caster<msdm::Node*>;
	public:
        static handle cast(msdm::NodeArrayNode src, return_value_policy, handle parent) {
            list l(src.Count);
            for (size_t i = 0; i < src.Count; i++) {
                auto value_ = reinterpret_steal<object>(
                    value_conv::cast(src.Nodes[i], return_value_policy::reference, parent));
                if (!value_)
                    return handle();
                PyList_SET_ITEM(l.ptr(), i, value_.release().ptr()); // steals a reference
            }
            return l.release();
        }

        PYBIND11_TYPE_CASTER(msdm::NodeArrayNode, const_name("list[") + value_conv::name + const_name("]"));
	};
}}