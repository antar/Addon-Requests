import requests

ADDON_API_KEY = ''
ADDON_API_URL = 'https://addon.to/tools/api.php'
ADDON_API_AGENT = 'addon.to-beta-api - request v1.0'

headers = { 
	'User-agent': ADDON_API_AGENT
}

data = { 
	'apikey': ADDON_API_KEY,
	'action': 'twitch_service',
	'twitch_channel': 'name',
	'twitch_group': '3', # make a request with 0 to get a group list
	'twitch_message': 'hello',
	'twitch_action': '2' # 1 random , 2 static msg , 3 addon raid, 4 unique chat bypass
}

data = requests.post(ADDON_API_URL, data=data, headers=headers)

print(data.text)
