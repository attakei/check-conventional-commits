==============================
Check for conventional commits
==============================

CLI to check about that commit message is based on "conventional commits". (include ``pre-commit`` hooks)

Description
===========

(TBD)

Installation & Usage
====================

For CLI
-------

Install from GitHub

.. code-block:: console

   $ pip install git+https://github.com/attakei/check-conventional-commits

When using CLI, you can pass message by STDIN or file.

.. code-block:: console

   $ echo "feat: Implement new func" | check-conventional-commits
   (If it is valid, no output and exit 0)

   $ echo "Fix it" | check-conventional-commits
   (If is is invalid, output message and exit 1)

If you want to append other types, use ``--extra-types``

.. code-block:: console

   $ echo "test: Implement new func" | check-conventional-commits
   (invalid)

   $ echo "test: Implement new func" | check-conventional-commits --extra-types=test
   (valid!)

For pre-commit
--------------

(TBD)

Contribution
============

(TBD)

License
=======

`Apache License, Version 2.0 <./LICENSE>`_
