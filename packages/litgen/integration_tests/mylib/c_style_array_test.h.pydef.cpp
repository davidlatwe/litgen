// ============================================================================
// This file was autogenerated
// It is presented side to side with its source: c_style_array_test.h
// It is not used in the compilation
//    (see integration_tests/bindings/pybind_mylib.cpp which contains the full binding
//     code, including this code)
// ============================================================================

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>
#include <pybind11/numpy.h>
#include "mylib/mylib_main/mylib.h"

namespace py = pybind11;

// <litgen_glue_code>  // Autogenerated code below! Do not edit!
struct BoxedUnsignedLong
{
    unsigned long value;
    BoxedUnsignedLong(unsigned long v = 0) : value(v) {}
    std::string __repr__() const { return std::string("BoxedUnsignedLong(") + std::to_string(value) + ")"; }
};

// </litgen_glue_code> // Autogenerated code end


void py_init_module_mylib(py::module& m)
{
    // <litgen_pydef> // Autogenerated code below! Do not edit!
    ////////////////////    <generated_from:BoxedTypes>    ////////////////////
    auto pyClassBoxedUnsignedLong =
        py::class_<BoxedUnsignedLong>
            (m, "BoxedUnsignedLong", "")
        .def_readwrite("value", &BoxedUnsignedLong::value, "")
        .def(py::init<unsigned long>(),
            py::arg("v") = 0)
        .def("__repr__",
            &BoxedUnsignedLong::__repr__)
        ;
    ////////////////////    </generated_from:BoxedTypes>    ////////////////////


    ////////////////////    <generated_from:c_style_array_test.h>    ////////////////////
    m.def("const_array2_add",
        [](const std::array<int, 2>& values) -> int
        {
            auto const_array2_add_adapt_fixed_size_c_arrays = [](const std::array<int, 2>& values) -> int
            {
                auto r = const_array2_add(values.data());
                return r;
            };

            return const_array2_add_adapt_fixed_size_c_arrays(values);
        },
        py::arg("values"),
        " Tests with const array: since the input numbers are const, their params are published as List[int],\n and the python signature will be:\n -->    def add_c_array2(values: List[int]) -> int:\n (and the runtime will check that the list size is exactly 2)");

    m.def("array2_modify",
        [](BoxedUnsignedLong & values_0, BoxedUnsignedLong & values_1)
        {
            auto array2_modify_adapt_fixed_size_c_arrays = [](BoxedUnsignedLong & values_0, BoxedUnsignedLong & values_1)
            {
                unsigned long values_raw[2];
                values_raw[0] = values_0.value;
                values_raw[1] = values_1.value;

                array2_modify(values_raw);

                values_0.value = values_raw[0];
                values_1.value = values_raw[1];
            };

            array2_modify_adapt_fixed_size_c_arrays(values_0, values_1);
        },
        py::arg("values_0"), py::arg("values_1"),
        " Test with a modifiable array: since the input array is not const, it could be modified.\n Thus, it will be published as a function accepting Boxed values:\n -->    def array2_modify(values_0: BoxedUnsignedLong, values_1: BoxedUnsignedLong) -> None:");


    auto pyClassPoint2 =
        py::class_<Point2>
            (m, "Point2", "")
        .def(py::init<>([](
        int x = int(), int y = int())
        {
            auto r = std::make_unique<Point2>();
            r->x = x;
            r->y = y;
            return r;
        })
        , py::arg("x") = int(), py::arg("y") = int()
        )
        .def_readwrite("x", &Point2::x, "")
        .def_readwrite("y", &Point2::y, "")
        ;


    m.def("array2_modify_mutable",
        [](Point2 & out_0, Point2 & out_1)
        {
            auto array2_modify_mutable_adapt_fixed_size_c_arrays = [](Point2 & out_0, Point2 & out_1)
            {
                Point2 out_raw[2];
                out_raw[0] = out_0;
                out_raw[1] = out_1;

                array2_modify_mutable(out_raw);

                out_0 = out_raw[0];
                out_1 = out_raw[1];
            };

            array2_modify_mutable_adapt_fixed_size_c_arrays(out_0, out_1);
        },
        py::arg("out_0"), py::arg("out_1"),
        " Test with a modifiable array that uses a user defined struct.\n Since the user defined struct is mutable in python, it will not be Boxed,\n and the python signature will be:\n-->    def get_points(out_0: Point2, out_1: Point2) -> None:");
    ////////////////////    </generated_from:c_style_array_test.h>    ////////////////////

    // </litgen_pydef> // Autogenerated code end
}
