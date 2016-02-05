# coding: utf-8
import ui

def close(sender):
	sender.superview.close()

class MyView (ui.View):
	def __init__(self):
		# This will also be called without arguments when the view is loaded from a UI file.
		# You don't have to call super. Note that this is called *before* the attributes
		# defined in the UI file are set. Implement `did_load` to customize a view after
		# it's been fully loaded from a UI file.
		pass

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
		v=ui.load_view('window')
		self.add_subview(v)
		v.center= touch.location


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


	
v = MyView()
v.background_color='white'
v.present()