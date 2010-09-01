flask-silk
~~~~~~~~~~

.. module:: flaskext.silk

flask-silk adds `silk icons`_ to your Flask application or module, or
extension!

Silk icons are very awesome. So these are expected to be used by many good
Flask extensions. But if you use many Flask extensions which contains silk
icons, you'll lose your storage space too much. Flask extensions should import
this small extension if these need.

.. _silk icons: http://www.famfamfam.com/lab/icons/silk

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

