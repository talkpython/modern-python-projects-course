.. Uptimer documentation master file, created by
   sphinx-quickstart on Wed Dec 16 11:45:26 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Uptimer's documentation!
===================================

Uptimer is a CLI tool to monitor the status of websites.
Specify a URL, and it will return its HTTP status code.

Quickstart
----------

1. Install poetry (Uptimer uses `poetry <https://python-poetry.org/>`_):

   $ pip install poetry

2. Install dependencies

   $ pip install

3. Run uptimer

   $ poetry run uptimer https://www.website-to-check/


CLI commands
------------

.. click:: uptimer.uptimer:check
    :prog: uptimer


Useful links
------------

.. toctree::
   :maxdepth: 2

   api.rst
