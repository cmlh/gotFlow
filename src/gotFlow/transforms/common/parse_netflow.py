#!/usr/bin/env python

from canari.config import config

# Python based netflow parser by Adam Maxwell (@catalyst256)

# nfdump -r [file] -b
# Date first seen     Duration Proto  Src IP Addr:Port       Dst IP Addr:Port Out Pkt In Pkt Out Byte In Byte Flows
# 2014-09-07 21:44:11.312 0.000 TCP 192.168.251.92:52953 <-> 50.31.164.215:80   0       0       0       8920    3
# ['2014-09-09', '05:54:03.852', '0.000', 'TCP', '192.168.251.219:45441', '<->', '192.30.252.129:22', '0', '0', '0', '5978', '3']

import subprocess


def parse_netflow(flow):
    try:
        nfdump = config['netflow/nfdump'].strip('\'')
        real_flows = []
        flows = subprocess.check_output([nfdump, '-r', flow])
        f = flows.split('\n')
        c = len(f) - 5
        f = f[1:c]
        for i in f:
            i = i.split(' ')
            a = [x for x in i if x != '']
            real_flows.append(a)
        return real_flows
    except Exception as e:
        return str(e)