# NeuroPACS Python SDK

## Install neuropacs from pip

```bash
pip install neuropacs
```

## Usage

```py
import neuropacs

api_key = "user_api_key"
server_url = "https://your_neuropacs_url"

nps = neuropacs.init(api_key, server_url)

version = nps.PACKAGE_VERSION
print(version)
```
