# Shelved 
until further notice 

# PyBrokenIRC Bridge
This is a WIP. Many plugins have been cut from this source tree. Plugins can be somebody else's problem.

## Installation

### Pre-requisites
* Python 3.8 or above - prefer the newest Python 3.x when available
* A Unix-like operating system: PyLink is actively developed on Linux only, so we cannot guarantee that things will work properly on other systems.

If you are a developer and want to help make PyLink more portable, patches are welcome.

### Installing from source

1) First, make sure the following dependencies are met:

    * Poetry (`pip install poetry`)
    
2) Clone the repository: `git clone git@github.com:paigeadelethompson/PyBrokenIRC.git && cd PyBrokenIRC`
    
3) Install PyLink using `poetry install` for local install or `poetry build && pip install dist/*.whl` and specify `--user` with pip to install to the user's local site; `mkdir -p ~/.local/ && python -m site` for more information about the `USER_SITE`.

#### Building with Dockerfile
`docker build -t paigeadelethompson/PyBrokenIRC -t paigeadelethompson/PyBrokenIRC:latest . `



```bash
$ docker -it --rm run -v $(pwd)/config.yml:/config.yml:ro -v $(pwd)/pylink-data:/pylink-data paigeadelethompson/pybrokenirc
```

## More Information
Documentation is available in the Wiki: [https://github.com/paigeadelethompson/PyBrokenIRC/wiki](https://github.com/paigeadelethompson/PyBrokenIRC/wiki)
