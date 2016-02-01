# coding: utf-8

"""
class Picture():
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y

pic = Picture()

for x in range(1000):
	if pic.x<view_length:
		pic.x+=30
		print (pic.x,pic.y)
	else:
		pic.x=0
		pic.y=pic.y+50
		print (pic.x,pic.y)
"""		
		
# coding: utf-8
# From test 5
import ui,photos,random
from PIL import Image

main_view = ui.load_view('Views/gallery')
scroll = main_view['scrollview1']

def photo_fill(view,amount,spacing=32,source=[],y_offset=0,exceptions=[]):
	[view.add_subview(ui.ImageView()) for i in range(amount)]
	view.content_size = (2000,2000)
	for i in range(100):
		for v in view.subviews:
			if v.x<1024:
				v.x+=50
				v.image = ui.Image().from_data(random.choice(source))
			else:
				v.x=0
				v.y=v.y+y_offset



# GETTING THERE!!!!
image_array=['emj:Alien','emj:Angry','emj:Anger_Symbol','emj:Alien_Monster','emj:Ambulance','emj:Airplane','emj:Artist_Palette','emj:Anchor','emj:Bath','emj:Bug']
roll_array = [photos.get_image(x,raw_data=True) for x in range(random.randint(0,100))]
excep = [scroll]
main_view.present()
photo_fill(scroll,20,100,exceptions=excep,source=roll_array,y_offset=100)