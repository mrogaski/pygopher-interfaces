# pylint: disable=missing-class-docstring,missing-function-docstring,no-self-use
"""Test behavior of abstract base class."""

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
    """Test subclass relationship with methods on the interface and the subclass."""

    class AbstractDingus(Interface):
        def do_something(self):
            raise NotImplementedError

    class Dingus:
        def do_something(self):
            return True

    assert issubclass(Dingus, AbstractDingus)


def test_subclass_failure():
    """Test subclass relationship with subclass that does not implement the interface."""

    class AbstractDingus(Interface):
        def do_something(self):
            raise NotImplementedError

    class Dingus:
        pass

    assert not issubclass(Dingus, AbstractDingus)
