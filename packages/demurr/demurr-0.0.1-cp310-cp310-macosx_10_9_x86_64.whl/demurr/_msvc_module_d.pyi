"""
Internal module to interface with llvm::ms_demangle
"""
from __future__ import annotations
import pybind11_stubgen.typing_ext
import typing
__all__ = ['ArrayTypeNode', 'CallingConv', 'CharKind', 'ConversionOperatorIdentifierNode', 'CustomTypeNode', 'Demangler', 'DynamicStructorIdentifierNode', 'EncodedStringLiteralNode', 'FuncClass', 'FunctionRefQualifier', 'FunctionSignatureNode', 'FunctionSymbolNode', 'IdentifierNode', 'IntegerLiteralNode', 'IntrinsicFunctionIdentifierNode', 'IntrinsicFunctionKind', 'LiteralOperatorIdentifierNode', 'LocalStaticGuardIdentifierNode', 'LocalStaticGuardVariableNode', 'NamedIdentifierNode', 'Node', 'NodeKind', 'PointerAffinity', 'PointerTypeNode', 'PrimitiveKind', 'PrimitiveTypeNode', 'QualifiedNameNode', 'Qualifiers', 'ReferenceKind', 'RttiBaseClassDescriptorNode', 'SpecialIntrinsicKind', 'SpecialTableSymbolNode', 'StorageClass', 'StructorIdentifierNode', 'SymbolNode', 'TagKind', 'TagTypeNode', 'TemplateParameterReferenceNode', 'ThunkSignatureNode', 'TypeNode', 'VariableSymbolNode', 'VcallThunkIdentifierNode']
class ArrayTypeNode(TypeNode):
    @property
    def dimensions(self) -> list[Node]:
        ...
    @property
    def element_type(self) -> TypeNode:
        ...
class CallingConv:
    """
    Members:
    
      None_
    
      Cdecl
    
      Pascal
    
      Thiscall
    
      Stdcall
    
      Fastcall
    
      Clrcall
    
      Eabi
    
      Vectorcall
    
      Regcall
    
      Swift
    
      SwiftAsync
    """
    Cdecl: typing.ClassVar[CallingConv]  # value = <CallingConv.Cdecl: 1>
    Clrcall: typing.ClassVar[CallingConv]  # value = <CallingConv.Clrcall: 6>
    Eabi: typing.ClassVar[CallingConv]  # value = <CallingConv.Eabi: 7>
    Fastcall: typing.ClassVar[CallingConv]  # value = <CallingConv.Fastcall: 5>
    None_: typing.ClassVar[CallingConv]  # value = <CallingConv.None_: 0>
    Pascal: typing.ClassVar[CallingConv]  # value = <CallingConv.Pascal: 2>
    Regcall: typing.ClassVar[CallingConv]  # value = <CallingConv.Regcall: 9>
    Stdcall: typing.ClassVar[CallingConv]  # value = <CallingConv.Stdcall: 4>
    Swift: typing.ClassVar[CallingConv]  # value = <CallingConv.Swift: 10>
    SwiftAsync: typing.ClassVar[CallingConv]  # value = <CallingConv.SwiftAsync: 11>
    Thiscall: typing.ClassVar[CallingConv]  # value = <CallingConv.Thiscall: 3>
    Vectorcall: typing.ClassVar[CallingConv]  # value = <CallingConv.Vectorcall: 8>
    __members__: typing.ClassVar[dict[str, CallingConv]]  # value = {'None_': <CallingConv.None_: 0>, 'Cdecl': <CallingConv.Cdecl: 1>, 'Pascal': <CallingConv.Pascal: 2>, 'Thiscall': <CallingConv.Thiscall: 3>, 'Stdcall': <CallingConv.Stdcall: 4>, 'Fastcall': <CallingConv.Fastcall: 5>, 'Clrcall': <CallingConv.Clrcall: 6>, 'Eabi': <CallingConv.Eabi: 7>, 'Vectorcall': <CallingConv.Vectorcall: 8>, 'Regcall': <CallingConv.Regcall: 9>, 'Swift': <CallingConv.Swift: 10>, 'SwiftAsync': <CallingConv.SwiftAsync: 11>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CharKind:
    """
    Members:
    
      Char
    
      Char16
    
      Char32
    
      Wchar
    """
    Char: typing.ClassVar[CharKind]  # value = <CharKind.Char: 0>
    Char16: typing.ClassVar[CharKind]  # value = <CharKind.Char16: 1>
    Char32: typing.ClassVar[CharKind]  # value = <CharKind.Char32: 2>
    Wchar: typing.ClassVar[CharKind]  # value = <CharKind.Wchar: 3>
    __members__: typing.ClassVar[dict[str, CharKind]]  # value = {'Char': <CharKind.Char: 0>, 'Char16': <CharKind.Char16: 1>, 'Char32': <CharKind.Char32: 2>, 'Wchar': <CharKind.Wchar: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ConversionOperatorIdentifierNode(IdentifierNode):
    @property
    def target_type(self) -> TypeNode:
        ...
class CustomTypeNode(TypeNode):
    @property
    def identifier(self) -> IdentifierNode:
        ...
class Demangler:
    def __init__(self) -> None:
        ...
    def parse(self, arg0: str) -> SymbolNode:
        ...
    @property
    def error(self) -> bool:
        ...
