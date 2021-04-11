"""Interface base class implementations."""
from typing import Set, Type


class InterfaceMeta(type):

    """Metaclass that defines the subclass relationship without inheritance."""

    def __subclasscheck__(cls, subclass):
        def get_methods(obj: Type) -> Set:
            """
            Return the set of public methods for a class.

            Args:
                obj: a class

            Returns:
                A set containing the method names.  Dunder methods, private methods, and properties are excluded.

            """
            return {
                attribute
                for attribute in dir(obj)
                if callable(getattr(obj, attribute)) and attribute.startswith("_") is False
            }

        interface_methods = get_methods(cls)
        class_methods = get_methods(subclass)
        return interface_methods.issubset(class_methods)


class Interface(metaclass=InterfaceMeta):

    """An interface base class."""
