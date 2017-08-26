# nodely >>> putMORE Node.js into Python
#
# Copyright (C) 2017 Stefan Zimmermann <user@zimmermann.co>
#
# nodely is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# nodely is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with nodely.  If not, see <http://www.gnu.org/licenses/>.

"""
nodely

putMORE Node.js into Python
"""

import json
import shutil
import sys

from path import Path
import zetup

__all__ = ['install', 'which', 'Popen', 'call']


#: The absolute path to the local node_modules/ sub-directory used for
#  installing Node.js packages under the python environment root
NODE_MODULES_DIR = Path(sys.prefix) / 'node_modules'

# create a dummy package.json in python environment root for making npm
# install packages to node_modules/ sub-directory defined above
(Path(sys.prefix) / 'package.json').write_text(json.dumps({
    'name': "python-nodely",
    'description': "putMORE Node.js into Python",
    'repository': "https://github.com/zimmermanncode/nodely",
}))


def install(package):
    """
    Install a Node.js `package` into ``node_modules/`` of current Python
    environment
    """
    command = ['npm', 'install', package]
    with Path(sys.prefix):
        status = zetup.call(command)
    if status:
        raise RuntimeError("Command {} failed with status {}"
                           .format(command, status))


def which(executable):
    """
    Find `executable` in ``node_modules/.bin/`` of current Python environment

    :return: Absolute ``path.Path`` instance
    """
    return shutil.which(executable, path=NODE_MODULES_DIR / '.bin')


def Popen(executable, args=None, **kwargs):
    """
    Create a subprocess for given Node.js `executable` with given sequence
    of `args` strings and optional `kwargs` for ``zetup.Popen``, including all
    options for ``subprocess.Popen``
    """
    import nodely.bin

    command = nodely.bin[executable]
    return command.Popen(args, **kwargs)


def call(executable, args=None, **kwargs):
    """
    Call given Node.js `executable` with given sequence of `args` strings and
    optional `kwargs` for ``zetup.call``, including all options for
    ``subprocess.call``
    """
    import nodely.bin

    command = nodely.bin[executable]
    return command.call(args, **kwargs)