class DynamicStructorIdentifierNode(IdentifierNode):
    @property
    def is_destructor(self) -> bool:
        ...
    @property
    def name(self) -> QualifiedNameNode:
        ...
    @property
    def variable(self) -> VariableSymbolNode:
        ...
class EncodedStringLiteralNode(SymbolNode):
    @property
    def char_kind(self) -> CharKind:
        ...
    @property
    def decoded_string(self) -> str:
        ...
    @property
    def truncated(self) -> bool:
        ...
class FuncClass:
    """
    Members:
    
      None_
    
      Public
    
      Protected
    
      Private
    
      Global
    
      Static
    
      Virtual
    
      Far
    
      ExternC
    
      NoParameterList
    
      VirtualThisAdjust
    
      VirtualThisAdjustEx
    
      StaticThisAdjust
    """
    ExternC: typing.ClassVar[FuncClass]  # value = <FuncClass.ExternC: 128>
    Far: typing.ClassVar[FuncClass]  # value = <FuncClass.Far: 64>
    Global: typing.ClassVar[FuncClass]  # value = <FuncClass.Global: 8>
    NoParameterList: typing.ClassVar[FuncClass]  # value = <FuncClass.NoParameterList: 256>
    None_: typing.ClassVar[FuncClass]  # value = <FuncClass.None_: 0>
    Private: typing.ClassVar[FuncClass]  # value = <FuncClass.Private: 4>
    Protected: typing.ClassVar[FuncClass]  # value = <FuncClass.Protected: 2>
    Public: typing.ClassVar[FuncClass]  # value = <FuncClass.Public: 1>
    Static: typing.ClassVar[FuncClass]  # value = <FuncClass.Static: 16>
    StaticThisAdjust: typing.ClassVar[FuncClass]  # value = <FuncClass.StaticThisAdjust: 2048>
    Virtual: typing.ClassVar[FuncClass]  # value = <FuncClass.Virtual: 32>
    VirtualThisAdjust: typing.ClassVar[FuncClass]  # value = <FuncClass.VirtualThisAdjust: 512>
    VirtualThisAdjustEx: typing.ClassVar[FuncClass]  # value = <FuncClass.VirtualThisAdjustEx: 1024>
    __members__: typing.ClassVar[dict[str, FuncClass]]  # value = {'None_': <FuncClass.None_: 0>, 'Public': <FuncClass.Public: 1>, 'Protected': <FuncClass.Protected: 2>, 'Private': <FuncClass.Private: 4>, 'Global': <FuncClass.Global: 8>, 'Static': <FuncClass.Static: 16>, 'Virtual': <FuncClass.Virtual: 32>, 'Far': <FuncClass.Far: 64>, 'ExternC': <FuncClass.ExternC: 128>, 'NoParameterList': <FuncClass.NoParameterList: 256>, 'VirtualThisAdjust': <FuncClass.VirtualThisAdjust: 512>, 'VirtualThisAdjustEx': <FuncClass.VirtualThisAdjustEx: 1024>, 'StaticThisAdjust': <FuncClass.StaticThisAdjust: 2048>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FunctionRefQualifier:
    """
    Members:
    
      None_
    
      Reference
    
      RValueReference
    """
    None_: typing.ClassVar[FunctionRefQualifier]  # value = <FunctionRefQualifier.None_: 0>
    RValueReference: typing.ClassVar[FunctionRefQualifier]  # value = <FunctionRefQualifier.RValueReference: 2>
    Reference: typing.ClassVar[FunctionRefQualifier]  # value = <FunctionRefQualifier.Reference: 1>
    __members__: typing.ClassVar[dict[str, FunctionRefQualifier]]  # value = {'None_': <FunctionRefQualifier.None_: 0>, 'Reference': <FunctionRefQualifier.Reference: 1>, 'RValueReference': <FunctionRefQualifier.RValueReference: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class FunctionSignatureNode(TypeNode):
    @property
    def affinity(self) -> PointerAffinity:
        ...
    @property
    def call_convention(self) -> CallingConv:
        ...
    @property
    def function_class(self) -> FuncClass:
        ...
    @property
    def noexcept(self) -> bool:
        ...
    @property
    def params(self) -> list[Node]:
        ...
    @property
    def ref_qualifier(self) -> FunctionRefQualifier:
        ...
    @property
    def return_type(self) -> TypeNode:
        ...
    @property
    def variadic(self) -> bool:
        ...
class FunctionSymbolNode(SymbolNode):
    @property
    def signature(self) -> FunctionSignatureNode:
        ...
class IdentifierNode(Node):
    @property
    def template_params(self) -> list[Node]:
        ...
class IntegerLiteralNode(Node):
    @property
    def negative(self) -> bool:
        ...
    @property
    def value(self) -> int:
        ...
class IntrinsicFunctionIdentifierNode(IdentifierNode):
    @property
    def operator(self) -> IntrinsicFunctionKind:
        ...
