#!/usr/bin/env python

from common.parse_netflow import parse_netflow
from canari.framework import configure
from common.entities import Port
from canari.maltego.message import Field
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
        dstip = i[6]
        dstip = dstip.split(':')[0]
        proto = i[3]
        if ip in dstip:
            dport = i[6]
            dport = dport.split(':')[1]
            e = Port(dport)
            e += Field('dumpfile', dump, displayname='Dump File', matchingrule='loose')
            # e.linklabel = proto
            if proto == 'TCP':
                e.linkcolor = 0xff0000
            if proto == 'UDP':
                e.linkcolor = 0x002bff
            if proto == 'ICMP':
                e.linkcolor = 0x2f9a0d
            response += e
        else:
            pass
    return response
