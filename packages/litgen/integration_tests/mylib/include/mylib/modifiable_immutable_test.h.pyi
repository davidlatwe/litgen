# ============================================================================
# This file was autogenerated
# It is presented side to side with its source: modifiable_immutable_test.h
#    (see integration_tests/bindings/lg_mylib/__init__pyi which contains the full
#     stub code, including this code)
# ============================================================================

# type: ignore
import sys
from typing import Literal, List, Any, Optional, Tuple, Dict
import numpy as np
from enum import Enum
import numpy

# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:BoxedTypes>    ####################
class BoxedBool:
    value: bool
    def __init__(self, v: bool = False) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedString:
    value: str
    def __init__(self, v: str = "") -> None:
        pass
    def __repr__(self) -> str:
        pass
####################    </generated_from:BoxedTypes>    ####################


####################    <generated_from:modifiable_immutable_test.h>    ####################


#
# Modifiable immutable python types test
#

# litgen adapts functions params that use modifiable pointer or reference to a type
# that is immutable in python.
# On the C++ side, these params are modifiable by the function.
# We need to box them into a Boxed type to ensure that any modification made by C++
# is visible when going back to Python.
#
# Note: immutable data types in python are
#   - Int, Float, String (correctly handled by litgen)
#   - Complex, Bytes (not handled)
#   - Tuple (not handled)


#///////////////////////////////////////////////////////////////////////////////////////////
# Test Part 1: in the functions below, the value parameters will be "Boxed"
#
# This is caused by the following options during generation:
#     options.fn_params_replace_modifiable_immutable_by_boxed__regex = code_utils.join_string_by_pipe_char([
#         r"^Toggle",
#         r"^Modify",
#      ])
#/////////////////////////////////////////////////////////////////////////////////////////


def toggle_bool_pointer(v: BoxedBool) -> None:
    """ Test with pointer:
     Will be published in python as:
     -->    def toggle_bool_pointer(v: BoxedBool) -> None:
    """
    pass

def toggle_bool_nullable(v: BoxedBool = None) -> None:
    """ Test with nullable pointer
     Will be published in python as:
     -->    def toggle_bool_nullable(v: BoxedBool = None) -> None:
    """
    pass

def toggle_bool_reference(v: BoxedBool) -> None:
    """ Test with reference
     Will be published in python as:
     -->    def toggle_bool_reference(v: BoxedBool) -> None:
    """
    pass

def modify_string(s: BoxedString) -> None:
    """ Test modifiable String
     Will be published in python as:
     -->    def modify_string(s: BoxedString) -> None:
    """
    pass


#///////////////////////////////////////////////////////////////////////////////////////////
#
# Test Part 2: in the functions below, the python return type is modified:
# the python functions will return a tuple:
#     (original_return_value, modified_parameter)
#
# This is caused by the following options during generation:
#
#     options.fn_params_output_modifiable_immutable_to_return__regex = r"^Change"
#/////////////////////////////////////////////////////////////////////////////////////////


def change_bool_int(label: str, value: int) -> Tuple[bool, int]:
    """ Test with int param + int return type
     Will be published in python as:
     --> def change_bool_int(label: str, value: int) -> Tuple[bool, int]:
    """
    pass

def change_void_int(label: str, value: int) -> int:
    """ Will be published in python as:
     -->    def change_void_int(label: str, value: int) -> int:
    """
    pass

def change_bool_int2(
    label: str,
    value1: int,
    value2: int
    ) -> Tuple[bool, int, int]:
    """ Will be published in python as:
     -->    def change_bool_int2(label: str, value1: int, value2: int) -> Tuple[bool, int, int]:
    """
    pass

def change_void_int_default_null(
    label: str,
    value: Optional[int] = None
    ) -> Tuple[bool, Optional[int]]:
    """ Will be published in python as:
     -->    def change_void_int_default_null(label: str, value: Optional[int] = None) -> Tuple[bool, Optional[int]]:
    """
    pass

def change_void_int_array(
    label: str,
    value: List[int]
    ) -> Tuple[bool, List[int]]:
    """ Will be published in python as:
     -->    def change_void_int_array(label: str, value: List[int]) -> Tuple[bool, List[int]]:
    """
    pass
####################    </generated_from:modifiable_immutable_test.h>    ####################

# </litgen_stub> // Autogenerated code end!
