#!/usr/bin/env python

from common.parse_netflow import parse_netflow
from canari.framework import configure
from common.entities import Port
from canari.maltego.message import UIMessage, Field
from canari.maltego.entities import IPv4Address

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
    label='[NF] - Get Destination Port',
    description='Get Destination Port from dump file',
    uuids=['netflow.v2.dump_2_getdestport'],
    inputs=[('Netflow', IPv4Address)],
    debug=True
)
def dotransform(request, response):
    ip = request.value
    dump = request.fields['dumpfile']
    x = parse_netflow(dump)
    for i in x:
        srcip = i[4]
        srcip = srcip.split(':')[0]
        if ip in srcip:
            dport = i[6]
            dport = dport.split(':')[1]
            e = Port(dport)
            e += Field('dumpfile', dump, displayname='Dump File')
            response += e
        else:
            pass
    return response
