from ui import *

 
#FUNCTIONS
#Gets the center of a view
def Get_Center(vw):
	center = (vw.width/2,vw.height/2)
	return center

#Sets the top center of a view to a touch location
def Move_To_Location(vw,evt):
	vw.x = evt.location[0]-(vw.width/2)
	vw.y = evt.location[1]

def reset(obj,x=0,y=0,width=100,height=100):
	obj.x=Get_Center(main_window)[0]
	obj.y=Get_Center(main_window)[1]
	obj.width=width
	obj.height=height

class ViewClass(View):
	def __init__(self):
		pass
	
	def touch_began(self,touch):
		window.width = touch.location[0]
		window.height = touch.location[1]
	
	def touch_moved(self,touch):
		window.width = touch.location[0]
		window.height = touch.location[1]
	
	def touched_ended(self,touch):
		#window.width = touch.location[0]
		#window.height = touch.location[1]
		pass


main_window = load_view()
window = main_window['window']
reset(window,height=246,width=246)
main_window.present('fullscreen')

