import requests

ADDON_API_KEY = ''
ADDON_API_URL = 'https://addon.to/tools/api.php'
ADDON_API_AGENT = 'addon.to-beta-api - request v1.0'

headers = { 
	'User-agent': ADDON_API_AGENT
}

data = { 
	'apikey': ADDON_API_KEY,
	'action': 'send_points',
	'value': '500',
	'to_user_id': '1',
	'description': 'test_123' # Optional not needed
}

data = requests.post(ADDON_API_URL, data=data, headers=headers)

print(data.text)