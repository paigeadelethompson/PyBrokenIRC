# PyLink

PyLink is an extensible, plugin-based IRC services framework written in Python. It aims to be:

1) a replacement for the now-defunct Janus.

2) a versatile framework and gateway to IRC.

## Support

Please report any bugs you find to the [issue tracker](https://github.com/GLolol/PyLink/issues). Pull requests are open if you'd like to contribute, though new stuff generally goes to the **devel** branch.

You can also find support via our IRC channels: `#PyLink @ irc.overdrivenetworks.com `([webchat](https://webchat.overdrivenetworks.com/?channels=PyLink,dev)) or `#PyLink @ chat.freenode.net`. Ask your questions and be patient for a response.

## Dependencies

* Python 3.4+
* PyYAML (`pip install pyyaml`)
* *For the servprotect plugin*: [expiringdict](https://github.com/mailgun/expiringdict) (note: unfortunately, installation is broken in pip due to [mailgun/expiringdict#13](https://github.com/mailgun/expiringdict/issues/13))
* *For the changehost and opercmds plugins*: [ircmatch](https://github.com/mammon-ircd/ircmatch) (`pip install ircmatch`)

## Supported IRCds

### Primary support

These IRCds are frequently tested and well supported. If any issues occur, please file a bug on the issue tracker.

* charybdis (3.5.x / git master) - module `ts6`
* InspIRCd 2.0.x - module `inspircd`
* UnrealIRCd 4.x - module `unreal`
    - Note: Support for mixed UnrealIRCd 3.2/4.0 networks is experimental, and requires you to enable a `mixed_link` option in the configuration. This may in turn void your support.

### Extended support

Support for these IRCds exist, but are not tested as frequently and thoroughly. Bugs should be filed if there are any issues, though they may not be always be fixed in a timely fashion.

* Elemental-IRCd (6.6.x / git master) - module `ts6`
* InspIRCd 2.2 (git master) - module `inspircd`
* IRCd-Hybrid (8.2.x / svn trunk) - module `hybrid`
    - Note: for host changing support and optimal functionality, a `service{}` block / U-line should be added for PyLink on every IRCd across your network.

## Setup

1) Rename `example-conf.yml` to `config.yml` and configure your instance there. Note that the configuration format isn't finalized yet - this means that your configuration may break in an update!

2) Run `./pylink` from the command line.

3) Profit???
