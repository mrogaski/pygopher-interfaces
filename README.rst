pygopher-interfaces
===================

.. rubric:: Go-style interfaces for Python

|status| |coverage| |analysis|

Interfaces in the Go programming language are a bit different than those found in Java or C++, as they
are `implicit <https://tour.golang.org/methods/10>`_.  This means that there is no explicit "implements" relationship
between the interface definition and an implementation of the defined interface.  A type implements an interface by
implementing all of the methods defined.  When we wish to define an interface in Python, we typically use abstract
base classes to define them because we can enforce implementation of methods.  This requires us to use inheritance,
which couples the interface and the implementation.

This package emulates Go-style interfaces by creating an ``Interface`` metaclass that can be used to construct Python
classes that override ``issubclass`` to test whether a class implements the methods of the interface class, rather than
whether it inherits from the interface class.

Installation
------------

.. code-block:: console

    pip install pygopher-interfaces
    # or:
    # pipenv install pygopher-interfaces
    # poetry add pygopher-interfaces

Usage
-----

To create an interface class, use the ``Interface`` metaclass.

.. code-block:: python

    from pygopher.interfaces import Interface


    class RepositoryInterface(metaclass=Interface):
        def get(account_id: int) -> Account:
            raise NotImplementedError

        def add(account: Account):
            raise NotImplementedError


    class MysqlRepository:
        def get(account_id: int) -> Account:
            ...

        def add(account: Account):
            ...


    >>> issubclass(MysqlRepository, RepositoryInterface)
    True


.. |status| image:: https://github.com/mrogaski/pygopher-interfaces/actions/workflows/ci.yml/badge.svg
    :alt: Status
    :scale: 100%
    :target: https://github.com/mrogaski/pygopher-interfaces/actions

.. |coverage| image:: https://codecov.io/gh/mrogaski/pygopher-interfaces/branch/main/graph/badge.svg?token=cu6sNIlaWt
    :alt: Test Coverage
    :scale: 100%
    :target: https://codecov.io/gh/mrogaski/pygopher-interfaces

.. |analysis| image:: https://app.codacy.com/project/badge/Grade/0516015cd3f94d66b7a7c8203255b6de
    :alt: Code Quality
    :scale: 100%
    :target: https://www.codacy.com/gh/mrogaski/pygopher-interfaces/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mrogaski/pygopher-interfaces&amp;utm_campaign=Badge_Grade