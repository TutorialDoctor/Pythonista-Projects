# KEY/LEGEND:
# evt:event
# anim:animation


import ui
from sound import *

# FUNCTIONS
#Gets the center of a view
def Get_Center(frame):
	center = (frame.width/2,frame.height/2)
	return center

#Sets the top center of a view to a touch location
def Move_To_Location(frame,evt):
	frame.x = evt.location[0]-(frame.width/2)
	frame.y = evt.location[1]


# A custom view class (inherits from the ui.View class)
class ViewClass(ui.View):
	def __init__(self):
		pass
	def touch_began(self,touch):
		Move_To_Location(window,touch)
		play_effect('Click_1')
		pass
	def touch_moved(self,touch):
		Move_To_Location(window,touch)
		pass
	def touch_ended(self,touch):
		play_effect('Crashing')
		Move_To_Location(window,touch)


# OBJECTS
main_view = ui.load_view()
window = main_view['window']
window.touch_enabled = False 
title = main_view['window']['title']


# DISPLAY IT
main_view.present('fullscreen')
