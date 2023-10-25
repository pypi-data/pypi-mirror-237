# This file is placed in the Public Domain.
#
# pylint: disable=E0402,C0115,R0902,R0903,W0201


"configuration"


import getpass
import os
import time


from .object import Default


def __dir__():
    return (
            'Config',
            'Cfg'
           )


class Config(Default):

    pass


Cfg = Config()
Cfg.commands  = True
Cfg.name      = __file__.split(os.sep)[-2].lower()
Cfg.workdir   = os.path.expanduser(f"~/.{Cfg.name}")
Cfg.pidfile   = os.path.join(Cfg.workdir, f"{Cfg.name}.pid")
Cfg.starttime = time.time()
Cfg.user      = getpass.getuser()
