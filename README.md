# Welpy <a href="https://github.com/Yakiyo/welpy"><img src="https://img.shields.io/github/stars/Yakiyo/welpy?style=social"></a> 

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?https://github.com/Yakiyo/welpy)

Generating dynamic welcome images with user avatars in [Carl-bot](https://carl.gg)'s welcome messages.

Carl bot is a great bot with tons of features, but it lacks the ability to generate welcome messages with a custom image with the user avatar. To resolve this issue in the [Tsurekano Discord Server](https://discord.gg/q2zDU5bGnh), I made a [custom bot](https://github.com/Yakiyo/Yume-bot) but with [Heroku](https://www.heroku.com) closing their free trial, the bot was shut down. So in response to that, I created welpy, a REST api with python and Pillow that generates dynamic images with user avatars.
This is only available for the Tsurekano Discord Server and since the image is hardcoded, I don't believe it can be used anywhere else anyway.
For self hosting please refer to [this](#self-hosting) section.

## Usage
Make a get request with a `id` param specifying the user's discord id

`GET /img?id=012345678912345678`

**Returns:** `image/png`

On any error, it just returns the base [empty image](./assets/welcome.jpg) since it is not possible to customize carl bot from the user end to handle errors.

## Self-Hosting
Its pretty straight forward and works in a simple manner. The entry point is [main.py](./main.py) where it handles the incoming http requests. On a `GET` request to the `img` endpoint, it takes the `id` param and fetches info from discord on that user (see [fetch.py](./fetch.py)). It then passes the user info to the image constructing function (at [image.py](./image.py)) and does required modifications and returns the image.

### Steps
1) [**Fork**](https://github.com/Yakiyo/welpy/fork) this repo.
2) Replace [**welcome.png**](./assets/welcome.png) with your background image.
3) With a bit of python knowledge, you can fiddle around with [**image.py**](./image.py) and make the image show up as you want. If you don't know enough python, you can use a image thats similar to the current image so that even if the avatar shows up in the same spot, it looks cool. Or just put some effort and learn python. Its pretty cool and you can flex to your friends.
4) Create a file named `.env` and add a discord bot token, this is required for making requests to discord.
```env
DISCORD_TOKEN=your-token-here
```
5) Deploy your app to someplace like [**Deta**](https://deta.sh). Install the deta cli and run the following commands in your terminal
```
$ deta deploy # deploys to deta

$ deta update -e .env # loads env vars from `.env` file
```
You can alternatively click on the "Deploy to Deta" button [here](#welpy-), which makes the steps simpler.

Read more on deploying to deta [here](https://docs.deta.shdocs/micros/getting_started).

## Demo Usage
```
https://welpy.deta.dev/img?id=695307292815654963
```
<img width="500px" src="https://welpy.deta.dev/img?id=695307292815654963">


## Author
**welpy** © [Yakiyo](https://github.com/Yakiyo). Authored and maintained by Yakiyo.

Released under [MIT](https://opensource.org/licenses/MIT) License