class IntrinsicFunctionKind:
    """
    Members:
    
      None_
    
      New
    
      Delete
    
      Assign
    
      RightShift
    
      LeftShift
    
      LogicalNot
    
      Equals
    
      NotEquals
    
      ArraySubscript
    
      Pointer
    
      Dereference
    
      Increment
    
      Decrement
    
      Minus
    
      Plus
    
      BitwiseAnd
    
      MemberPointer
    
      Divide
    
      Modulus
    
      LessThan
    
      LessThanEqual
    
      GreaterThan
    
      GreaterThanEqual
    
      Comma
    
      Parens
    
      BitwiseNot
    
      BitwiseXor
    
      BitwiseOr
    
      LogicalAnd
    
      LogicalOr
    
      TimesEqual
    
      PlusEqual
    
      MinusEqual
    
      DivEqual
    
      ModEqual
    
      RshEqual
    
      LshEqual
    
      BitwiseAndEqual
    
      BitwiseOrEqual
    
      BitwiseXorEqual
    
      VbaseDtor
    
      VecDelDtor
    
      DefaultCtorClosure
    
      ScalarDelDtor
    
      VecCtorIter
    
      VecDtorIter
    
      VecVbaseCtorIter
    
      VdispMap
    
      EHVecCtorIter
    
      EHVecDtorIter
    
      EHVecVbaseCtorIter
    
      CopyCtorClosure
    
      LocalVftableCtorClosure
    
      ArrayNew
    
      ArrayDelete
    
      ManVectorCtorIter
    
      ManVectorDtorIter
    
      EHVectorCopyCtorIter
    
      EHVectorVbaseCopyCtorIter
    
      VectorCopyCtorIter
    
      VectorVbaseCopyCtorIter
    
      ManVectorVbaseCopyCtorIter
    
      CoAwait
    
      Spaceship
    
      MaxIntrinsic
    """
    ArrayDelete: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ArrayDelete: 55>
    ArrayNew: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ArrayNew: 54>
    ArraySubscript: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ArraySubscript: 9>
    Assign: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Assign: 3>
    BitwiseAnd: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseAnd: 16>
    BitwiseAndEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseAndEqual: 38>
    BitwiseNot: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseNot: 26>
    BitwiseOr: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseOr: 28>
    BitwiseOrEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseOrEqual: 39>
    BitwiseXor: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseXor: 27>
    BitwiseXorEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.BitwiseXorEqual: 40>
    CoAwait: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.CoAwait: 63>
    Comma: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Comma: 24>
    CopyCtorClosure: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.CopyCtorClosure: 52>
    Decrement: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Decrement: 13>
    DefaultCtorClosure: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.DefaultCtorClosure: 43>
    Delete: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Delete: 2>
    Dereference: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Dereference: 11>
    DivEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.DivEqual: 34>
    Divide: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Divide: 18>
    EHVecCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.EHVecCtorIter: 49>
    EHVecDtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.EHVecDtorIter: 50>
    EHVecVbaseCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.EHVecVbaseCtorIter: 51>
    EHVectorCopyCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.EHVectorCopyCtorIter: 58>
    EHVectorVbaseCopyCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.EHVectorVbaseCopyCtorIter: 59>
    Equals: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Equals: 7>
    GreaterThan: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.GreaterThan: 22>
    GreaterThanEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.GreaterThanEqual: 23>
    Increment: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Increment: 12>
    LeftShift: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LeftShift: 5>
    LessThan: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LessThan: 20>
    LessThanEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LessThanEqual: 21>
    LocalVftableCtorClosure: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LocalVftableCtorClosure: 53>
    LogicalAnd: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LogicalAnd: 29>
    LogicalNot: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LogicalNot: 6>
    LogicalOr: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LogicalOr: 30>
    LshEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.LshEqual: 37>
    ManVectorCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ManVectorCtorIter: 56>
    ManVectorDtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ManVectorDtorIter: 57>
    ManVectorVbaseCopyCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ManVectorVbaseCopyCtorIter: 62>
    MaxIntrinsic: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.MaxIntrinsic: 65>
    MemberPointer: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.MemberPointer: 17>
    Minus: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Minus: 14>
    MinusEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.MinusEqual: 33>
    ModEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ModEqual: 35>
    Modulus: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Modulus: 19>
    New: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.New: 1>
    None_: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.None_: 0>
    NotEquals: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.NotEquals: 8>
    Parens: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Parens: 25>
    Plus: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Plus: 15>
    PlusEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.PlusEqual: 32>
    Pointer: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Pointer: 10>
    RightShift: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.RightShift: 4>
    RshEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.RshEqual: 36>
    ScalarDelDtor: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.ScalarDelDtor: 44>
    Spaceship: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.Spaceship: 64>
    TimesEqual: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.TimesEqual: 31>
    VbaseDtor: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VbaseDtor: 41>
    VdispMap: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VdispMap: 48>
    VecCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VecCtorIter: 45>
    VecDelDtor: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VecDelDtor: 42>
    VecDtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VecDtorIter: 46>
    VecVbaseCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VecVbaseCtorIter: 47>
    VectorCopyCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VectorCopyCtorIter: 60>
    VectorVbaseCopyCtorIter: typing.ClassVar[IntrinsicFunctionKind]  # value = <IntrinsicFunctionKind.VectorVbaseCopyCtorIter: 61>
    __members__: typing.ClassVar[dict[str, IntrinsicFunctionKind]]  # value = {'None_': <IntrinsicFunctionKind.None_: 0>, 'New': <IntrinsicFunctionKind.New: 1>, 'Delete': <IntrinsicFunctionKind.Delete: 2>, 'Assign': <IntrinsicFunctionKind.Assign: 3>, 'RightShift': <IntrinsicFunctionKind.RightShift: 4>, 'LeftShift': <IntrinsicFunctionKind.LeftShift: 5>, 'LogicalNot': <IntrinsicFunctionKind.LogicalNot: 6>, 'Equals': <IntrinsicFunctionKind.Equals: 7>, 'NotEquals': <IntrinsicFunctionKind.NotEquals: 8>, 'ArraySubscript': <IntrinsicFunctionKind.ArraySubscript: 9>, 'Pointer': <IntrinsicFunctionKind.Pointer: 10>, 'Dereference': <IntrinsicFunctionKind.Dereference: 11>, 'Increment': <IntrinsicFunctionKind.Increment: 12>, 'Decrement': <IntrinsicFunctionKind.Decrement: 13>, 'Minus': <IntrinsicFunctionKind.Minus: 14>, 'Plus': <IntrinsicFunctionKind.Plus: 15>, 'BitwiseAnd': <IntrinsicFunctionKind.BitwiseAnd: 16>, 'MemberPointer': <IntrinsicFunctionKind.MemberPointer: 17>, 'Divide': <IntrinsicFunctionKind.Divide: 18>, 'Modulus': <IntrinsicFunctionKind.Modulus: 19>, 'LessThan': <IntrinsicFunctionKind.LessThan: 20>, 'LessThanEqual': <IntrinsicFunctionKind.LessThanEqual: 21>, 'GreaterThan': <IntrinsicFunctionKind.GreaterThan: 22>, 'GreaterThanEqual': <IntrinsicFunctionKind.GreaterThanEqual: 23>, 'Comma': <IntrinsicFunctionKind.Comma: 24>, 'Parens': <IntrinsicFunctionKind.Parens: 25>, 'BitwiseNot': <IntrinsicFunctionKind.BitwiseNot: 26>, 'BitwiseXor': <IntrinsicFunctionKind.BitwiseXor: 27>, 'BitwiseOr': <IntrinsicFunctionKind.BitwiseOr: 28>, 'LogicalAnd': <IntrinsicFunctionKind.LogicalAnd: 29>, 'LogicalOr': <IntrinsicFunctionKind.LogicalOr: 30>, 'TimesEqual': <IntrinsicFunctionKind.TimesEqual: 31>, 'PlusEqual': <IntrinsicFunctionKind.PlusEqual: 32>, 'MinusEqual': <IntrinsicFunctionKind.MinusEqual: 33>, 'DivEqual': <IntrinsicFunctionKind.DivEqual: 34>, 'ModEqual': <IntrinsicFunctionKind.ModEqual: 35>, 'RshEqual': <IntrinsicFunctionKind.RshEqual: 36>, 'LshEqual': <IntrinsicFunctionKind.LshEqual: 37>, 'BitwiseAndEqual': <IntrinsicFunctionKind.BitwiseAndEqual: 38>, 'BitwiseOrEqual': <IntrinsicFunctionKind.BitwiseOrEqual: 39>, 'BitwiseXorEqual': <IntrinsicFunctionKind.BitwiseXorEqual: 40>, 'VbaseDtor': <IntrinsicFunctionKind.VbaseDtor: 41>, 'VecDelDtor': <IntrinsicFunctionKind.VecDelDtor: 42>, 'DefaultCtorClosure': <IntrinsicFunctionKind.DefaultCtorClosure: 43>, 'ScalarDelDtor': <IntrinsicFunctionKind.ScalarDelDtor: 44>, 'VecCtorIter': <IntrinsicFunctionKind.VecCtorIter: 45>, 'VecDtorIter': <IntrinsicFunctionKind.VecDtorIter: 46>, 'VecVbaseCtorIter': <IntrinsicFunctionKind.VecVbaseCtorIter: 47>, 'VdispMap': <IntrinsicFunctionKind.VdispMap: 48>, 'EHVecCtorIter': <IntrinsicFunctionKind.EHVecCtorIter: 49>, 'EHVecDtorIter': <IntrinsicFunctionKind.EHVecDtorIter: 50>, 'EHVecVbaseCtorIter': <IntrinsicFunctionKind.EHVecVbaseCtorIter: 51>, 'CopyCtorClosure': <IntrinsicFunctionKind.CopyCtorClosure: 52>, 'LocalVftableCtorClosure': <IntrinsicFunctionKind.LocalVftableCtorClosure: 53>, 'ArrayNew': <IntrinsicFunctionKind.ArrayNew: 54>, 'ArrayDelete': <IntrinsicFunctionKind.ArrayDelete: 55>, 'ManVectorCtorIter': <IntrinsicFunctionKind.ManVectorCtorIter: 56>, 'ManVectorDtorIter': <IntrinsicFunctionKind.ManVectorDtorIter: 57>, 'EHVectorCopyCtorIter': <IntrinsicFunctionKind.EHVectorCopyCtorIter: 58>, 'EHVectorVbaseCopyCtorIter': <IntrinsicFunctionKind.EHVectorVbaseCopyCtorIter: 59>, 'VectorCopyCtorIter': <IntrinsicFunctionKind.VectorCopyCtorIter: 60>, 'VectorVbaseCopyCtorIter': <IntrinsicFunctionKind.VectorVbaseCopyCtorIter: 61>, 'ManVectorVbaseCopyCtorIter': <IntrinsicFunctionKind.ManVectorVbaseCopyCtorIter: 62>, 'CoAwait': <IntrinsicFunctionKind.CoAwait: 63>, 'Spaceship': <IntrinsicFunctionKind.Spaceship: 64>, 'MaxIntrinsic': <IntrinsicFunctionKind.MaxIntrinsic: 65>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LiteralOperatorIdentifierNode(IdentifierNode):
    @property
    def name(self) -> str:
        ...
