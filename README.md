# Crafty-Client

## OLD VERSION ALERT!

Our development is now focused on Gitlab, please check out this repository over there!  
https://gitlab.com/crafty-controller/crafty-client

## About

Crafty Client is a pypi (pip) package for interfacing with the [Crafty Web MC server control panel](https://gitlab.com/crafty-controller/crafty-web).

It was written from scratch and is based on requests and urllib3, by [kevdagoat](https://gitlab.com/kevdagoat)

## Install

Make sure you have python3 installed on your system with the pip package manager.

#### For windows (conda) environments
```bash
pip install crafty-client
```

#### For linux (apt/yum/rpm/etc.) environments
```bash
pip3 install crafty-client
```

## Usage

Example:
```python
from crafty_client import CraftyWeb

URL = "https://127.0.0.1:8000"    # The location of the crafty-web webserver
API_TOKEN = "<place token here>"  # Your crafty Web API token, printed in the console at installation.

cweb = CraftyWeb(URL, API_TOKEN)

print(cweb.list_mc_servers())
```
