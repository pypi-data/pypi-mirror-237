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
product_id = "PD/MSA/PSP-v1.0"

nps = neuropacs.init(api_key, server_url)

# PRINT CURRENT VERSION
version = nps.PACKAGE_VERSION
print(version)

#GENERATE AN AES KEY
aes_key = npcs.generate_aes_key()

#CONNECT TO NEUROPACS
connection_id = npcs.connect(api_key,aes_key)

#CREATE A NEW JOB
order_id = npcs.new_job(connection_id, aes_key)

#UPLOAD AN IMAGE
npcs.upload("your_image_path",connection_id, order_id, aes_key)

#START A JOB
job_status = npcs.run_job(connection_id, aes_key, product_id, order_id)
```
