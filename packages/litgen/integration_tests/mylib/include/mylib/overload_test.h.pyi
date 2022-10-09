# ============================================================================
# This file was autogenerated
# It is presented side to side with its source: overload_test.h
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
####################    <generated_from:overload_test.h>    ####################

#
# litgen is able to detect automatically the presence of overloads that require
# to use `py::overload_cast<...>` when publishing
#

#
# overload on free functions
#

def add_overload(a: int, b: int) -> int:  # type: ignore
    pass
def add_overload(a: int, b: int, c: int) -> int:  # type: ignore
    pass

#
# overload on methods
#

class FooOverload:
    def add_overload(self, a: int, b: int) -> int:          # type: ignore
        pass
    def add_overload(self, a: int, b: int, c: int) -> int:  # type: ignore
        pass
####################    </generated_from:overload_test.h>    ####################

# </litgen_stub> // Autogenerated code end!
