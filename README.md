# PyBrokenIRC Bridge
This is a WIP. Many plugins have been cut from this source tree. Plugins can be somebody else's problem.

## Installation

### Pre-requisites
* Python 3.7 or above - prefer the newest Python 3.x when available
* A Unix-like operating system: PyLink is actively developed on Linux only, so we cannot guarantee that things will work properly on other systems.

If you are a developer and want to help make PyLink more portable, patches are welcome.

### Installing from source

1) First, make sure the following dependencies are met:

    * Poetry (`pip3 install poetry`)
    
2) Clone the repository: `git clone git@github.com:paigeadelethompson/PyBrokenIRC.git && cd PyBrokenIRC`
    
3) Install PyLink using `poetry install` for local install or `poetry build && pip install dist/*.whl` and specify `--user` with pip to install to the user's local site; `mkdir -p ~/.local/ && python -m site` for more information about the `USER_SITE`.

#### Building with Dockerfile
`docker build -t PyBrokenIRC -t PyBrokenIRC:latest . `



```bash
$ docker run -v $HOME/pylink:/pylink jlu5/pylink
```

## More Information
Documentation is available in the Wiki: [https://github.com/paigeadelethompson/PyBrokenIRC/wiki](https://github.com/paigeadelethompson/PyBrokenIRC/wiki)
