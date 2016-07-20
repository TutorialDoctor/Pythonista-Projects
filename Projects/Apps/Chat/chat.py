import ui,console,speech,sound

# counter for how many times message entry button is pressed
i=0

def close(sender):
	sender.superview.close()

def speak(sender):
	if entry_message.text =='':
		speech.say('I cannot say that')
	else:
		speech.say(entry_message.text)

def change_text(sender):
	global i
	i+=1
	message_box2.text = entry_message.text
	def expand():
		message_box_container.width = message_box_container.width + 64
		message2.y-=64
		message.y-=64
	def shrink():
		def shrink_width():
			message_box_container.width = message_box_container.width - 64
		ui.animate(shrink_width,1,0)
	
	sound.play_effect('digital:HighDown')
	# If the message entry button counter is <= 3 (presses)...
	if i <= 4:
		# animate the width of the message2 box(expand) with a duration of 1 and a delay of 0, and then shrink it.
		# Also, move both message views 64 pixels up (negative)
		ui.animate(expand,1,0,shrink)
	else:
		message.y=message.location
		message2.y=message2.location
		i = 0
		
	# 3 can be changed to whatever you like. i will use this to reset the locations of the views


class MyView (ui.View):

	def __init__(self):
	# This will also be called without arguments when the view is loaded from a UI file.
	# You don't have to call super. Note that this is called *before* the attributes
	# defined in the UI file are set. Implement `did_load` to customize a view after
	# it's been fully loaded from a UI file.
		pass
		#print(self)

	def did_load(self):
	# This will be called when a view has been fully loaded from a UI file.
		pass

	def will_close(self):
		# This will be called when a presented view is about to be dismissed.
		# You might want to save data here.
		pass

	def draw(self):
		# This will be called whenever the view's content needs to be drawn.
		# You can use any of the ui module's drawing functions here to render
		# content into the view's visible rectangle.
		# Do not call this method directly, instead, if you need your view
		# to redraw its content, call set_needs_display().
		# Example:
		pass

	def layout(self):
		# This will be called when a view is resized. You should typically set the
		# frames of the view's subviews here, if your layout requirements cannot
		# be fulfilled with the standard auto-resizing (flex) attribute.
		pass

	def touch_began(self, touch):
		# Called when a touch begins.
		nv=ui.load_view('chat')['message']
		self.add_subview(nv)
		nv.center= touch.location

	def touch_moved(self, touch):
		# Called when a touch moves.
		#v=ui.load_view('window')
		#self.add_subview(v)
		#v.center= touch.prev_location
		pass

	def touch_ended(self, touch):
		# Called when a touch ends.
		pass

	def keyboard_frame_will_change(self, frame):
		# Called when the on-screen keyboard appears/disappears
		# Note: The frame is in screen coordinates.
		pass

	def keyboard_frame_did_change(self, frame):
		# Called when the on-screen keyboard appears/disappears
		# Note: The frame is in screen coordinates.
		pass

# TEXT VIEW DELEGATE
class MyTextViewDelegate (object):
	def textview_should_begin_editing(self, textview):
		return True
	def textview_did_begin_editing(self, textview):
		pass
	def textview_did_end_editing(self, textview):
		pass
	def textview_should_change(self, textview, range, replacement):
		return True
	def textview_did_change(self, textview):
		textview.text = 'changed'
	def textview_did_change_selection(self, textview):
		pass

# TABLE VIEW DELEGATE
class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		user_name.text=tableview.data_source.items[row]
		sound.play_effect('ui:click3')

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Eat'

# TEXT FIELD DELEGATE
class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		pass
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		textfield.text = 'Changed'

#IMPLEMENTATION
a = MyView()

v = ui.load_view()
v.background_color='white'

channels = v['channels']
channels.delegate = MyTableViewDelegate()
message = v['message']
message_box = message['message_box']
message_box.editable=False
message_box.text = 'yup'
message.location = message.y
user_name = message['user_name']
user_name.text = 'Tutorial Doctor'

message2 = v['message2']
message_box_container = message2['container']
message_box2=message_box_container['message_box']
message_box2.editable=False
message_box2.text = 'huh?'
message2.location = message2.y
user_name2 = message2['user_name']
user_name2.text = 'Other Person'

print(message.location)
entry_message = v['entry']['message']
mic = v['entry']['mic']
mic.action=speak

banner = v['banner']
banner.image=ui.Image.named('IMG_3222.PNG')

close_button = v['btn_close']
close_button.action=close

message_button = v['entry']['btn_message']
message_button.action = change_text
v.present(orientations=['landscape'],hide_title_bar=True)
#a.present()
