import ui,sound,scene,urllib,os,objc_util


class Game(scene.Scene):
	music_dir = 'Music/'
	background_music = ['TRG_Banks_-_06_-_Goodbye_Machineryhead.mp3','David_Szesztay_-_Beach_Party.mp3']
	os.chdir(music_dir)
	sound_player=sound.Player(background_music[1])
	os.chdir('..')
	
	def setup(self):
		pass
	
	def update(self):
		#Performs any scene-specific updates that need to occur before scene actions are evaluated.
		
		#self.move(box,(0,5))
		#self.move(self.box,(0,5))
		self.move(player,(1,0))
		self.move(player2,(-1,0))
		self.jump(box)
	
	def stop(self):
		#Gets called automatically when the home button is pressed while a scene is running.
		self.sound_player.stop()
	
	def pause(self):
		#Gets called automatically when the home button is pressed while a scene is running.
		pass
	
	def touch_began(self,touch):
		#This method is called when a touch begins on the scene’s view
		pass
	
	def touch_moved(node,touch):
		#This method is called when a touch moves in the scene’s view
		pass
	
	def touch_ended(node,touch):
		#This method is called when a touch ends in the scene’s view
		pass

	# CUSTOM METHODS
	def move(self,node,direction):
		node.center+=direction
	
	def jump(self,node):
		node.run_action(scene.Action.move_by(20,20,1))
	
	def pause_game(self,sender):
		if sender.value == True:
			sv.paused=True
		else:
			sv.paused=False


# IMPLEMENTATION

# Create a new game
game = Game()
# Create a node
box = scene.SpriteNode()

# Add the node to the game
game.add_child(box)


# Download a file from internet (google drive)
#other_sound = urllib.request.urlretrieve('https://drive.google.com/uc?export=download&id=0B3zm9_2zdxHnQUJweTVtMU1GdDQ', 'notsonice.m4a')


def get_objects():
	console.text = str([x.name for x in editor.subviews])
	
def toggle_music(sender):
	if sender.value == True:
		game.sound_player.play()
	elif sender.value == False:
		game.sound_player.stop()

def pause_game(sender):
	if sender.value == True:
		sv.paused=True
	else:
		sv.paused=False

# UI
editor = ui.load_view('editor')
sound_title = editor['sound_title']


bubble = editor['bubble']
bubble.image = ui.Image('emj:Hearts')
player = editor['chr_1']
player.image = ui.Image('plf:AlienGreen_stand')
player2 = editor['chr_2']
player2.image = ui.Image('plf:AlienPink_front')
platform=editor['platform']
platform.image = ui.Image('Art/IMG_0066.PNG')
npc=editor['npc']
npc.image=ui.Image('plf:AlienBeige_front')


settings_view=editor['settings_view']
music_switch = settings_view['music_switch']
music_switch.action = toggle_music
pause_switch = settings_view['pause_switch']
pause_switch.action=game.pause_game
console= settings_view['console']
print(player.image.size)
get_objects()


# A Scene View is a ui.View that can display a scene
# A good way to use the scene and ui modules together.
sv = scene.SceneView()
sv.scene=game
sv.shows_fps=True
sv.add_subview(editor)
sv.present()
game.sound_player.play()
