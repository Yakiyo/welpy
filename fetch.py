from requests import get
from os import getenv

# Fetch a user from discord
def fetch(id):
	if id is None:
		return None
	heads = {
		'Accept': "application/json",
		'Authorization': f'Bot {getenv("DISCORD_TOKEN")}'
	  }
	res = get(f'https://discord.com/api/users/{id}', headers=heads).json()
	if 'message' in res and res['message'] == 'Unknown User':
		return None
	return {
		'name': f'{res["username"]}#{res["discriminator"]}',
		'avatar': f'https://cdn.discordapp.com/avatars/{res["id"]}/{res["avatar"]}.png?size=1024'
	}
