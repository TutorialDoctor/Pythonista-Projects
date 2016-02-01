# coding: utf-8
# TRIAL AND ERROR
import ui,photos,random

# testing my logic for the gallery:
print [i for i in range(0,100) if i <= 30]

main_view = ui.load_view('Views/gallery')
im = ui.ImageView()
im.image = ui.Image().named('iob:flash_off_256')


[main_view.add_subview(ui.ImageView()) for i in range(0,10)]
# gotta increment x


"""
# Checking to see if they were added:
i=0
for sub in main_view.subviews:
	sub.name = 'imageview'+str(i)
	sub.image = ui.Image().named('pzl:Blue1')
	if i%2==0:
		print sub.name
	i+=1

main_view.present()

init = 0
while init < main_view.width-900:
	for sub in main_view.subviews:
		sub.image = ui.Image().named('emj:Alien')
		sub.x=init
		init=init+1
t=0		
for x in main_view.subviews:
	t+=1
	if t%2==0:
		main_view.subviews[t-1].x +=40
"""

# GETTING THERE!!!!
d=0
ims=['emj:Alien','emj:Angry','emj:Anger_Symbol','emj:Alien_Monster','emj:Ambulance','emj:Airplane','emj:Artist_Palette','emj:Anchor']
main_view.present()
print main_view.subviews
for i in range(len(main_view.subviews)):
	main_view.subviews[i].image = ui.Image().named(random.choice(ims))
	if i!=0:
		main_view.subviews[i].x=main_view.subviews[i-1].x+200

	
	

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