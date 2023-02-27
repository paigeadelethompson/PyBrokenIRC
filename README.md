# Figaro IRC bridge
This is a WIP. Many plugins have been cut from this source tree. Plugins can be somebody else's problem.

## Installation

### Pre-requisites
* Python 3.7 or above - prefer the newest Python 3.x when available
* A Unix-like operating system: PyLink is actively developed on Linux only, so we cannot guarantee that things will work properly on other systems.

If you are a developer and want to help make PyLink more portable, patches are welcome.

### Installing from source

1) First, make sure the following dependencies are met:

    * Setuptools (`pip3 install setuptools`)
    * PyYAML (`pip3 install pyyaml`)
    * cachetools (`pip3 install cachetools`)
    * *For hashed password support*: Passlib >= 1.7.0 (`pip3 install passlib`)
    * *For Unicode support in Relay*: unidecode (`pip3 install Unidecode`)
    * *For extended PID file tracking (i.e. removing stale PID files after a crash)*: psutil (`pip3 install psutil`)

2) Clone the repository: `git clone https://github.com/PyLink/PyLink && cd PyLink`
    - Previously there was a *devel* branch for testing versions of PyLink - this practice has since been discontinued.

3) Install PyLink using `python3 setup.py install` (global install) or `python3 setup.py install --user` (local install)
    * Note: `--user` is a *literal* string; *do not* replace it with your username.
    *  **Whenever you switch branches or update PyLink's sources via `git pull`, you will need to re-run this command for changes to apply!**

### Installing via Docker

As of PyLink 3.0 there is a Docker image available on Docker Hub: [jlu5/pylink](https://hub.docker.com/r/jlu5/pylink)

It supports the following tags:

- Rolling tags: **`latest`** (latest stable/RC release), **`latest-beta`** (latest beta snapshot)
- Pinned to a major branch: e.g. **`3`** (latest 3.x stable release), **`3-beta`** (latest 3.x beta snapshot)
- Pinned to a specific version: e.g. **`3.0.0`**

To use this image you should mount your configuration/DB folder into `/pylink`. **Make sure this directory is writable by UID 10000.**

```bash
$ docker run -v $HOME/pylink:/pylink jlu5/pylink
```

### Installing via PyPI (stable branch only)

1) Make sure you're running the right pip command: on most distros, pip for Python 3 uses the command `pip3`.

2) Run `pip3 install pylinkirc` to download and install PyLink. pip will automatically resolve dependencies.

3) Download or copy https://github.com/PyLink/PyLink/blob/master/example-conf.yml for an example configuration.

## Configuration

1) Rename `example-conf.yml` to `pylink.yml` (or a similarly named `.yml` file) and configure your instance there.

2) Run `pylink` from the command line. PyLink will load its configuration from `pylink.yml` by default, but you can override this by running `pylink` with a config argument (e.g. `pylink mynet.yml`).

## Supported IRCds

### Primary support

These IRCds (in alphabetical order) are frequently tested and well supported. If any issues occur, please file a bug on the issue tracker.

