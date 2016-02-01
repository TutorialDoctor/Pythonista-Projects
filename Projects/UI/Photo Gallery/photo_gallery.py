# coding: utf-8
# MORE TRIAL AND ERROR
import ui,photos,random
from PIL import Image

main_view = ui.load_view('Views/gallery')
scroll = main_view['scrollview1']
def photo_fill(view,amount,spacing=32,source=[],y_offset=0,exceptions=[]):
	view.content_size = (2000,2000)
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


# GETTING THERE!!!!
image_array=['emj:Alien','emj:Angry','emj:Anger_Symbol','emj:Alien_Monster','emj:Ambulance','emj:Airplane','emj:Artist_Palette','emj:Anchor','emj:Bath','emj:Bug']
roll_array = [photos.get_image(x,raw_data=True) for x in range(random.randint(0,100))]
excep = [scroll]
main_view.present()
photo_fill(scroll,20,100,exceptions=excep,source=roll_array,y_offset=100)