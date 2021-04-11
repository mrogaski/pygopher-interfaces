# pylint: disable=missing-class-docstring,missing-function-docstring,no-self-use
"""Test behavior of abstract base class."""
from typing import List

from pygopher.interfaces import Interface


def test_subclass_trivial():
    """Test subclass relationship with no defined methods."""

    class AbstractDingus(Interface):
        def do_something(self):
            pass

    class Dingus:
        def do_something(self):
            pass

    assert issubclass(Dingus, AbstractDingus)


def test_subclass_trivial_with_methods():
    """Test subclass relationship with no interface methods and methods on the subclass."""

    class AbstractDingus(Interface):
        def do_something(self):
            pass

    class Dingus:
        def do_something(self):
            return True

    assert issubclass(Dingus, AbstractDingus)


def test_subclass_equivalent():
    """Test subclass relationship with matching methods on the interface and the subclass."""

    class AbstractDingus(Interface):
        def do_something(self):
            raise NotImplementedError

    class Dingus:
        def do_something(self):
            return True

    assert issubclass(Dingus, AbstractDingus)


def test_subclass_equivalent_signatures():
    """Test subclass relationship with matching method signatures on the interface and the subclass."""

    class AbstractDingus(Interface):
        def do_something(self, a: str, b: int) -> bool:
            raise NotImplementedError

    class Dingus:
        def do_something(self, a: str, b: int) -> bool:
            return True

    assert issubclass(Dingus, AbstractDingus)


def test_subclass_failure_missing_method():
    """Test subclass relationship with subclass that does not implement the interface."""

    class AbstractDingus(Interface):
        def do_something(self):
            raise NotImplementedError

    class Dingus:
        pass

    assert not issubclass(Dingus, AbstractDingus)


def test_subclass_failure_argument_mismatch():
    """Test subclass relationship with subclass that does not implement the interface argument signatures."""

    class AbstractDingus(Interface):
        def do_something(self, a: str):
            raise NotImplementedError

    class Dingus:
        def do_something(self):
            raise NotImplementedError

    assert not issubclass(Dingus, AbstractDingus)


def test_subclass_failure_argument_type_mismatch():
    """Test subclass relationship with subclass that does not implement the interface argument signature typing."""

    class AbstractDingus(Interface):
        def do_something(self, a: str):
            raise NotImplementedError

    class Dingus:
        def do_something(self, a: int):
            raise NotImplementedError

    assert not issubclass(Dingus, AbstractDingus)


def test_subclass_failure_return_type_mismatch():
    """Test subclass relationship with subclass that does not implement the interface return signature typing."""

    class AbstractDingus(Interface):
        def do_something(self, a: str) -> bool:
            raise NotImplementedError

    class Dingus:
        def do_something(self, a: str) -> List[bool]:
            raise NotImplementedError

    assert not issubclass(Dingus, AbstractDingus)
