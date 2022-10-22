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
	if 'message' in res:
		return None

	user = {
		'name': f'{res["username"]}#{res["discriminator"]}',
		'avatar': f'https://cdn.discordapp.com/avatars/{res["id"]}/{res["avatar"]}.png?size=1024'
	}
	if res['avatar'] is None:
		user['avatar'] = 'https://cdn.discordapp.com/embed/avatars/4.png'

	return user
