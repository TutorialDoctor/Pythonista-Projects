# coding: utf-8

import ui,console,re

def save_file(sender):
	"""Creates a file in the Files directory"""
	# If the field text DOES match a regular expression...
	if re.match('\w+\.\w+',f.text) != None:
		# open a file with the file name as its name...
		with open('Files/'+f.text,'w') as outfile:
			# and write the text of the textview to it.
			outfile.write(t.text)
		# Then show a hud alert message with a success icon
		console.hud_alert(f.text+' file saved','success')
	else:
		# Otherwise, show an error hud alert
		console.hud_alert('Incorrect file name format','error')

def load_file(sender):
	"""Creates a file in the Files directory"""
	# If the field text DOES match a regular expression...
	if re.match('\w+\.\w+',f.text) != None:
		# open a file with the file name as its name...
		with open('Files/'+f.text,'r') as infile:
			# and write the text of the textview to it.
			t.text = infile.read()
		# Then show a hud alert message with a success icon
		console.hud_alert(f.text+' file loaded','success')
	else:
		# Otherwise, show an error hud alert
		console.hud_alert('Incorrect file name format','error')

def clear_view(sender):
	t.text = ''

# Setup			
v = ui.load_view()
v.tint_color='white'
save = v['save_button']
load = v['load_button']
clear = v['clear_button']
t = v['textview1']
f = v['textfield1']
save.action = save_file
load.action = load_file
clear.action = clear_view

v.present('sheet',title_bar_color='#929292')

#print help(create_file)

# Demonstrates:
	# Using Regular Expressions to verify file name formatting 
	# Console alerts
	# Using UI controls for file manipulation