* [InspIRCd](http://www.inspircd.org/) (2.0 - 3.x) - module `inspircd`
    - Set the `target_version` option to `insp3` to target InspIRCd 3.x (default), or `insp20` to target InspIRCd 2.0 (legacy).
    - For vHost setting to work, `m_chghost.so` must be loaded. For ident and realname changing support, `m_chgident.so` and `m_chgname.so` must be loaded respectively.
    - Supported channel, user, and prefix modes are negotiated on connect, but hotloading modules that change these is not supported. After changing module configuration, it is recommended to SQUIT PyLink to force a protocol renegotiation.
* [Nefarious IRCu](https://github.com/evilnet/nefarious2) (2.0.0+) - module `p10`
    - Note: Both account cloaks (user and oper) and hashed IP cloaks are optionally supported (`HOST_HIDING_STYLE` settings 0 to 3). Make sure you configure PyLink to match your IRCd settings.
* [UnrealIRCd](https://www.unrealircd.org/) (4.2.x - 5.0.x) - module `unreal`
    - Supported channel, user, and prefix modes are negotiated on connect, but hotloading modules that change these is not supported. After changing module configuration, it is recommended to SQUIT PyLink to force a protocol renegotiation.

### Extended support

Support for these IRCds exist, but are not tested as frequently and thoroughly. Bugs should be filed if there are any issues, though they may not always be fixed in a timely fashion.

* [charybdis](https://github.com/charybdis-ircd/charybdis) (3.5+) - module `ts6`
    - For KLINE support to work, a `shared{}` block should be added for PyLink on all servers.
* [ChatIRCd](http://www.chatlounge.net/software) (1.2.x / git master) - module `ts6`
    - For KLINE support to work, a `shared{}` block should be added for PyLink on all servers.
* [juno-ircd](https://github.com/cooper/juno) (13.x / ava) - module `ts6` (see [configuration example](https://github.com/cooper/juno/blob/master/doc/ts6.md#pylink))
* [ngIRCd](https://ngircd.barton.de/) (24+) - module `ngircd`
    - For GLINEs to propagate, the `AllowRemoteOper` option must be enabled in ngIRCd.
    - `+` (modeless) channels are not supported, and should be disabled for PyLink to function correctly.
    - For use with Relay, the `CloakHostModeX` setting will work fine but `CloakHost` and `CloakUserToNick` are *not* supported.

### Legacy extended support

Support for these IRCds was added at some point but is no longer actively maintained, either due to inactive upstream development or a perceived lack of interest. We recommend migrating to an IRCd in the above two sections.

* [beware-ircd](http://ircd.bircd.org/) (1.6.3) - module `p10`
    - Because bircd disallows BURST after ENDBURST for regular servers, U-lines are required for all PyLink servers. Fortunately, wildcards are supported in U-lines, so you can add something along the lines of `U:<your pylink server>:` and `U:*.relay:` (adjust accordingly for your relay server suffix).
    - Use `ircd: snircd` as the target IRCd.
    - Halfops, `sethost` (`+h`), and account-based cloaking (`VHostStyle=1`) are supported. Crypted IPs and static hosts (`VHostStyle` 2 and 3) are NOT.
* [Elemental-IRCd](https://github.com/Elemental-IRCd/elemental-ircd) (6.6.x / git master) - module `ts6`
    - For KLINE support to work, a `shared{}` block should be added for PyLink on all servers.
* [IRCd-Hybrid](http://www.ircd-hybrid.org/) (8.2.x / svn trunk) - module `hybrid`
    - For host changing support and optimal functionality, a `service{}` block / U-line should be added for PyLink on every IRCd across your network.
    - For KLINE support to work, a `shared{}` block should also be added for PyLink on all servers.
* [ircd-ratbox](http://www.ratbox.org/) (3.x) - module `ts6`
    - Host changing is not supported.
    - On ircd-ratbox, all known IPs of users will be shown in `/whois`, even if the client is e.g. a cloaked relay client. If you're paranoid about this, turn off Relay IP forwarding on the ratbox network(s).
    - For KLINE support to work, a `shared{}` block should be added for PyLink on all servers.
* [IRCu](http://coder-com.undernet.org/) (u2.10.12.16+) - module `p10`
    - Host changing (changehost, relay) is not supported.
* [snircd](https://development.quakenet.org/) (1.3.x+) - module `p10`
    - Outbound host changing (i.e. for the `changehost` plugin) is not supported.

### Clientbot

PyLink supports connecting to IRCds as a relay bot and forwarding users back as virtual clients, similar to Janus' Clientbot. This can be useful if the IRCd a network used isn't supported, or if you want to relay certain channels without fully linking with a network.

For Relay to work properly with Clientbot, be sure to load the `relay_clientbot` plugin in conjunction with `relay`.

Note: **Clientbot links can only be used as a leaf for Relay links - they CANNOT be used to host channels!** This means that Relay does not support having all your networks be Clientbot - in those cases you are better off using a classic relay bot, like [RelayNext for Limnoria](https://github.com/jlu5/SupyPlugins/tree/master/RelayNext).
