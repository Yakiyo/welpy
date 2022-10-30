from io import BytesIO
from requests import get
from flask import Response
from PIL import Image, ImageOps, ImageFont, ImageDraw

def create_image(user):
	img = Image.open('./assets/welcome.png')
	buffer = BytesIO()

	# Return the empty image when user is None for whatever reason may it be
	if user is None:
		img.save(buffer, format='PNG', quality=90)
		buffer.seek(0)
		return Response(buffer, headers={'Cache-Control': 'no-cache'}, mimetype='image/jpg', status=200)

	# Paste the avatar
	av = Image.open(get(user["avatar"], stream=True, timeout=5).raw)
	av = ImageOps.fit(av, (600, 600)).convert('RGBA')
	img.paste(av, (250, 550))

	# TODO: Make circular avatar
	# l_img = Image.new('L', [600, 600], 0)
	# dl = ImageDraw.Draw(l_img)
	# dl.pieslice([(0,0), [600, 600]], 0, 360, fill=255)

	# Set font
	fsize = 80
	font = ImageFont.truetype('./assets/Poppins-Bold.ttf', fsize)

	# Write username
	d = ImageDraw.Draw(img)
	# mid point of text should be 550
	name = user['name']
	tw = d.textsize(name, font=font)[0]
	# If text size goes more than 900 px, create a loop
	# and keep reducing the font size by 3 px until text
	# becomes equal or less than 900px
	while tw > 800:
		fsize -= 3
		font = ImageFont.truetype('./assets/Poppins-Bold.ttf', fsize)
		tw = d.textsize(name, font=font)[0]

	# Centers the text at a specific point, so half of the text is on both side of that point
	d.text((550 - tw / 2, 1200), name, font=font, fill='#00b9bd')
	# draw rectangular border around av
	d.rounded_rectangle([(250, 550), (850, 1150)], radius=5, width=7, outline='#00b9bd')

	img.save(buffer, format='PNG', quality=90)
	buffer.seek(0)
	img.close()
	return Response(buffer, headers={'Cache-Control': 'no-cache'}, mimetype='image/png', status=200)
