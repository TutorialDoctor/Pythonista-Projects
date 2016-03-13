# coding: utf-8
from __future__ import print_function
from scene import *
import sound

class MyScene(Scene):
	def __init__(self):
		Scene.__init__(self)
		# create a label node with text '0' and font 'Fira Mono', whose parent is 'self'(the current scene)
		self.timelabel=LabelNode('0',('Hoefler Text',100),parent=self,color='#ff5555')
		# set the label's postion
		self.timelabel.position = (self.size.w/2,self.size.h)
	def setup(self):
		pass
	def update(self):
		# set the time label's text to the time in seconds that has passed since the scene was started (scene.Scene.t)
		self.timelabel.text= str(len(self.touches))+' touches'
		
		# update the label's position so that it stays centered
		self.timelabel.position = (self.size.w/2,self.size.h-64)
	def pause(self):
		pass
	def resume(self):
		pass
	def stop(self):
		pass
	def touch_began(node,touch):
		# just playing a sound effect on every beginning touch event.
		sound.play_effect('8ve:8ve-tap-mellow')
	def touch_ended(node,touch):
		pass
	def touch_moved(node,touch):
		pass
	def did_change_size(self):
		pass
	def did_evaluate_actions(self):
		pass

game = MyScene()
if __name__=='__main__':
	run(game)