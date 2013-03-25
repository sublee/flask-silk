"""
Flask-Silk
----------

Adds `silk`_ icons to your Flask application or blueprint, or extension.

Links
`````

* `documentation <http://packages.python.org/Flask-Silk>`_
* `development version
  <http://github.com/sublee/flask-silk/zipball/master#egg=flask-silk-dev>`_

.. _silk: http://www.famfamfam.com/lab/icons/silk

"""
import re
from setuptools import setup


setup(
    name='Flask-Silk',
    version='0.2',
    license='BSD',
    author='Heungsub Lee',
    author_email=re.sub('((sub).)(.*)', r'\2@\1.\3', 'sublee'),
    url='http://github.com/sublee/flask-silk',
    description='Adds silk icons to your Flask application or blueprint, or '
                'extension.',
    long_description=__doc__,
    packages=['flask_silk'],
    include_package_data=True,
    package_data={'flask_silk': ['icons/*']},
    zip_safe=False,
    platforms='any',
    install_requires=['Flask>=0.8'],
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
