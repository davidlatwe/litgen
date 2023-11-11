from __future__ import annotations
import lg_mylib


def test_const_array2_add():
    a = [5, 6]
    r = lg_mylib.const_array2_add(a)
    assert r == 11

    got_exception = False
    try:
        lg_mylib.const_array2_add([1, 2, 3])
    except TypeError:
        got_exception = True
    assert got_exception


def test_array2_change():
    a = lg_mylib.BoxedUnsignedLong(5)
    b = lg_mylib.BoxedUnsignedLong(6)
    lg_mylib.array2_modify(a, b)
    assert a.value == 11
    assert b.value == 66


def test_array2_modify_mutable():
    pt1 = lg_mylib.Point2(50, 51)
    pt2 = lg_mylib.Point2(53, 54)
    lg_mylib.array2_modify_mutable(pt1, pt2)
    assert pt1.x == 0 and pt1.y == 1 and pt2.x == 2 and pt2.y == 3
