from os import getenv
from flask import Flask, request
from dotenv import load_dotenv
from image import create_image
from fetch import fetch

load_dotenv()

app = Flask("welpy")


@app.route("/")
def hello_world():
    return {
		"msg": 'https://github.com/Yakiyo/welpy',
		"status": 200
	}


@app.get("/img")
def handle():
    id = request.args.get("id", None)
    # Returns empty image if user or id is none, else the proper image
	# this is because it is not possible to handle errors on carl bot
	# from the user side. Thus why, just return the empty image if
	# anything goes wrong.
	# TODO: Log error using a discord webhook
    return create_image(fetch(id))


# Only run on local testing, since Deta for some
# reason times out if its turned on on micros too
if not getenv("DETA_RUNTIME"):
    app.run()
