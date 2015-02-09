#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'Adam Maxwell'
__copyright__ = 'Copyright 2015, Gotflow Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Adam Maxwell'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'GotflowEntity',
    'MyGotflowEntity'
]

class GotflowEntity(Entity):
    _namespace_ = 'gotFlow'


# @EntityField(name='gotFlow.fieldN', propname='fieldN', displayname='Field N', matchingrule=MatchingRule.Loose)
# @EntityField(name='gotFlow.field1', propname='field1', displayname='Field 1', type=EntityFieldType.Integer)
# class MyGotflowEntity(GotflowEntity):
#     pass


class Folder(GotflowEntity):
    pass


class DumpFile(GotflowEntity):
    pass

class Port(GotflowEntity):
    pass