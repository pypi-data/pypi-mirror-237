NAME

::

   LIBBOT - library to program bots


DESCRIPTION

::

   LIBBOT is a python3 library intended to be programmable in a
   static, only code, no popen, no user imports and no reading
   modules from a directory, way. 

   LIBBOT provides a demo bot, it can connect to IRC, fetch and
   display RSS feeds, take todo notes, keep a shopping list
   and log text. You can also copy/past the service file and run
   it under systemd for 24/7 presence in a IRC channel.


SYNOPSIS

::

   bot <cmd> [key=val] 
   bot <cmd> [key==val]
   bot [-c] [-d] [-v] [-i]


INSTALL

::

   $ pipx install libbot


USAGE

::

   default action is doing nothing

   $ bot
   $

   first argument is a command

   $ bot cmd
   cfg,cmd,dlt,dne,dpl,fnd,log,met,mod,mre,
   nme,pwd,rem,rss,sts,tdo,thr,ver

   starting a console requires an option

   $ bot -c
   >

   list of modules

   $ bot mod
   bsc,err,flt,irc,log,mod,rss,shp,sts,tdo,
   thr,udp

   start as daemon

   $ bot -d
   $ 

   add -v if you want to have verbose logging


CONFIGURATION

::

   irc

   $ bot cfg server=<server>
   $ bot cfg channel=<channel>
   $ bot cfg nick=<nick>

   sasl

   $ bot pwd <nsnick> <nspass>
   $ bot cfg password=<frompwd>

   rss

   $ bot rss <url>
   $ bot dpl <url> <item1,item2>
   $ bot rem <url>
   $ bot nme <url> <name>


COMMANDS

::

   cfg - irc configuration
   cmd - commands
   dlt - remove a user
   dne - mark todo as done
   dpl - sets display items
   fnd - find objects 
   log - log some text
   met - add a user
   mre - displays cached output
   nme - display name of a feed
   pwd - sasl nickserv name/pass
   rem - removes a rss feed
   rss - add a feed
   sts - show status
   tdo - add todo item
   thr - show the running threads


SYSTEMD

::

   replace "<user>" with the user running pipx


   [Unit]
   Description=library to program bots
   Requires=network.target
   After=network.target

   [Service]
   Type=simple
   User=<user>
   Group=<user>
   WorkingDirectory=/home/<user>/.bot
   ExecStart=/home/<user>/.local/pipx/venvs/libbot/bin/botd
   RemainAfterExit=yes

   [Install]
   WantedBy=multi-user.target


FILES

::

   ~/.bot
   ~/.local/bin/bot
   ~/.local/bin/botcmd
   ~/.local/bin/botd
   ~/.local/pipx/venvs/libbot/


AUTHOR

::

   botlib <botlib@proton.me>


COPYRIGHT

::

   LIBBOT is placed in the Public Domain.
