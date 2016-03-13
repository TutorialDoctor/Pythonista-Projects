# coding: utf-8
from __future__ import print_function
from scene import *
import sound,random

class MyScene(Scene):
	def __init__(self):
		Scene.__init__(self)
		self.create_label()
		self.sprites = []
	def setup(self):
		pass
	def update(self):
		self.counterlabel.text = str(gravity())
		self.counterlabel.position = (self.size.w/2,self.size.h-32)
	def pause(self):
		pass
	def resume(self):
		pass
	def stop(self):
		print(str(len(self.sprites))+' sprites in the scene')
		print(self.sprites)
	def touch_began(node,touch):
		node.create_sprite(node.get_random_item(),touch.location)
		node.create_sprite('emj:Gem_Stone',touch.location+(64,0))
		node.create_sprite('emj:Gem_Stone',touch.location+(-64,0))
		node.create_sprite('emj:Gem_Stone',touch.location+(0,64))
		node.create_sprite('emj:Gem_Stone',touch.location+(0,-64))
	def touch_ended(node,touch):
		pass
	def touch_moved(node,touch):
		pass
	def did_change_size(self):
		pass
	def did_evaluate_actions(self):
		pass
	
	def create_label(self):
		# create a label node with text '0' and font 'Fira Mono', whose parent is 'self'(the current scene)
		self.counterlabel=LabelNode('0',('Hoefler Text',22),parent=self,color='#ff5555')
		# set the label's postion
		self.counterlabel.position = (self.size.w/2,self.size.h-32)
	
	def create_sprite(self,i,p):
		"""Creates a sprite with image i at position p and appends it to an array of sprites"""
		sprite=SpriteNode(i,parent=self,position=p)
		self.sprites.append(sprite)
		
	def get_random_item(self):
		choices = ['emj:Raised_Hand','emj:Raised_Hands','emj:Raised_Fist']
		random_choice = random.choice(choices)
		if random_choice==choices[0]:
			sound.play_effect('ui:switch38')
			return choices[0]
		elif random_choice==choices[1]:
			sound.play_effect('ui:switch23')
			return choices[1]
		elif random_choice==choices[2]:
			sound.play_effect('ui:switch18')
			return choices[2]
		else:
			None
game = MyScene()
if __name__=='__main__':
	run(game)