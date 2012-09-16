"""
Flask-Silk
----------

Adds `silk`_ icons to your Flask application or module, or extension.

Links
`````

* `documentation <http://packages.python.org/Flask-Silk>`_
* `development version
  <http://github.com/sublee/flask-silk/zipball/master#egg=flask-silk-dev>`_

.. _silk: http://www.famfamfam.com/lab/icons/silk

"""
from setuptools import setup


setup(
    name='Flask-Silk',
    version='0.1.2',
    url='http://github.com/sublee/flask-silk',
    license='BSD',
    author='Heungsub Lee',
    author_email='h@subl.ee',
    description='Adds silk icons to your Flask application or module, or ' \
                'extension.',
    long_description=__doc__,
    packages=['flaskext', 'flaskext.silk'],
    include_package_data=True,
    package_data={'flaskext.silk': ['icons/*']},
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    test_suite='test',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
