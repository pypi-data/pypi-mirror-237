# CFKV

[![Deploy > PYPI > Test ](https://github.com/mooncitizen/python-cfkv/actions/workflows/testpypi.yaml/badge.svg)](https://github.com/mooncitizen/python-cfkv/actions/workflows/testpypi.yaml)

[![Release](https://github.com/mooncitizen/python-cfkv/actions/workflows/pypi.yaml/badge.svg)](https://github.com/mooncitizen/python-cfkv/actions/workflows/pypi.yaml)

A simple wrapper to communicate with [Cloudflare KV Store ](https://developers.cloudflare.com/kv/). It can be used as a cache and features will be implemented to be used in frameworks such as ```FastAPI```

- [x] Set and Get
- [ ] Fastapi Middleware
- [ ] Flask integration
- [ ] Options to include string instead of dict entry

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