class LocalStaticGuardIdentifierNode(IdentifierNode):
    @property
    def is_thread(self) -> bool:
        ...
    @property
    def scope_index(self) -> int:
        ...
class LocalStaticGuardVariableNode(SymbolNode):
    @property
    def visible(self) -> bool:
        ...
class NamedIdentifierNode(IdentifierNode):
    @property
    def name(self) -> str:
        ...
class Node:
    def __str__(self) -> str:
        ...
    @property
    def kind(self) -> NodeKind:
        ...
class NodeKind:
    """
    Members:
    
      Unknown
    
      Md5Symbol
    
      PrimitiveType
    
      FunctionSignature
    
      Identifier
    
      NamedIdentifier
    
      VcallThunkIdentifier
    
      LocalStaticGuardIdentifier
    
      IntrinsicFunctionIdentifier
    
      ConversionOperatorIdentifier
    
      DynamicStructorIdentifier
    
      StructorIdentifier
    
      LiteralOperatorIdentifier
    
      ThunkSignature
    
      PointerType
    
      TagType
    
      ArrayType
    
      Custom
    
      IntrinsicType
    
      NodeArray
    
      QualifiedName
    
      TemplateParameterReference
    
      EncodedStringLiteral
    
      IntegerLiteral
    
      RttiBaseClassDescriptor
    
      LocalStaticGuardVariable
    
      FunctionSymbol
    
      VariableSymbol
    
      SpecialTableSymbol
    """
    ArrayType: typing.ClassVar[NodeKind]  # value = <NodeKind.ArrayType: 16>
    ConversionOperatorIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.ConversionOperatorIdentifier: 9>
    Custom: typing.ClassVar[NodeKind]  # value = <NodeKind.Custom: 17>
    DynamicStructorIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.DynamicStructorIdentifier: 10>
    EncodedStringLiteral: typing.ClassVar[NodeKind]  # value = <NodeKind.EncodedStringLiteral: 22>
    FunctionSignature: typing.ClassVar[NodeKind]  # value = <NodeKind.FunctionSignature: 3>
    FunctionSymbol: typing.ClassVar[NodeKind]  # value = <NodeKind.FunctionSymbol: 26>
    Identifier: typing.ClassVar[NodeKind]  # value = <NodeKind.Identifier: 4>
    IntegerLiteral: typing.ClassVar[NodeKind]  # value = <NodeKind.IntegerLiteral: 23>
    IntrinsicFunctionIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.IntrinsicFunctionIdentifier: 8>
    IntrinsicType: typing.ClassVar[NodeKind]  # value = <NodeKind.IntrinsicType: 18>
    LiteralOperatorIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.LiteralOperatorIdentifier: 12>
    LocalStaticGuardIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.LocalStaticGuardIdentifier: 7>
    LocalStaticGuardVariable: typing.ClassVar[NodeKind]  # value = <NodeKind.LocalStaticGuardVariable: 25>
    Md5Symbol: typing.ClassVar[NodeKind]  # value = <NodeKind.Md5Symbol: 1>
    NamedIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.NamedIdentifier: 5>
    NodeArray: typing.ClassVar[NodeKind]  # value = <NodeKind.NodeArray: 19>
    PointerType: typing.ClassVar[NodeKind]  # value = <NodeKind.PointerType: 14>
    PrimitiveType: typing.ClassVar[NodeKind]  # value = <NodeKind.PrimitiveType: 2>
    QualifiedName: typing.ClassVar[NodeKind]  # value = <NodeKind.QualifiedName: 20>
    RttiBaseClassDescriptor: typing.ClassVar[NodeKind]  # value = <NodeKind.RttiBaseClassDescriptor: 24>
    SpecialTableSymbol: typing.ClassVar[NodeKind]  # value = <NodeKind.SpecialTableSymbol: 28>
    StructorIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.StructorIdentifier: 11>
    TagType: typing.ClassVar[NodeKind]  # value = <NodeKind.TagType: 15>
    TemplateParameterReference: typing.ClassVar[NodeKind]  # value = <NodeKind.TemplateParameterReference: 21>
    ThunkSignature: typing.ClassVar[NodeKind]  # value = <NodeKind.ThunkSignature: 13>
    Unknown: typing.ClassVar[NodeKind]  # value = <NodeKind.Unknown: 0>
    VariableSymbol: typing.ClassVar[NodeKind]  # value = <NodeKind.VariableSymbol: 27>
    VcallThunkIdentifier: typing.ClassVar[NodeKind]  # value = <NodeKind.VcallThunkIdentifier: 6>
    __members__: typing.ClassVar[dict[str, NodeKind]]  # value = {'Unknown': <NodeKind.Unknown: 0>, 'Md5Symbol': <NodeKind.Md5Symbol: 1>, 'PrimitiveType': <NodeKind.PrimitiveType: 2>, 'FunctionSignature': <NodeKind.FunctionSignature: 3>, 'Identifier': <NodeKind.Identifier: 4>, 'NamedIdentifier': <NodeKind.NamedIdentifier: 5>, 'VcallThunkIdentifier': <NodeKind.VcallThunkIdentifier: 6>, 'LocalStaticGuardIdentifier': <NodeKind.LocalStaticGuardIdentifier: 7>, 'IntrinsicFunctionIdentifier': <NodeKind.IntrinsicFunctionIdentifier: 8>, 'ConversionOperatorIdentifier': <NodeKind.ConversionOperatorIdentifier: 9>, 'DynamicStructorIdentifier': <NodeKind.DynamicStructorIdentifier: 10>, 'StructorIdentifier': <NodeKind.StructorIdentifier: 11>, 'LiteralOperatorIdentifier': <NodeKind.LiteralOperatorIdentifier: 12>, 'ThunkSignature': <NodeKind.ThunkSignature: 13>, 'PointerType': <NodeKind.PointerType: 14>, 'TagType': <NodeKind.TagType: 15>, 'ArrayType': <NodeKind.ArrayType: 16>, 'Custom': <NodeKind.Custom: 17>, 'IntrinsicType': <NodeKind.IntrinsicType: 18>, 'NodeArray': <NodeKind.NodeArray: 19>, 'QualifiedName': <NodeKind.QualifiedName: 20>, 'TemplateParameterReference': <NodeKind.TemplateParameterReference: 21>, 'EncodedStringLiteral': <NodeKind.EncodedStringLiteral: 22>, 'IntegerLiteral': <NodeKind.IntegerLiteral: 23>, 'RttiBaseClassDescriptor': <NodeKind.RttiBaseClassDescriptor: 24>, 'LocalStaticGuardVariable': <NodeKind.LocalStaticGuardVariable: 25>, 'FunctionSymbol': <NodeKind.FunctionSymbol: 26>, 'VariableSymbol': <NodeKind.VariableSymbol: 27>, 'SpecialTableSymbol': <NodeKind.SpecialTableSymbol: 28>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PointerAffinity:
    """
    Members:
    
      None_
    
      Pointer
    
      Reference
    
      RValueReference
    """
    None_: typing.ClassVar[PointerAffinity]  # value = <PointerAffinity.None_: 0>
    Pointer: typing.ClassVar[PointerAffinity]  # value = <PointerAffinity.Pointer: 1>
    RValueReference: typing.ClassVar[PointerAffinity]  # value = <PointerAffinity.RValueReference: 3>
    Reference: typing.ClassVar[PointerAffinity]  # value = <PointerAffinity.Reference: 2>
    __members__: typing.ClassVar[dict[str, PointerAffinity]]  # value = {'None_': <PointerAffinity.None_: 0>, 'Pointer': <PointerAffinity.Pointer: 1>, 'Reference': <PointerAffinity.Reference: 2>, 'RValueReference': <PointerAffinity.RValueReference: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PointerTypeNode(TypeNode):
    @property
    def affinity(self) -> PointerAffinity:
        ...
    @property
    def class_parent(self) -> QualifiedNameNode:
        ...
    @property
    def pointee(self) -> TypeNode:
        ...
