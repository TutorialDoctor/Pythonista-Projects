# coding: utf-8
from scene import *
import ui

class Game(Scene):
	def __init__(self,name=''):
		Scene.__init__(self)
		
		# CONSTANTS
		self.CENTER = (self.size.w/2,self.size.h/2)
		self.TOP_RIGHT = self.size
		self.BOTTOM_RIGHT = (self.size.w,0)
		self.TOP_LEFT = (0,self.size.h)
		self.BOTTOM_LEFT = (0,0)
		
		# PROPERTIES
		self.root = Node(parent=self)
		self.name = name
		self.gravity_enabled = True
	
	# BUILT-IN METHODS
	def setup(self):
		self.sprite= SpriteNode('plf:AlienBlue_front',position=newGame.CENTER)
		self.label = LabelNode('Alien Man')
		self.add_child(self.root)
		self.add_children([self.sprite,self.label])

	def update(self):
		self.label.position=self.sprite.position+(0,20)
		self.add_gravity(self.sprite)

	def pause(self):
		pass
	def resume(self):
		pass
	def stop(self):
		pass
	def touch_began(node,touch):
		pass
	def touch_ended(node,touch):
		pass
	def touch_moved(node,touch):
		pass
	def did_change_size(self):
		pass
	def did_evaluate_actions(self):
		pass
	
	# CUSTOM METHODS
	def get_node():
		pass
	
	def add_children(self,nodes):
		for node in nodes:
			self.root.add_child(node)
	
	#WIP traverse the node tree
	def get_children(self):
		for node in self.root.children:
			if node.children != None:
				print node.children
	
	def add_gravity(self,a):
		if self.gravity_enabled:
			g = gravity()
			if abs(g.x) > 0.05:
				x = a.position.x
				max_speed = 40
				x = max(0, min(self.size.w, x + g.x * max_speed))
				a.position = (x, 32)
		else:
			None


# Testing
newGame = Game('Alien Fall')
print newGame.name
print newGame.root.children
newGame.get_children()
# I need to traverse the games root node tree to get children (query)
# I need all nodes to have a name attribute

# Run the game
if __name__=='__main__':
	run(newGame,PORTRAIT,show_fps=True)