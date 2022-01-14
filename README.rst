==============================
Check for conventional commits
==============================

CLI to check about that commit message is based on "conventional commits". (include ``pre-commit`` hooks)

Description
===========

`Conventional Commits <https://www.conventionalcommits.org/>`_ is specification for commit messages.
This repository is python package to provide CLI command and ``pre-commit`` hooks definitions
to check that your commit messages are based on spec of "conventional commits".

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

For pre-commit (recommended)
----------------------------

This repository includes definition of ``pre-commit`` hooks.
You can run it simply in your repository.

.. code-block:: yaml

   repos:
     - repo: https://github.com/attakei/check-conventional-commits
       rev: v0.0.1
       hooks:
         - id: check-conventional-commits

.. note::

   This hook run on "commit-msg" stage.
   You shoud set commit-msg hooks by ``pre-commit install -t commit-msg``

Contribution
============

(TBD)

License
=======

`Apache License, Version 2.0 <./LICENSE>`_
