from setuptools import setup, find_packages


setup(
    name='Flask-DebugToolbar',
    version='0.02',
    url='http://github.com/mvantellingen/flask-debugtoolbar',
    license='BSD',
    author='Michael van Tellingen',
    author_email='michaelvantellingen@gmail.com',
    description='A port of the Django debug toolbar to Flask',
    long_description=__doc__,
    packages=find_packages(),
    package_dir={'flaskext.debugtoolbar': 'flaskext/debugtoolbar'},
    package_data={'flaskext.debugtoolbar': [
        'static/css/*.css', 'static/js/*.js', 'static/img/*',
        'templates/*.html', 'templates/panels/*.html'
    ]},
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
