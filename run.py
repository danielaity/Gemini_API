import requests
import json
import base64
import hmac
import hashlib
import datetime, time

api_key = ''
api_secret = ''.encode()

def getBalances():
    t = datetime.datetime.now()
    payload_nonce = str(int(time.mktime(t.timetuple())*1000))
    payload = {'request': '/v1/balances', 'nonce': payload_nonce}
    encoded_payload = json.dumps(payload).encode()
    b64 = base64.b64encode(encoded_payload)
    signature = hmac.new(api_secret, b64, hashlib.sha384).hexdigest()

    resp = requests.post(
        url = 'https://api.gemini.com/v1/balances',
        headers = {
            'Content-Type': 'text/plain',
            'Content-Length': '0',
            'X-GEMINI-APIKEY': api_key,
            'X-GEMINI-PAYLOAD': b64,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': 'no-cache'
        }
    )
    
    return resp.json()

print(getBalances())
