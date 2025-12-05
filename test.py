import requests
import uuid

payload = {
    "jsonrpc": "2.0",
    "id": str(uuid.uuid4()),
    "method": "sum",
    "params": [1, 2]
}

resp = requests.post("http://localhost:8545/rpc", json=payload)
print(resp.json())
