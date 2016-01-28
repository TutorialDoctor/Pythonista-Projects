# coding: utf-8

import ui
from objc_util import *
UIScreen = ObjCClass('UIScreen')

v = ui.load_view()
v.present('sheet',hide_title_bar=True)
	
def main():
	screen = UIScreen.mainScreen()
	while v.on_screen:
		screen.setBrightness_(v['view1']['slider1'].value)

if __name__ == '__main__':
	main()