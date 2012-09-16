# -*- coding: utf-8 -*-
"""
    flaskext.silk
    ~~~~~~~~~~~~~

    A small extension for adding `Silk
    <http://www.famfamfam.com/lab/icons/silk/>`_ icons.

    :copyright: (c) 2010-2012 by Heungsub Lee.
    :license: BSD, see LICENSE for more details.
"""
import os

from flask import send_from_directory


__copyright__ = 'Copyright 2010-2012 by Heungsub Lee'
__license__ = 'BSD License'
__author__ = 'Heungsub Lee'
__email__ = 'h''@''subl.ee'
__version__ = '0.1.2'
__all__ = ['Silk', 'send_silkicon']


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

    Now the application or module's ``/icons/<filaname>`` is bound to
    :meth:`silkicon` for serves a prepared silk icon.

    Also you can work with your own icon directory::

        import os.path
        my_icons = os.path.join(silk.base.static_path, 'icons')
        my_icons2 = os.path.join(silk.base.static_path, 'other-icons')
        silk.register_icon_directory(my_icons)
        silk.register_icon_directory(my_icons2)

    Silk finds the icon in the registered directories first. If the icon does
    not exist in any directories, Silk finds the prepared silk icon.

    :param base: a flask application or module
    :param silk_path: a path to serve silk icons. default is ``/icons``.
    """

    directories = []

    def __init__(self, base, silk_path='/icons'):
        self.base = base
        if not silk_path.startswith('/'):
            silk_path = '/' + silk_path
        rule = silk_path + '/<filename>'
        self.silkicon = self.base.route(rule)(self.silkicon)

    def register_icon_directory(self, path):
        self.directories.append(path)

    def silkicon(self, filename):
        return send_silkicon(filename, directories=self.directories)


def send_silkicon(filename, directories=[]):
    """Sends an icon. The icon is in a shared directory or specified
    directories. Here's a simple examples of how to send an icon::

        from flaskext.silk import send_silkicon
        from myapplication import app

        my_icons = os.path.join(app.static_path, 'icons')
        my_icons2 = os.path.join(app.static_path, 'other-icons')

        @app.route('/static/icons/<filename>')
        def icon(filename):
            return send_silkicon(filename, directories=[my_icons, my_icons2])

    :param filename: a filename for icon
    :param directories: specified icon directories
    """
    for directory in directories:
        try:
            return send_from_directory(directory, filename)
        except Exception:
            pass
    directory = os.path.join(os.path.dirname(__file__), 'icons')
    return send_from_directory(directory, filename)
