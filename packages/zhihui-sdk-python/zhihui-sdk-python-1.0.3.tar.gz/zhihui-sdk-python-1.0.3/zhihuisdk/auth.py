import hashlib
import hmac
import json
import time
import requests 
from urllib.parse import urlencode, quote

from typing import Dict

def sig_code(params, key): 
    key = str(key)
    key = key.encode('utf-8')
    paramsSort = quote(urlencode(params)).encode('utf-8')
    signature = hmac.new(
        key,
        msg=paramsSort,
        digestmod=hashlib.sha256
    ).hexdigest()
    params["sig"] = signature
    return params


from typing import Dict, Any, Optional, List

class AuthOptions:
    def __init__(self, channel: str = "api", stamp: str = "apiUser"):
        self.channel = channel
        self.stamp = stamp

class SuccessResponse:
    def __init__(self, status_code: int, data: Dict[str, Any]):
        self.status_code = status_code
        self.data = data

class ErrorResponse:
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class Data:
    def __init__(self, access_token: str):
        self.access_token = access_token

def auth(app_id: str, app_key: str, options: Optional[List[AuthOptions]] = None) -> str:
    default_options = AuthOptions()

    if options:
        default_options = options[0]

    params = {
        "appid": app_id,
        "channel": default_options.channel,
        "stamp": default_options.stamp,
        "timestamp": int(round(time.time() * 1000))
    }

    params_map = {k: str(v) for k, v in params.items()}
    params_map = sig_code(params_map, app_key)
    body = json.dumps(params_map)
    api_url = "https://zhihui.qq.com/account/api/auth/token"
    resp = requests.post(api_url, headers={"Content-Type": "application/json"}, data=body)
    response = resp.json()
    # print(resp)
    if response.get('statusCode') != 200:
        print("Request Auth API Error:", resp.text)
        return "error"


    if response.get('statusCode') == 200:
        return response.get('data', {}).get('access_token', '')

    return "error"