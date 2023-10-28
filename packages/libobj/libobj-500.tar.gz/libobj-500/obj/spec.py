# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611,W0622


"specifications"


from .all     import *
from .disk    import *
from .func    import *
from .find    import *
from .object  import *


def __dir__():
    return (
            'Default',
            'Object',
            'Storage',
            'construct',
            'edit',
            'fetch',
            'find',
            'fntime',
            'fqn',
            'ident',
            'items',
            'keys',
            'last',
            'name',
            'read',
            'search', 
            'sync',
            'update',
            'values',
            'write'
           )


__all__ = __dir__()
