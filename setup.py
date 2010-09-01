"""
flask-silk
----------

Adds `silk icons`_ to your Flask application or module, or extension.

Links
`````

* `documentation <http://packages.python.org/flask-silk>`_
* `development version
  <http://github.com/sublee/flask-silk/zipball/master#egg=flask-silk-dev>`_

"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="flask-silk",
    version="0.1.0",
    url="http://github.com/sublee/flask-silk",
    license="BSD",
    author="Lee Heung-sub",
    author_email="heung@sublee.kr",
    description="Adds `silk icons`_ to your Flask application or module, "
                "or extension.",
    long_description=__doc__,
    packages=["flaskext", "flaskext.silk"],
    include_package_data=True,
    package_data={"flaskext.silk": ["icons/*"]},
    namespace_packages=["flaskext"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "Flask"
    ],
    test_suite="test",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)