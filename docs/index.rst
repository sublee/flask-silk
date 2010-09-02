flask-silk
~~~~~~~~~~

.. module:: flaskext.silk

flask-silk is small Flask extension. It adds `silk`_ icons to your Flask
application or module, or extension!

Silk is very awesome. It will be good for your Flask extensions. But if
someone use many Flask extensions which contains silk icons, they will lose
their storage space too much. They can solve the problem with flask-silk.

.. note::
   Silk is licensed under a `Creative Commons Attribution 2.5 License.
   <http://creativecommons.org/licenses/by/2.5/>`_ or
   `3.0 License <http://creativecommons.org/licenses/by/3.0/>`_. Before using
   the icons, read the license.

.. _silk: http://www.famfamfam.com/lab/icons/silk

Installation
============

Check out development version::

    $ git clone git://github.com/sublee/flask-silk.git

How to Use
==========

If you want to contain silk icons to your application, follow the below
example::

    from flask import Flask
    from flaskext.silk import Silk
    app = Flask(__name__)
    silk = Silk(app)

In your application, you can get an icon's url by::

    url_for("silkicon", filename="bug.png")

It also works with Flask module::

    from flask import Module
    from flaskext.silk import Silk
    mod = Module(__name__)
    silk = Silk(mod)

API
===

.. autoclass:: Silk
   :members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