class PrimitiveKind:
    """
    Members:
    
      Void
    
      Bool
    
      Char
    
      Schar
    
      Uchar
    
      Char8
    
      Char16
    
      Char32
    
      Short
    
      Ushort
    
      Int
    
      Uint
    
      Long
    
      Ulong
    
      Int64
    
      Uint64
    
      Wchar
    
      Float
    
      Double
    
      Ldouble
    
      Nullptr
    """
    Bool: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Bool: 1>
    Char: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Char: 2>
    Char16: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Char16: 6>
    Char32: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Char32: 7>
    Char8: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Char8: 5>
    Double: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Double: 18>
    Float: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Float: 17>
    Int: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Int: 10>
    Int64: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Int64: 14>
    Ldouble: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Ldouble: 19>
    Long: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Long: 12>
    Nullptr: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Nullptr: 20>
    Schar: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Schar: 3>
    Short: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Short: 8>
    Uchar: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Uchar: 4>
    Uint: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Uint: 11>
    Uint64: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Uint64: 15>
    Ulong: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Ulong: 13>
    Ushort: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Ushort: 9>
    Void: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Void: 0>
    Wchar: typing.ClassVar[PrimitiveKind]  # value = <PrimitiveKind.Wchar: 16>
    __members__: typing.ClassVar[dict[str, PrimitiveKind]]  # value = {'Void': <PrimitiveKind.Void: 0>, 'Bool': <PrimitiveKind.Bool: 1>, 'Char': <PrimitiveKind.Char: 2>, 'Schar': <PrimitiveKind.Schar: 3>, 'Uchar': <PrimitiveKind.Uchar: 4>, 'Char8': <PrimitiveKind.Char8: 5>, 'Char16': <PrimitiveKind.Char16: 6>, 'Char32': <PrimitiveKind.Char32: 7>, 'Short': <PrimitiveKind.Short: 8>, 'Ushort': <PrimitiveKind.Ushort: 9>, 'Int': <PrimitiveKind.Int: 10>, 'Uint': <PrimitiveKind.Uint: 11>, 'Long': <PrimitiveKind.Long: 12>, 'Ulong': <PrimitiveKind.Ulong: 13>, 'Int64': <PrimitiveKind.Int64: 14>, 'Uint64': <PrimitiveKind.Uint64: 15>, 'Wchar': <PrimitiveKind.Wchar: 16>, 'Float': <PrimitiveKind.Float: 17>, 'Double': <PrimitiveKind.Double: 18>, 'Ldouble': <PrimitiveKind.Ldouble: 19>, 'Nullptr': <PrimitiveKind.Nullptr: 20>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PrimitiveTypeNode(TypeNode):
    @property
    def primitive_kind(self) -> PrimitiveKind:
        ...
