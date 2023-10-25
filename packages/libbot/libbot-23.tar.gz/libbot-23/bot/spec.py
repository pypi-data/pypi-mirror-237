# This file is placed in the Public Domain.
#
# pylint: disable=W0611,W0614,W0401,E0402,E0611


"the python3 bot namespace"


from .all     import *
from .broker  import *
from .config  import *
from .client  import *
from .error   import *
from .find    import *
from .handler import *
from .event   import *
from .func    import *
from .object  import *
from .parse   import *
from .scan    import *
from .disk    import *
from .thread  import *
from .timer   import *
from .utils   import *


def __dir__():
    return (
            'Broker',
            'Censor',
            'Cfg',
            'Client',
            'CLI',
            'Console',
            'Default',
            'Errors',
            'Event',
            'Handler',
            'Object',
            'Repeater',
            'Storage',
            'Thread',
            'cdir',
            'command',
            'construct',
            'edit',
            'fetch',
            'find',
            'fntime',
            'fqn',
            'ident',
            'items',
            'keys',
            'laps',
            'last',
            'launch',
            'mods',
            'name',
            'parse',
            'read',
            'scan',
            'search', 
            'shutdown',
            'spl',
            'strip',
            'sync',
            'update',
            'values',
            'write'
           )
