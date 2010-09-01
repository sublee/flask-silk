# -*- coding: utf-8 -*-
"""
    flaskext.silk
    ~~~~~~~~~~~~~

    A small extension for adding `Silk icons
    <http://www.famfamfam.com/lab/icons/silk/>`_.

    :copyright: (c) 2010 by Lee Heung-sub.
    :license: BSD, see LICENSE for more details.
"""
import os.path
from flask import send_from_directory


class Silk(object):
    """This small extension add :meth:`silkicon` to your Flask application or
    module. Just::

        from flask import Flask
        from flaskext.silk import Silk
        app = Flask(__name__)
        silk = Silk(app)

    :param base: a flask application or module
    :param silk_path: a path to serve silk icons. default is ``/icons``.
    """

    def __init__(self, base, silk_path="/icons"):
        self.base = base
        if not silk_path.startswith("/"):
            silk_path = "/" + silk_path
        rule = silk_path + "/<filename>"
        self.silkicon = self.base.route(rule)(self.silkicon)

    def silkicon(self, filename=None, iconname=None, ext="png"):
        directory = os.path.join(os.path.dirname(__file__), "icons")
        if not filename:
            filename = iconname + os.path.extsep + ext
        return send_from_directory(directory, filename)