class QualifiedNameNode(Node):
    @property
    def components(self) -> list[Node]:
        ...
class Qualifiers:
    """
    Members:
    
      None_
    
      Const
    
      Volatile
    
      Far
    
      Huge
    
      Unaligned
    
      Restrict
    
      Pointer64
    """
    Const: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Const: 1>
    Far: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Far: 4>
    Huge: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Huge: 8>
    None_: typing.ClassVar[Qualifiers]  # value = <Qualifiers.None_: 0>
    Pointer64: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Pointer64: 64>
    Restrict: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Restrict: 32>
    Unaligned: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Unaligned: 16>
    Volatile: typing.ClassVar[Qualifiers]  # value = <Qualifiers.Volatile: 2>
    __members__: typing.ClassVar[dict[str, Qualifiers]]  # value = {'None_': <Qualifiers.None_: 0>, 'Const': <Qualifiers.Const: 1>, 'Volatile': <Qualifiers.Volatile: 2>, 'Far': <Qualifiers.Far: 4>, 'Huge': <Qualifiers.Huge: 8>, 'Unaligned': <Qualifiers.Unaligned: 16>, 'Restrict': <Qualifiers.Restrict: 32>, 'Pointer64': <Qualifiers.Pointer64: 64>}
    def __and__(self, other: typing.Any) -> typing.Any:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __ge__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __gt__(self, other: typing.Any) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> typing.Any:
        ...
    def __le__(self, other: typing.Any) -> bool:
        ...
    def __lt__(self, other: typing.Any) -> bool:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, other: typing.Any) -> typing.Any:
        ...
    def __rand__(self, other: typing.Any) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def __ror__(self, other: typing.Any) -> typing.Any:
        ...
    def __rxor__(self, other: typing.Any) -> typing.Any:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, other: typing.Any) -> typing.Any:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ReferenceKind:
    """
    Members:
    
      None_
    
      LValueRef
    
      RValueRef
    """
    LValueRef: typing.ClassVar[ReferenceKind]  # value = <ReferenceKind.LValueRef: 1>
    None_: typing.ClassVar[ReferenceKind]  # value = <ReferenceKind.None_: 0>
    RValueRef: typing.ClassVar[ReferenceKind]  # value = <ReferenceKind.RValueRef: 2>
    __members__: typing.ClassVar[dict[str, ReferenceKind]]  # value = {'None_': <ReferenceKind.None_: 0>, 'LValueRef': <ReferenceKind.LValueRef: 1>, 'RValueRef': <ReferenceKind.RValueRef: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RttiBaseClassDescriptorNode(IdentifierNode):
    @property
    def flags(self) -> int:
        ...
    @property
    def nv_offset(self) -> int:
        ...
    @property
    def vbptr_offset(self) -> int:
        ...
    @property
    def vbtable_offset(self) -> int:
        ...
