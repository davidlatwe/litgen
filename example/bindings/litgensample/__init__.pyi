from typing import List
from typing import (
    Literal,  # for enums annotations, when some enum values depend on other values of the same enum
)
import numpy as np
from enum import Enum

# Disable black formatter
# fmt: off

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
# <Autogenerated_Boxed_Types>
class BoxedBool:
    value:bool
    def __init__(self, v: bool = False) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedUnsignedLong:
    value:int
    def __init__(self, v: int = 0) -> None:
        pass
    def __repr__(self) -> str:
        pass
class BoxedInt:
    value:int
    def __init__(self, v: int = 0) -> None:
        pass
    def __repr__(self) -> str:
        pass
# </Autogenerated_Boxed_Types>






# <Namespace LiterateGeneratorExample>
def toggle_bool(v_0: BoxedBool) -> None:
    pass

#    MY_API None ToggleBool2(std::shared_ptr<bool> v) {
#        bool *b = v.get();
#        printf("ToggleBool2 ptr=%p value=%s\n", b, (*b) ? "True" : "False");
#        *b = !(*b);
#    }



class MyEnum(Enum):
    """ A super nice enum
     for demo purposes ( bool val = False )
    """
    a = 1    # This is value a
    aa = 2   # this is value aa
    aaa = 3  # this is value aaa

    # Lonely comment

    # This is value b
    b = 4

    # This is c
    # with doc on several lines
    c = Literal[MyEnum.a] | Literal[MyEnum.b]


#
# C Style array tests
#

# Tests with Boxed Numbers
def add_c_array2(values: List[int]) -> int:
    pass
def log_c_array2(values: List[int]) -> None:
    pass
def change_c_array2(
    values_0: BoxedUnsignedLong,
    values_1: BoxedUnsignedLong
    ) -> None:
    pass
class Point2:
    """ Test with C array containing user defined struct (which will not be boxed)"""
    x:int
    y:int
def get_points(out_0: Point2, out_1: Point2) -> None:
    pass

#
# C Style buffer to py::array tests
#

def add_inside_buffer(buffer: np.ndarray, number_to_add: int) -> None:
    """ Modifies a buffer by adding a value to its elements"""
    pass
def buffer_sum(buffer: np.ndarray, stride: int = -1) -> int:
    """ Returns the sum of a const buffer"""
    pass
def add_inside_two_buffers(
    buffer_1: np.ndarray,
    buffer_2: np.ndarray,
    number_to_add: int
    ) -> None:
    """ Modifies two buffers"""
    pass


def mul_inside_buffer(buffer: np.ndarray, factor: float) -> None:
    """ Modify an array by multiplying its elements (template function!)"""
    pass

#
# C String lists tests
#

def c_string_list_total_size(
    items: List[str],
    output_0: BoxedInt,
    output_1: BoxedInt
    ) -> int:
    pass


def add(a: int, b: int) -> int:
    """ Adds two numbers"""
    pass

# Adds three numbers, with a surprise
# MY_API inline int add(int a, int b, int c) { return a + b + c + 4; }


def sub(a: int, b: int) -> int:
    pass

def mul(a: int, b: int) -> int:
    pass

class Foo:
    """ A superb struct"""
    def __init__(self) -> None:
        pass

    #
    # These are our parameters
    #

    #
    # Test with numeric arrays which should be converted to py::array
    #
    values:np.ndarray  # ndarray[type=int, size=2] default:{0, 1}
    flags:np.ndarray   # ndarray[type=bool, size=3] default:{False, True, False}


    # Multiplication factor
    factor:int = 10

    # addition factor
    delta:int

    #
    # And these are our calculations
    #

    def calc(self, x: int) -> int:
        """ Do some math"""
        pass


def foo_instance() -> Foo:
    """ return_value_policy::reference"""
    pass


def set_foo_delta_to50_pointer(f: Foo) -> None:
    pass
def set_foo_delta_to25_ref(f: Foo) -> None:
    pass

#
# </Namespace LiterateGeneratorExample>

# </litgen_stub>

# fmt: on
