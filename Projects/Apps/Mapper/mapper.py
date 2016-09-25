import ui

def function(sender):
	map=ui.load_view('map')
	im=map['scrollview']['image']
	im.image=ui.Image('IMG_0075.JPG')
	im.frame=(0,0,2000,2000)
	map.present('sheet')

v = ui.load_view()
logo=v['logo']
logo.image=ui.Image('IMG_0074.PNG')
btn=v['button']
btn.action = function
v.present(hide_title_bar=True)
