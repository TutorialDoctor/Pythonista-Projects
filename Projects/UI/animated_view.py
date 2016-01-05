# Jan 2, 2016, 10:12 AM
# Tutorial Doctor
# Edited cy cclauss Tue Jan  5 17:18:36 EST 2016

# Add a ui to this file and add a custom view named view2. Add your
# controls to view2 and run the script.  view 2 should animate in
# when you press the +, and animate out when you press the greater than sign.
# Additionaly, some toolbar options should be added to the main view.

import ui,sound
print ui

# Action Functions
#--------------------------------------------------------------------
def move_left(sender):
	def left():
		view2.x = 0
		#view2 is a custom view located to the right of the main view
		# add suviews to this view if you please.
		r[0].action = move_right
	r[0].title = '>'
	ui.animate(left, .5)


def move_right(sender):
	def right():
		r[0].action = move_left
		view2.x = window.width
	r[0].title = '+'
	ui.animate(right, .5)


def close(sender):
	window.close()
def check(sender):
	sound.play_effect('Woosh_1')
def error(sender):
	sound.play_effect('Error')
def clip(sender):
	sound.play_effect('Clock_1')
#--------------------------------------------------------------------


# Setup
#--------------------------------------------------------------------
window = ui.load_view()
view2 = window['view2']
view2.x = window.width
view2.height = window.height
view2.width = window.width
#--------------------------------------------------------------------


# Functions
#--------------------------------------------------------------------
def create_l_buttonItems(titles):
	def make_button_item(title):
		button = ui.ButtonItem(b)
		button.enabled = title != '|'
		button.tint_color = 'white'
		return button
	return [make_button_item(title) for title in titles]

def create_r_buttonItems(titles):
	def make_button_item(title):
		button = ui.ButtonItem(b)
		button.tint_color = 'white'
		button.action = move_right if title == '>' else move_left
		return button
	return [make_button_item(title) for title in titles]
#--------------------------------------------------------------------


# Implementation
#--------------------------------------------------------------------
l = create_l_buttonItems('File | Edit | About'.split())
window.left_button_items = l
r = create_r_buttonItems('+')
window.right_button_items = r
window.present('fullscreen', title_bar_color='#635D51')
#--------------------------------------------------------------------


# Testing
#--------------------------------------------------------------------
for menu in (l, r):
	print(', '.join(item.title for item in l))
#--------------------------------------------------------------------


# Notes and discoveries
#--------------------------------------------------------------------
# The readability of code can be improved by avoiding single character variable names.
# If you write good functions, the implementation should be short and simple to understand.
# Comments shouldn't be needed in this case.
# This code is still not as refactorable as it can be.
#--------------------------------------------------------------------
