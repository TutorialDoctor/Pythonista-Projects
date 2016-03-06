# coding: utf-8
import ui,sound,sqlite3,console

def play_sound():
	sound.play_effect('game:Clock_2')

def get_views_of(x):
	for i in range(len(x.subviews)):
		print (i,x.subviews[i])

def get_node(root,name):
	if hasattr(root,'name') and root.name == name:
		return root
	for child in root.subviews:
		n = get_node(child,name)
		if n:
			return n

welcome_screen = ui.load_view('Views/welcome.pyui')
btn_submit = welcome_screen['button']


#conn = sqlite3.connect('Data/passwords.db')
#c = conn.cursor()
#c.execute('''CREATE TABLE entries
			 #(user text, password text)''')

def submit(sender):
	new_user = welcome_screen['name'].text
	new_pass = welcome_screen['pass'].text
	conn = sqlite3.connect('Data/passwords.db',timeout=10)
	# Create a cursor for querying (moving through) the database
	cursor = conn.cursor()
	# Insert a row of data with the cursor
	if new_user and new_pass != '':
		cursor.execute("INSERT INTO entries VALUES (?,?)",(new_user,new_pass))
		play_sound()
	else:
		console.alert('Fill out both fields')

	# Save (commit) the changes to the connected database
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	console.hud_alert('success')
	cursor.close()

def read_data():
	# Connect to a database
	connection = sqlite3.connect('Data/passwords.db',timeout=10)

	# Create a cursor for querying (moving through) the database
	cursor = connection.cursor()

	# Selecting from the database with the cursor
	for row in cursor.execute('SELECT * FROM entries'):
		print row
	connection.commit()
	cursor.close()

# Close the connection
con = sqlite3.connect('Data/passwords.db').close()
btn_submit.action = submit
welcome_screen.present('sheet')