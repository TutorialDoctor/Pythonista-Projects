# coding: utf-8
# MORE TRIAL AND ERROR
import ui,photos,random
from PIL import Image

main_view = ui.load_view('Views/gallery')
scroll = main_view['scrollview1']


# GETTING THERE!!!!
image_array=['emj:Alien','emj:Angry','emj:Anger_Symbol','emj:Alien_Monster','emj:Ambulance','emj:Airplane','emj:Artist_Palette','emj:Anchor','emj:Bath','emj:Bug']
roll_array = [photos.get_image(x,raw_data=True) for x in range(0,9)]
excep = [scroll]
main_view.present()
offset=45
def fill(view,amount,spacing=32,source=[],y_offset=0,exceptions=[]):
	[view.add_subview(ui.ImageView()) for i in range(0,amount)]
	for i in range(len(view.subviews)):
		curr = view.subviews[i]
		prev = view.subviews[i-1]
		if curr not in exceptions:
			curr.y=y_offset
			curr.image = ui.Image().named(random.choice(source))
			if i!=0:
				if curr.x<view.width:
					curr.x=prev.x+spacing
			print (curr.x,curr.y)
fill(scroll,50,3,image_array,0)


def photo_fill(view,amount,spacing=32,source=[],y_offset=0,exceptions=[]):
	[view.add_subview(ui.ImageView()) for i in range(0,amount)]
	for i in range(len(view.subviews)):
		curr = view.subviews[i]
		prev = view.subviews[i-1]
		if curr not in exceptions:
			curr.y=y_offset
			curr.image = ui.Image().from_data(random.choice(source))
			if i!=0:
				if curr.x<view.width:
					curr.x=prev.x+spacing
			print (curr.x,curr.y)
photo_fill(main_view,10,exceptions=excep,source=roll_array,y_offset=100)
# How to load photos from the camera roll
#for x in range(photos.get_count()):
	#print photos.get_image(x)

# From cover_flow
def pil_to_ui(img):
	b = BytesIO()
	img.save(b, "PNG")
	data = b.getvalue()
	b.close()
	return ui.Image.from_data(data)