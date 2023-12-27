import pytest

from task2 import find_in_different_registers

def test_find_in_different_registers():
    assert find_in_different_registers(["hello", "world", "hello"]) == ["world"]
    assert find_in_different_registers(["hello", "world", "hello", "world"]) == []
    assert find_in_different_registers(["hello", "world", "hello", "world", "hello"]) == []
    assert find_in_different_registers(["hello", "world", "Hello", "wOrld", "heLlo", "World"]) == ["hello", "world"] or find_in_different_registers(["hello", "world", "Hello", "wOrld", "heLlo", "World"]) == ["world", "hello"]

