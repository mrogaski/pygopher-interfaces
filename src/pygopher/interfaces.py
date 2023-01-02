"""Interface base class implementations."""
import inspect
import sys
import typing as tp


if sys.version_info < (3, 8):
    from importlib_metadata import version
else:
    from importlib.metadata import version

__version__ = version("pygopher-interfaces")


def method_signatures(obj: type) -> tp.Set[inspect.Signature]:
    """
    Return the set of public method signatures for a class.

    Args:
        obj: a class

    Returns:
        A set containing the method signatures.  Dunder methods, private methods, and properties are excluded.

    """
    return {
        inspect.signature(attribute)
        for attribute in [getattr(obj, name) for name in dir(obj) if not name.startswith("_")]
        if callable(attribute)
    }


class Interface(type):
    """
    Metaclass that defines the subclass relationship without inheritance.
    """

    def __subclasscheck__(cls, subclass: type) -> bool:
        """

        Args:
            subclass: a class which will be checked for matching method signatures.

        Returns:
            True if the subclass implements the interface, false otherwise.

        """

        interface_methods = method_signatures(cls)
        class_methods = method_signatures(subclass)
        return interface_methods.issubset(class_methods)

    def __instancecheck__(cls, instance: type) -> bool:
        """

        Args:
            instance: an object which will be checked for matching method signatures.

        Returns:
            True if the instance class implements the interface, false otherwise.

        """
        return issubclass(type(instance), cls)
