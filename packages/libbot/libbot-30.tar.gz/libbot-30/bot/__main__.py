# This file is placed in the Public Domain.
#
# pylint: disable=C0412,C0115,C0116,W0212,R0903,C0207,C0413,W0611
# pylint: disable=C0411,E0402,E0611,C2801


"runtime"


import getpass
import importlib
import os
import pwd
import readline
import shutil
import sys
import termios
import time
import threading
import traceback


sys.path.insert(0, os.getcwd())


from bot.spec import Broker, Censor, Cfg, Client, Errors, Event
from bot.spec import Object, CLI, Handler, Storage, keys
from bot.spec import command, cprint, fmt, daemon, debug, parse, scan, forever
from bot.spec import launch, mods, name, privileges, shutdown, spl, update


import bot.modules

Censor.output = print
Storage.wd = Cfg.wd


class Console(CLI):

    def dispatch(self, evt):
        parse(evt)
        command(evt)
        evt.wait()

    def poll(self) -> Event:
        return self.event(input("> "))


def scandir(path, modnames, init=False):
    mns = []
    if not os.path.exists(path):
        return mns
    pname = path.split(os.sep)[-1]
    for fnm in os.listdir(path):
        if fnm.startswith("__"):
            continue
        if not fnm.endswith(".py"):
            continue
        fnn = fnm[:-3]
        fqn = f"{pname}.{fnn}"
        mod = importlib.import_module(fqn, pname)
        mns.append(fqn)
        Storage.scan(mod)
        Handler.scan(mod)
        if init and "init" in dir(mod):
            try:
                mod.init()
            except Exception as ex:
                Errors.add(ex)
    return mns


def wrap(func) -> None:
    old = None
    try:
        old = termios.tcgetattr(sys.stdin.fileno())
    except termios.error:
        pass
    try:
        func()
    except (EOFError, KeyboardInterrupt):
        print("")
        sys.stdout.flush()
    finally:
        if old:
            termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old)


def main():
    parse(Cfg, " ".join(sys.argv[1:]))
    update(Cfg, Cfg.sets)
    Cfg.mod = ",".join(bot.modules.__dir__())
    if Cfg.wd:
        Storage.wd = Cfg.wd
    if Cfg.md:
        scandir(Cfg.md, Cfg.mod, "x" not in Cfg.opts)
        Cfg.mod += "." + ",".join(mods(Cfg.md))
    if "v" in Cfg.opts:
        dtime = time.ctime(time.time()).replace("  ", " ")
        cprint(f"{Cfg.name.upper()} started at {dtime} {fmt(Cfg)}")
    if "n" in Cfg.opts:
        Cfg.commands = False
    if "d" in Cfg.opts:
        daemon(Cfg.pidfile)
    if "d" in Cfg.opts or "s" in Cfg.opts:
        privileges(Cfg.user)
        scan(bot.modules, Cfg.mod, True)
        forever()
    elif "c" in Cfg.opts:
        if "w" in Cfg.opts:
            for thr in thrs:
                thr.join()
                cprint(f"ready {thr.name}")
        scan(bot.modules, Cfg.mod, True)
        csl = Console()
        csl.start()
        csl.forever()
    else:
        scan(bot.modules, Cfg.mod)
        cli = Console()
        evt = cli.event(Cfg.otxt)
        parse(evt)
        command(evt)
        evt.wait()


def wrapped():
    wrap(main)


if __name__ == "__main__":
    wrapped()
