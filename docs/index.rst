Flask-Silk
~~~~~~~~~~

.. module:: flask_silk

Flask-Silk is small Flask extension. It adds `silk`_ icons to your Flask
application or blueprint, or extension!

Silk is very awesome. It will be good for your Flask extensions. But if
someone use many Flask extensions which contains silk icons, they will lose
their storage space too much. They can solve the problem with Flask-Silk.

If you want to preview silk icons, visit :doc:`/dict`.

.. note::
   Silk is licensed under `Creative Commons Attribution 2.5 License
   <http://creativecommons.org/licenses/by/2.5>`_ or
   `3.0 License <http://creativecommons.org/licenses/by/3.0>`_. Before using
   the icons, read the license.

.. _silk: http://www.famfamfam.com/lab/icons/silk

Installation
============

Install via `PyPI <http://pypi.python.org/pypi/Flask-Silk>`_::

    $ easy_install Flask-Silk

Or check out development version::

    $ git clone git://github.com/sublee/flask-silk.git

How to Use
==========

If you want to contain silk icons to your application, follow the below
example::

    from flask import Flask
    from flask.ext.silk import Silk
    app = Flask(__name__)
    silk = Silk(app)

In your application, you can get an icon's url by::

    url_for('silkicon', filename='bug.png')

It also works with Flask blueprint::

    from flask import Blueprint
    from flask.ext.silk import Silk
    blu = Blueprint(__name__, __name__)
    silk = Silk(blu)

API
===

.. autoclass:: Silk
   :members:

.. autofunction:: send_silkicon

Indices and tables
==================

* :doc:`/dict`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
