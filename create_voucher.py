import requests

ADDON_API_KEY = ''
ADDON_API_URL = 'https://addon.to/tools/api.php'
ADDON_API_AGENT = 'addon.to-beta-api - request v1.0'

headers = { 
	'User-agent': ADDON_API_AGENT
}

data = { 
	'apikey': ADDON_API_KEY,
	'action': 'create_voucher',
	'value': '1550'
}

data = requests.post(ADDON_API_URL, data=data, headers=headers)

print(data.text)