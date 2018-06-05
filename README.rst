catlolzer
#########
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

An advanced Python-based cat lolzing engine.

.. code-block:: python

  >>> from catlolzer import CatLolzer
  >>> mylolzer = CatLolzer(alpha=8)
  >>> for cat in my_crazy_cats:
  ...   mylolzer.lolize(cat)

.. contents::

.. section-numbering::


Installation
============

Dependencies:

* ``numpy``

.. code-block:: bash

  pip install catlolzer
  


Features
========

* Powerfull cat lolzing.
* Pure python.
* Supports Python 3.5+.
* Fully tested.


Use
===

This is just a dummy repo for you to copy and base you own Python packge on!


Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/catlolzer.git


Install in development mode, including test dependencies:

.. code-block:: bash

  cd catlolzer
  pip install -e '.[test]'



Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  cd catlolzer
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt

Additionally, if you update this ``README.rst`` file,  use ``python setup.py checkdocs`` to validate it compiles.


Credits
=======

Created by Shay Palachy (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/catlolzer.svg
  :target: https://pypi.python.org/pypi/catlolzer

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/catlolzer.svg
   :target: https://pypi.python.org/pypi/catlolzer

.. |Build-Status| image:: https://travis-ci.org/shaypal5/catlolzer.svg?branch=master
  :target: https://travis-ci.org/shaypal5/catlolzer

.. |LICENCE| image:: https://github.com/shaypal5/catlolzer/blob/master/mit_license_badge.svg
  :target: https://github.com/shaypal5/catlolzer/blob/master/LICENSE
  
.. https://img.shields.io/github/license/shaypal5/catlolzer.svg

.. |Codecov| image:: https://codecov.io/github/shaypal5/catlolzer/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/catlolzer?branch=master