class SpecialIntrinsicKind:
    """
    Members:
    
      None_
    
      Vftable
    
      Vbtable
    
      Typeof
    
      VcallThunk
    
      LocalStaticGuard
    
      StringLiteralSymbol
    
      UdtReturning
    
      Unknown
    
      DynamicInitializer
    
      DynamicAtexitDestructor
    
      RttiTypeDescriptor
    
      RttiBaseClassDescriptor
    
      RttiBaseClassArray
    
      RttiClassHierarchyDescriptor
    
      RttiCompleteObjLocator
    
      LocalVftable
    
      LocalStaticThreadGuard
    """
    DynamicAtexitDestructor: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.DynamicAtexitDestructor: 10>
    DynamicInitializer: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.DynamicInitializer: 9>
    LocalStaticGuard: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.LocalStaticGuard: 5>
    LocalStaticThreadGuard: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.LocalStaticThreadGuard: 17>
    LocalVftable: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.LocalVftable: 16>
    None_: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.None_: 0>
    RttiBaseClassArray: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.RttiBaseClassArray: 13>
    RttiBaseClassDescriptor: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.RttiBaseClassDescriptor: 12>
    RttiClassHierarchyDescriptor: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.RttiClassHierarchyDescriptor: 14>
    RttiCompleteObjLocator: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.RttiCompleteObjLocator: 15>
    RttiTypeDescriptor: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.RttiTypeDescriptor: 11>
    StringLiteralSymbol: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.StringLiteralSymbol: 6>
    Typeof: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.Typeof: 3>
    UdtReturning: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.UdtReturning: 7>
    Unknown: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.Unknown: 8>
    Vbtable: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.Vbtable: 2>
    VcallThunk: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.VcallThunk: 4>
    Vftable: typing.ClassVar[SpecialIntrinsicKind]  # value = <SpecialIntrinsicKind.Vftable: 1>
    __members__: typing.ClassVar[dict[str, SpecialIntrinsicKind]]  # value = {'None_': <SpecialIntrinsicKind.None_: 0>, 'Vftable': <SpecialIntrinsicKind.Vftable: 1>, 'Vbtable': <SpecialIntrinsicKind.Vbtable: 2>, 'Typeof': <SpecialIntrinsicKind.Typeof: 3>, 'VcallThunk': <SpecialIntrinsicKind.VcallThunk: 4>, 'LocalStaticGuard': <SpecialIntrinsicKind.LocalStaticGuard: 5>, 'StringLiteralSymbol': <SpecialIntrinsicKind.StringLiteralSymbol: 6>, 'UdtReturning': <SpecialIntrinsicKind.UdtReturning: 7>, 'Unknown': <SpecialIntrinsicKind.Unknown: 8>, 'DynamicInitializer': <SpecialIntrinsicKind.DynamicInitializer: 9>, 'DynamicAtexitDestructor': <SpecialIntrinsicKind.DynamicAtexitDestructor: 10>, 'RttiTypeDescriptor': <SpecialIntrinsicKind.RttiTypeDescriptor: 11>, 'RttiBaseClassDescriptor': <SpecialIntrinsicKind.RttiBaseClassDescriptor: 12>, 'RttiBaseClassArray': <SpecialIntrinsicKind.RttiBaseClassArray: 13>, 'RttiClassHierarchyDescriptor': <SpecialIntrinsicKind.RttiClassHierarchyDescriptor: 14>, 'RttiCompleteObjLocator': <SpecialIntrinsicKind.RttiCompleteObjLocator: 15>, 'LocalVftable': <SpecialIntrinsicKind.LocalVftable: 16>, 'LocalStaticThreadGuard': <SpecialIntrinsicKind.LocalStaticThreadGuard: 17>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SpecialTableSymbolNode(SymbolNode):
    @property
    def qualifiers(self) -> Qualifiers:
        ...
    @property
    def target_name(self) -> QualifiedNameNode:
        ...
