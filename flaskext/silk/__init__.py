# -*- coding: utf-8 -*-
"""
    flaskext.silk
    ~~~~~~~~~~~~~

    A small extension for adding `Silk
    <http://www.famfamfam.com/lab/icons/silk/>`_ icons.

    :copyright: (c) 2010 by Lee Heung-sub.
    :license: BSD, see LICENSE for more details.
"""
import os.path
from flask import send_from_directory


class Silk(object):
    """This small extension adds :meth:`silkicon` to your Flask application::

        from flask import Flask
        from flaskext.silk import Silk
        app = Flask(__name__)
        silk = Silk(app)

    Or it works with your Flask module::

        from flask import Module
        from flaskext.silk import Silk
        mod = Module(__name__)
        silk = Silk(mod)

    :param base: a flask application or module
    :param silk_path: a path to serve silk icons. default is ``/icons``.
    """

    def __init__(self, base, silk_path="/icons"):
        self.base = base
        if not silk_path.startswith("/"):
            silk_path = "/" + silk_path
        rule = silk_path + "/<filename>"
        self.silkicon = self.base.route(rule)(self.silkicon)

    def silkicon(self, filename):
        return send_silkicon(filename)


def send_silkicon(filename=None, iconname=None, ext="png"):
    """Sends a silk icon. The icon is in a shared directory.

    An example::

        from flaskext.silk import send_silkicon
        from myapplication import app
        @app.route("/static/icons/<filename>")
        def icon(filename):
            return send_silkicon(filename)
    """
    directory = os.path.join(os.path.dirname(__file__), "icons")
    if not filename:
        filename = iconname + os.path.extsep + ext
    return send_from_directory(directory, filename)

