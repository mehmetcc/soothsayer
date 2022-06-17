frens tell me this is not idiomatic but still..

soothsayer
==========

.. contents:: Table of Contents
    :depth: 3

Summary
-------
soothsayer is the most simple microservice ever possible to serve the default sentiment analysis model provided by flair (a python package).

Dependencies
------------
This microservice is dependent on the following python packages:

* fastapi
* flair
* uvicorn

The code is being managed and built by **poetry**.

Running the service
-------------------
Make sure you have a working poetry installation. Check their `docs <#https://python-poetry.org/docs/>`_ for more information.

After getting a working copy of poetry, type in the following commands:

.. code-block:: bash

    poetry install
    poetry run start

To run tests:

.. code-block:: bash

    poetry run pytest tests/

