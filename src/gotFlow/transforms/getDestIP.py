#!/usr/bin/env python

from common.parse_netflow import parse_netflow
from canari.framework import configure
from common.entities import Port
from canari.maltego.message import UIMessage, Field, MatchingRule
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
    label='[NF] - Get Destination IP',
    description='Get Destination IP from dump file',
    uuids=['netflow.v2.dump_2_getdestip'],
    inputs=[('Netflow', Port)],
    debug=True
)
def dotransform(request, response):
    port = request.value
    dump = request.fields['dumpfile']
    x = parse_netflow(dump)
    for i in x:
        dstport = i[6]
        dstport = dstport.split(':')[1]
        proto = i[3]
        if port in dstport:
            dip = i[6]
            dip = dip.split(':')[0]
            e = IPv4Address(dip)
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
