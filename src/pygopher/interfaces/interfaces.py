"""Interface base class implementations."""
import inspect
from typing import Set, Type


def get_method_signatures(obj: Type) -> Set:
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

    def __subclasscheck__(cls, subclass):
        """

        Args:
            subclass: a class which will be checked for matching method signatures.

        Returns:
            True if the subclass implements the interface, false otherwise.

        """

        interface_methods = get_method_signatures(cls)
        class_methods = get_method_signatures(subclass)
        return interface_methods.issubset(class_methods)

    def __instancecheck__(cls, instance):
        """

        Args:
            instance: an object which will be checked for matching method signatures.

        Returns:
            True if the instance class implements the interface, false otherwise.

        """
        return issubclass(type(instance), cls)
