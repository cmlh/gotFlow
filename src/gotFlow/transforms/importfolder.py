#!/usr/bin/env python

import glob
import os.path
from canari.framework import configure
from common.entities import DumpFile, Folder
from canari.maltego.message import UIMessage

__author__ = 'Adam Maxwell'
__copyright__ = 'Copyright 2015, Gotflow Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Adam Maxwell'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label='[NF] - Import Files',
    description='Import nfdump files from a folder',
    uuids=['netflow.v2.import_from_folder'],
    inputs=[('Netflow', Folder)],
    debug=True
)
def dotransform(request, response):
    folder = request.value
    if not os.path.exists(folder):
        return response + UIMessage("Path not valid, please check")
    else:
        dump_files = glob.glob(folder + '/*')
        for f in dump_files:
            e = DumpFile(f)
            response += e
        return response
