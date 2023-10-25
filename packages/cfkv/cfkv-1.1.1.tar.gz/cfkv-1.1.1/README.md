# CFKV

[![Deploy > PYPI > Test ](https://github.com/mooncitizen/python-cfkv/actions/workflows/testpypi.yaml/badge.svg)](https://github.com/mooncitizen/python-cfkv/actions/workflows/testpypi.yaml)

[![Release](https://github.com/mooncitizen/python-cfkv/actions/workflows/pypi.yaml/badge.svg)](https://github.com/mooncitizen/python-cfkv/actions/workflows/pypi.yaml)

A simple wrapper to communicate with [Cloudflare KV Store ](https://developers.cloudflare.com/kv/). It can be used as a cache and features will be implemented to be used in frameworks such as ```FastAPI```

- [x] Set and Get
- [ ] Fastapi Middleware
- [ ] Flask integration
- [x] Options to include string instead of dict entry

### Simple Usage

```python
import datetime
from cfkv import KVStore

store = KVStore(namespace_id="YOUR_NAMESPACE_ID", account_id="ACCOUNT_ID", api_key="API_KEY")

# Usage Example
key = "sample_key"
get = store.get(key)

if get is None:
    data = {"test": True, "date": str(datetime.datetime.now())}
    store.set(key)
    data['stored'] = False
    get = data
else:
    data['stored'] = True

print(get)
```

### Setup

You will need to know your namespace id which is generated when you create a KV namespace and Account ID. To generate the KV api key follow the instructions below

1. Navigate to [Cloudflare API Tokens](https://dash.cloudflare.com/profile/api-tokens)
2. Create API Token
3. Scroll down to create custom token
4. Create a token with **Workers KV Storage** and select **Edit**

![Example Token](github/image.png)

You can use environment variables to store these the following are monitored
```python
KV_NAMESPACE_ID="YOUR_NAMESPACE_ID"
CF_ACCOUNT_ID="YOUR_ACCOUNT_ID"
CF_API_KEY="YOUR_API_KEY"
```