class StorageClass:
    """
    Members:
    
      None_
    
      PrivateStatic
    
      ProtectedStatic
    
      PublicStatic
    
      Global
    
      FunctionLocalStatic
    """
    FunctionLocalStatic: typing.ClassVar[StorageClass]  # value = <StorageClass.FunctionLocalStatic: 5>
    Global: typing.ClassVar[StorageClass]  # value = <StorageClass.Global: 4>
    None_: typing.ClassVar[StorageClass]  # value = <StorageClass.None_: 0>
    PrivateStatic: typing.ClassVar[StorageClass]  # value = <StorageClass.PrivateStatic: 1>
    ProtectedStatic: typing.ClassVar[StorageClass]  # value = <StorageClass.ProtectedStatic: 2>
    PublicStatic: typing.ClassVar[StorageClass]  # value = <StorageClass.PublicStatic: 3>
    __members__: typing.ClassVar[dict[str, StorageClass]]  # value = {'None_': <StorageClass.None_: 0>, 'PrivateStatic': <StorageClass.PrivateStatic: 1>, 'ProtectedStatic': <StorageClass.ProtectedStatic: 2>, 'PublicStatic': <StorageClass.PublicStatic: 3>, 'Global': <StorageClass.Global: 4>, 'FunctionLocalStatic': <StorageClass.FunctionLocalStatic: 5>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StructorIdentifierNode(IdentifierNode):
    @property
    def class_(self) -> IdentifierNode:
        ...
    @property
    def is_destructor(self) -> bool:
        ...
class SymbolNode(Node):
    @property
    def name(self) -> QualifiedNameNode:
        ...
class TagKind:
    """
    Members:
    
      Class
    
      Struct
    
      Union
    
      Enum
    """
    Class: typing.ClassVar[TagKind]  # value = <TagKind.Class: 0>
    Enum: typing.ClassVar[TagKind]  # value = <TagKind.Enum: 3>
    Struct: typing.ClassVar[TagKind]  # value = <TagKind.Struct: 1>
    Union: typing.ClassVar[TagKind]  # value = <TagKind.Union: 2>
    __members__: typing.ClassVar[dict[str, TagKind]]  # value = {'Class': <TagKind.Class: 0>, 'Struct': <TagKind.Struct: 1>, 'Union': <TagKind.Union: 2>, 'Enum': <TagKind.Enum: 3>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TagTypeNode(TypeNode):
    @property
    def qualified_name(self) -> QualifiedNameNode:
        ...
    @property
    def tag(self) -> TagKind:
        ...
class TemplateParameterReferenceNode(Node):
    @property
    def ThunkOffsets(self) -> typing.Annotated[list[int], pybind11_stubgen.typing_ext.FixedSize(3)]:
        ...
    @property
    def affinity(self) -> PointerAffinity:
        ...
    @property
    def is_member_pointer(self) -> bool:
        ...
    @property
    def symbol(self) -> SymbolNode:
        ...
    @property
    def thunk_offset_count(self) -> int:
        ...
class ThunkSignatureNode(FunctionSignatureNode):
    class ThisAdjustor:
        @property
        def static_offset(self) -> int:
            ...
        @property
        def vboffset_offset(self) -> int:
            ...
        @property
        def vbptr_offset(self) -> int:
            ...
        @property
        def vtordisp_offset(self) -> int:
            ...
    @property
    def this_adjust(self) -> ThunkSignatureNode.ThisAdjustor:
        ...
class TypeNode(Node):
    @property
    def qualifiers(self) -> Qualifiers:
        ...
class VariableSymbolNode(SymbolNode):
    @property
    def storage_class(self) -> StorageClass:
        ...
    @property
    def type(self) -> TypeNode:
        ...
class VcallThunkIdentifierNode(IdentifierNode):
    @property
    def offset_in_vtable(self) -> int:
        ...
__version__: str = '"0.0.1"'
