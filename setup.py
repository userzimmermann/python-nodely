import os

from setuptools import setup


ROOT = os.path.dirname(os.path.realpath(__file__))


setup(
    name='nodely',
    description="putMORE Node.js into Python",

    author="Stefan Zimmermann",
    author_email="user@zimmermann.co",
    url="https://github.com/zimmermanncode/nodely",

    license='LGPLv3',

    setup_requires=open(os.path.join(ROOT, 'requirements.setup.txt')).read(),
    install_requires=open(os.path.join(ROOT, 'requirements.txt')).read(),

    use_scm_version={'write_to': 'nodely/__version__.py'},

    packages=[
        'nodely',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved'
        ' :: GNU Library or Lesser General Public License (LGPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    keywords=[
        'nodely', 'nodejs', 'node', 'npm', 'npmjs',
        'javascript', 'js', 'ecmascript', 'ecma', 'es',
        'install', 'which', 'subprocess', 'popen', 'call',
    ],
)
