import requests
import json
import time
import datetime

def get_data():
    url = 'https://collections.rarity.tools/upcoming2'
    headers = {
        'Referer': 'https://rarity.tools/', 'content-type': 'application/json',
        'pragma': 'no-cache',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Origin': 'https://rarity.tools'
    }
    reponse = requests.get(url, headers=headers)
    cnt = 0 
    while reponse.status_code!=200:
        cnt = cnt + 1
        time.sleep((cnt * cnt + 1))
        reponse = requests.get(url, headers=headers)
        if cnt > 7:
            return None
    jsonn = json.loads(reponse.text)
    return jsonn


