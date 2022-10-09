// ============================================================================
// This file was autogenerated
// It is presented side to side with its source: call_policies_test.h
// It is not used in the compilation
//    (see integration_tests/bindings/pybind_mylib.cpp which contains the full binding
//     code, including this code)
// ============================================================================

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>

#include "mylib/mylib.h"

namespace py = pybind11;

// <litgen_glue_code>  // Autogenerated code below! Do not edit!

// </litgen_glue_code> // Autogenerated code end


void py_init_module_MYLIB(py::module& m)      //  rename this function name!!!
{
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:call_policies_test.h>    ////////////////////
    m.def("call_guard_tester",
        call_guard_tester,
        "// py::call_guard<CallGuardLogger>()",
        py::call_guard<CallGuardLogger>());


    auto pyClassCallGuardLogger =
        py::class_<CallGuardLogger>
            (m, "CallGuardLogger", " ============================================================================\n CallGuardLogger: dummy call guard for the tests\n ============================================================================")
        .def(py::init<>())
        .def_readwrite_static("nb_construct", &CallGuardLogger::nb_construct, "")
        .def_readwrite_static("nb_destroy", &CallGuardLogger::nb_destroy, "")
        ;
    ////////////////////    </generated_from:call_policies_test.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
}
