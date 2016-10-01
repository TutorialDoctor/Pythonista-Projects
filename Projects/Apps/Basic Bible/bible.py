# coding: utf-8
import ui,sqlite3,datetime,sound,console,clipboard,dialogs,re,objc_util,editor,os,webbrowser,speech,fileinput

# This script uses 2 tables from the database, but there are others for translations


# VARIABLES
pairs={1: 'Genesis', 2: 'Exodus', 3: 'Leviticus', 4: 'Numbers', 5: 'Deuteronomy', 6: 'Joshua', 7: 'Judges', 8: 'Ruth', 9: '1 Samuel', 10: '2 Samuel', 11: '1 Kings', 12: '2 Kings', 13: '1 Chronicles', 14: '2 Chronicles', 15: 'Ezra', 16: 'Nehemiah', 17: 'Esther', 18: 'Job', 19: 'Psalms', 20: 'Proverbs', 21: 'Ecclesiastes', 22: 'Song of Solomon', 23: 'Isaiah', 24: 'Jeremiah', 25: 'Lamentations', 26: 'Ezekiel', 27: 'Daniel', 28: 'Hosea', 29: 'Joel', 30: 'Amos', 31: 'Obadiah', 32: 'Jonah', 33: 'Micah', 34: 'Nahum', 35: 'Habakkuk', 36: 'Zephaniah', 37: 'Haggai', 38: 'Zechariah', 39: 'Malachi', 40: 'Matthew', 41: 'Mark', 42: 'Luke', 43: 'John', 44: 'Acts', 45: 'Romans', 46: '1 Corinthians', 47: '2 Corinthians', 48: 'Galatians', 49: 'Ephesians', 50: 'Philippians', 51: 'Colossians', 52: '1 Thessalonians', 53: '2 Thessalonians', 54: '1 Timothy', 55: '2 Timothy', 56: 'Titus', 57: 'Philemon', 58: 'Hebrews', 59: 'James', 60: '1 Peter', 61: '2 Peter', 62: '1 John', 63: '2 John', 64: '3 John', 65: 'Jude', 66: 'Revelation'}

database = 'bible-sqlite.db'
# I'd like to add a timestamp to notes, so:
time_stamp = datetime.datetime.today().strftime('%m_%d_%Y_%H:%M:%S')
# File name for our notes file (here for easy access)
save_file = 'favorites.txt'
thoughts_file='thoughts.txt'
bookmarks_file='bookmarks.txt'
translation='t_kjv'
fullscreen_preview=None


# We will load the following list into a list dialog
translations={"t_asv":"American Standard - ASV1901 (ASV)",
"t_bbe":"Bible in Basic English - (BBE)",
"t_dby":"Darby - (DBY)",
"t_kjv":"King James Version (KJV)",
"t_wbt":"Webster's Bible (WBT)",
"t_web":"World English Bible (WEB)",
"t_ylt":"Young's Literal Translation (YLT)"}
# END VARIABLES

churches=['Union City (CA)','Vallejo (CA)','Moreno Valley (CA)','Baton Rouge (LA)','Tyler (TX)','Clarksville (NC)','Morrow (GA)','Xenia (OH)']

def create_assembly_folders():
	try:
		for folder in churches:
			document_directory=os.mkdir(folder)
	except:None


# Try to make a directory named 'Notes.' Do nothing if there is an exception error.
try:
	document_directory = os.mkdir('Notes')
except: None

"""
table_name: t_kjv
	records:
		b - book (int)
		c - chapter (int)
		v - verse (int)
		t - text (str)

table_name: key_english
	records:
		b - book (int)
		n - name (str)

table_name: bible_version_key
		id
		table
		abbreviation
	
American Standard - ASV1901 (ASV)
Bible in Basic English - (BBE)
Darby
King James Version (KJV)
Webster's Bible (WBT)
World English Bible (WEB)
Young's Literal Translation (YLT)
"""

instructions = """
Thoughts can be frozen and unfrozen using the Freeze Switch above.

Use the Thoughts(arrow) button to save a scripture selection to this Thought Bubble.

Uses the Load Button to load old thoughts from your Thoughts File into this Thought Bubble

Use the View Thoughts button to view your old thoughts.

The Save Thoughts button will save your current thoughts to your Thoughts File.

Use the Translate button to set the translation of the bible.

Use the Clip button to save your thoughts to the clipboard.

Use the Share button to share your thoughts via the IOS Share Sheet.
"""

web=ui.load_view_str("""
[
  {
    "class" : "View",
    "attributes" : {
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "enabled" : true,
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "frame" : "{{0, 0}, {540, 540}}",
    "selected" : false,
    "nodes" : [
      {
        "class" : "WebView",
        "attributes" : {
          "class" : "WebView",
          "name" : "webview",
          "frame" : "{{170, 170}, {200, 200}}",
          "uuid" : "C40643E2-3779-4B0D-ADBE-6CB8BC5350B1",
          "scales_to_fit" : true,
          "flex" : "WH"
        },
        "frame" : "{{0, 0}, {540, 540}}",
        "selected" : false,
        "nodes" : [

        ]
      }
    ]
  }
]
""")

settings_view = """
[
  {
    "class" : "View",
    "attributes" : {
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "enabled" : true,
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "frame" : "{{0, 0}, {336, 544}}",
    "selected" : false,
    "nodes" : [
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Font Size",
          "font_name" : "<System>",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "name" : "label1",
          "text_color" : "RGBA(0.396226,0.396226,0.396226,1.000000)",
          "class" : "Label",
          "alignment" : "center",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "703EBC4B-A8C3-4CF5-BFD8-8EBEC7F3CCB2"
        },
        "frame" : "{{95, 17}, {150, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Full Preview",
          "font_name" : "<System>",
          "name" : "label1",
          "text_color" : "RGBA(0.405660,0.405660,0.405660,1.000000)",
          "class" : "Label",
          "alignment" : "left",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "703EBC4B-A8C3-4CF5-BFD8-8EBEC7F3CCB2"
        },
        "frame" : "{{51, 121}, {150, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Switch",
        "attributes" : {
          "class" : "Switch",
          "value" : true,
          "frame" : "{{245, 255}, {51, 31}}",
          "uuid" : "F7BDB82C-1EF1-4D6E-B5FC-0F1FE88FE431",
          "name" : "switch1"
        },
        "frame" : "{{242, 122}, {51, 31}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Heart scripture",
          "font_name" : "<System>",
          "name" : "label1",
          "text_color" : "RGBA(0.396226,0.396226,0.396226,1.000000)",
          "class" : "Label",
          "alignment" : "left",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "703EBC4B-A8C3-4CF5-BFD8-8EBEC7F3CCB2"
        },
        "frame" : "{{51, 191}, {150, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Switch",
        "attributes" : {
          "class" : "Switch",
          "value" : true,
          "frame" : "{{245, 255}, {51, 31}}",
          "uuid" : "F7BDB82C-1EF1-4D6E-B5FC-0F1FE88FE431",
          "name" : "switch1"
        },
        "frame" : "{{242, 192}, {51, 31}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Heart scripture",
          "font_name" : "<System>",
          "name" : "label1",
          "text_color" : "RGBA(0.405660,0.405660,0.405660,1.000000)",
          "class" : "Label",
          "alignment" : "left",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "703EBC4B-A8C3-4CF5-BFD8-8EBEC7F3CCB2"
        },
        "frame" : "{{51, 260}, {150, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Switch",
        "attributes" : {
          "class" : "Switch",
          "value" : true,
          "frame" : "{{245, 255}, {51, 31}}",
          "uuid" : "F7BDB82C-1EF1-4D6E-B5FC-0F1FE88FE431",
          "name" : "switch1"
        },
        "frame" : "{{242, 261}, {51, 31}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Slider",
        "attributes" : {
          "class" : "Slider",
          "value" : 0.5,
          "frame" : "{{68, 255}, {200, 34}}",
          "uuid" : "64D8FB92-9362-4C8E-ABCC-8D93A0AE21F5",
          "name" : "slider_font",
          "flex" : "W"
        },
        "frame" : "{{69, 57}, {200, 34}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Aa",
          "font_name" : "<System>",
          "name" : "label3",
          "class" : "Label",
          "alignment" : "center",
          "frame" : "{{93, 256}, {150, 32}}",
          "uuid" : "C22A3BFB-B4DC-4C89-AFCF-7AED93972D5D"
        },
        "frame" : "{{15, 59}, {49, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 28,
          "text" : "Aa",
          "font_name" : "<System>",
          "name" : "label3",
          "class" : "Label",
          "alignment" : "center",
          "frame" : "{{93, 256}, {150, 32}}",
          "uuid" : "C22A3BFB-B4DC-4C89-AFCF-7AED93972D5D"
        },
        "frame" : "{{274, 59}, {49, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      }
    ]
  }
]
"""

splash_view = """
[
  {
    "selected" : false,
    "frame" : "{{0, 0}, {1024, 768}}",
    "class" : "View",
    "nodes" : [
      {
        "selected" : true,
        "frame" : "{{0, 0}, {1024, 768}}",
        "class" : "View",
        "nodes" : [

        ],
        "attributes" : {
          "uuid" : "A168428A-4038-472C-9288-8D1AD236BE41",
          "frame" : "{{462, 334}, {100, 100}}",
          "background_color" : "RGBA(0.500000,0.666667,1.000000,1.000000)",
          "name" : "view1",
          "custom_class" : "MyView",
          "class" : "View"
        }
      },
      {
        "selected" : false,
        "frame" : "{{319, 332}, {344, 61}}",
        "class" : "Label",
        "nodes" : [

        ],
        "attributes" : {
          "font_size" : 43,
          "text_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "frame" : "{{437, 368}, {150, 32}}",
          "uuid" : "12F3C02D-DBB8-4767-B577-A0631B246612",
          "text" : "The Bible App",
          "alignment" : "center",
          "class" : "Label",
          "name" : "label1",
          "font_name" : "AnonymousPro"
        }
      },
      {
        "selected" : false,
        "frame" : "{{387, 439}, {209, 32}}",
        "class" : "Label",
        "nodes" : [

        ],
        "attributes" : {
          "name" : "label2",
          "font_name" : "<System>",
          "frame" : "{{437, 368}, {150, 32}}",
          "uuid" : "DB5A637D-59D2-49DA-B6EF-33B65EEA9372",
          "text" : "By The Tutorial Doctor",
          "alignment" : "center",
          "class" : "Label",
          "font_size" : 18,
          "text_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)"
        }
      }
    ],
    "attributes" : {
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    }
  }
]
"""

info_view = """
[
  {
    "class" : "View",
    "attributes" : {
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "enabled" : true,
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    },
    "frame" : "{{0, 0}, {540, 540}}",
    "selected" : false,
    "nodes" : [
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Created by The Tutorial Doctor",
          "font_name" : "Arial-ItalicMT",
          "name" : "label1",
          "class" : "Label",
          "alignment" : "left",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "EAB6D439-BC91-4DC3-BF66-A7671A878516"
        },
        "frame" : "{{271, 502}, {269, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "ImageView",
        "attributes" : {
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "uuid" : "695F69D6-5D84-4A57-8F67-11825A0D96CC",
          "name" : "imageview1",
          "corner_radius" : 11,
          "border_width" : 0,
          "class" : "ImageView",
          "frame" : "{{220, 220}, {100, 100}}",
          "image_name" : "iob:alert_circled_256",
          "background_color" : "RGBA(1.000000,0.312500,0.312500,1.000000)"
        },
        "frame" : "{{120, 75}, {307, 312}}",
        "selected" : false,
        "nodes" : [

        ]
      }
    ]
  }
]
"""

map_view = """
[
  {
    "selected" : false,
    "frame" : "{{0, 0}, {540, 540}}",
    "class" : "View",
    "nodes" : [
      {
        "selected" : true,
        "frame" : "{{0, 0}, {540, 540}}",
        "class" : "ScrollView",
        "nodes" : [
          {
            "selected" : false,
            "frame" : "{{-10, 0}, {550, 540}}",
            "class" : "ImageView",
            "nodes" : [

            ],
            "attributes" : {
              "flex" : "WH",
              "frame" : "{{220, 220}, {100, 100}}",
              "class" : "ImageView",
              "name" : "image",
              "uuid" : "875A34C9-D9DA-45AF-BA8F-F97858CC6E5E"
            }
          }
        ],
        "attributes" : {
          "uuid" : "4C0B4FD8-9B61-4600-95F6-57866DB738F0",
          "frame" : "{{110, 110}, {320, 320}}",
          "content_height" : 540,
          "class" : "ScrollView",
          "name" : "scrollview",
          "content_width" : 540
        }
      }
    ],
    "attributes" : {
      "enabled" : true,
      "background_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
      "tint_color" : "RGBA(0.000000,0.478000,1.000000,1.000000)",
      "border_color" : "RGBA(0.000000,0.000000,0.000000,1.000000)",
      "flex" : ""
    }
  }
]
"""
#Used this code to get book number to book name conversion. Much easier than doing a query in two tables.
#con = sqlite3.connect('bible-sqlite.db')
#cur = con.cursor()
#a = cur.execute('select b,n from key_english')
#print(dict([x for x in a]))



# CLASSES			
# I will leave the results as a list so that I can load them into a tableview data source
# Textfield
class MyTextFieldDelegate (object):
	def textfield_should_begin_editing(self, textfield):
		return True
	def textfield_did_begin_editing(self, textfield):
		pass
	def textfield_did_end_editing(self, textfield):
		if textfield.text != '':
			def show():
				search.hidden=False
				search.alpha=.9
			ui.animate(show,.4)
			try:
				con = sqlite3.connect('bible-sqlite.db')
				cur = con.cursor()			
				substring= textfield.text
				sub_query="select b,c,v,t from {} where t like '%{}%'".format(translation,substring)
				sub_all=[x for x in cur.execute(sub_query)]
				table.data_source = ui.ListDataSource(sub_all)
				table.reload()
				matches.text=str(len(sub_all))
				#table.reload_data()
			except:
				None
	def textfield_should_return(self, textfield):
		textfield.end_editing()
		return True
	def textfield_should_change(self, textfield, range, replacement):
		return True
	def textfield_did_change(self, textfield):
		pass

#Textview
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
		return True
	def textview_did_change_selection(self, textview):
		pass

#Tableview
class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		item = tableview.data_source.items[row]
		search_selection.text =  str(pairs[item[0]])+' '+str(item[1])+': '+str(item[2])+'\n'+str(item[3])

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'
	
import ui

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
		pass
	def touch_moved(self, touch):
		# Called when a touch moves.
		splash.close()
		splash.wait_modal()
		bible.present(orientations=['landscape'],hide_title_bar=True)


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
# END CLASSES


# FUNCTIONS
# closes the superview of the sender
def close(sender):
	sender.superview.superview.close()
	speech.stop()

# save text in a view to the clipboard
def clip(sender):
	clipboard.set(thoughts.text)
	console.alert('Saved to Clipboard')

# open a list dialog
def translate(sender):
	global translation
	show=dialogs.list_dialog('Translations',[trans for trans in translations])
	translation=show
	try:
		translation_label.text = translations[translation]
	except: None
	
# open the IOS share sheet
def share(sender):
	dialogs.share_text(thoughts.text)

# load sqlite3 query into a tableview as a result of a segmented control action
def test(sender):
	con = sqlite3.connect(database)
	cursor=con.cursor()
	# A query to get all old testament book names in the 'key_english' table 
	ot_query = 'select n from key_english where b < 40'
	ot_bks = [x[0] for x in cursor.execute(ot_query)]
	
	# A query to get all new testament book names in the 'key_english' table 
	nt_query = 'select n from key_english where b >= 40'
	nt_bks = [x[0] for x in cursor.execute(nt_query)]
	
	selected_testament = sender.segments[sender.selected_index]
	
	if selected_testament=='Old Testament':
		books.data_source.items=ot_bks
	
	elif selected_testament=='New Testament':
		books.data_source.items= nt_bks

# Updates the table and text views
def updates(*args):
	# Connect to the sqlite database and create a cursor to query it with
	con = sqlite3.connect(database)
	cursor=con.cursor()
	# Three argument parameters (all tanleviews) that were passed in using a lambda function.
	tbl_books = args[0]
	tbl_chapters = args[1]
	control_testaments = args[2]
	
	# A query to get all book names in the 'key_english' table
	all_bks_query = 'select n from key_english'
	all_bks = [x[0] for x in cursor.execute(all_bks_query)]
	
	# Store tableview selections
	selected_book = tbl_books.items[tbl_books.selected_row]
	selected_chap = tbl_chapters.items[tbl_chapters.selected_row]
	#selected_testament = control_testaments.segments[control_testaments.selected_index]
	
	
	# Select book from the key_english table where the name = the selected book/cell of a tableview
	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
	
	c = selected_chap # unnecessary perhaps but using 'c' is shorter.
	
	# Select chapter,verse,text from the t_kjv table where book = book number (tableview) and chapter = selected chapter
	txt_query = "select c,v,t from '{}' where b = '{}' AND c = '{}'".format(translation,bk_num,c)
	txt = [row for row in cursor.execute(txt_query)]
	# Format the text as -- ''+chapter+text -- ('' can be replaced with whatever prefix you want)
	txt_formatted = "\n".join("{} {}: {}\n".format('',c,t) for b,c,t in txt)
	
	# If the formatted text is an empty string, set the contents textview to a string
	# This is a quick fix if a user selects a chapter in a book that doesn't exist for that book
	if txt_formatted=='':
		contents.text = 'Chapter does not exist'
	
	# Otherwise, set the contents textview to the formatted text
	else:
		contents.text = txt_formatted
		#contents2.data_source=ui.ListDataSource(txt)
		#contents2.data_source.number_of_lines=8
		#contents2.reload_data()
		#contents2.reload()
	# Set the heading label to the selected book plus the selected chapter (as a string)
	heading.text=selected_book+' '+str(selected_chap)

#	Save text/selected text in a textview to a file
def save_selection(sender):
	'''saves text/selected text in a textview to a file. If no text is selected, the entire text is saved.'''
	# Get the beginning of the textview selection
	beg= contents.selected_range[0]
	# Get the end of the textview selection
	end = contents.selected_range[1]
	# Get the entire text in the textview
	txt = contents.text
	# If text is selected (if there is a substring from beginning to end)...
	with open('Notes/'+save_file,'a') as outfile:
		if txt[beg:end] != '':
			# write the text to a file with a timestamp, the heading lable text, and the selected text.
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt[beg:end]+'\n')
		# Otherwise...
		else:
			# write the entire text to the file.
			outfile.write('\n'+time_stamp+'\n'+heading.text+'\n\n'+txt+'\n')
	# Play a sound
	sound.play_effect('digital:ThreeTone2')
	# Alert the user that fhe file has been saved to the file.
	console.alert('Saved to {}'.format(save_file))

# Same logic as save_selection
def selectionToThoughts(sender):
	beg= contents.selected_range[0]
	end = contents.selected_range[1]
	txt = contents.text
	if txt[beg:end] != '':
		thoughts.text = thoughts.text +heading.text+'\n'+txt[beg:end]+'\n\n'
	else:
		thoughts.text = thoughts.text +heading.text+'\n'+txt+'\n\n'
	sound.play_effect('rpg:DrawKnife2')

# Save text of a textview to a file
def save_thoughts(sender):
	with open('Notes/'+thoughts_file,'a',encoding='utf-8')	as outfile:
		outfile.write(time_stamp+'\n'+thoughts.text+'\n')
	sound.play_effect('rpg:BookFlip2')
	console.alert('Saved to {}'.format(thoughts_file))

# Make a textview editable or not editable with a switch.
def freeze(sender):
	if sender.value == True:
		thoughts.editable=True
	if sender.value==False:
		thoughts.editable=False

# Load text from a file into the 'thoughts' textview
def load_thoughts(sender):
	with open('Notes/'+thoughts_file,'r',encoding='utf-8') as infile:
		selection=dialogs.alert('Import {}'.format(infile.name),'Are you sure?','Yes','No')
		if selection==1:
			thoughts.text = infile.read()
		elif selection==2:
			None

# Set the 'thoughts' textview to an empty string (clear it).
def clear_thoughts(sender):
	selection=dialogs.alert('Clear Thoughts','Are you sure?','Yes','No')
	if selection==1:
		thoughts.text=''
	elif selection==2:
		None

# Creating a quick popup sheet to preview a text file called 'thoughts.txt' (see top)
def view_thoughts(sender):
	class update():
		def textview_should_begin_editing(self, textview):
			return True
		def textview_did_begin_editing(self, textview):
			pass
		def textview_did_end_editing(self, textview):
			with open('Notes/'+thoughts_file,'w',encoding='utf-8') as infile:
				infile.write(tv.text)
			dialogs.alert('updated')
		def textview_should_change(self, textview, range, replacement):
			return True
		def textview_did_change(self, textview):
			return True
		def textview_did_change_selection(self, textview):
			pass

	v=ui.View(name=thoughts_file)
	items=['Edit']
	v.right_button_items=[ui.ButtonItem(x) for x in items]
	v.width=540
	v.height=540
	v.background_color='white'
	tv=ui.TextView()
	tv.width=v.width
	tv.height=v.height
	tv.flex='WH'
	tv.background_color=''
	tv.editable=False
	tv.font=('Times New Roman',18)
	
	def make_editable(sender):
		tv.editable=True
	
	v.right_button_items[0].action = make_editable
	tv.delegate=update()
	with open('Notes/'+thoughts_file,'r',encoding='utf-8') as infile:
		tv.text=infile.read()
	v.add_subview(tv)
	global fullscreen_preview
	if not fullscreen_preview:
		v.present('sheet')
	else:
		v.present('fullscreen')

# Shows the search window
def show_search(sender):
	def show():
		search.hidden=False
		search.alpha=.9
	ui.animate(show,.4)
		
# Hides the search window
def hide_search(sender):
	def hide():
		search.alpha=0
	ui.animate(hide,.4)
	#search.present('sheet')
	#search.hidden=True

def choose_theme(sender):
	light_themes = [None,'Default','Dawn','Tomorrow','Solarized Light']
	dark_themes = ['Solarized Dark','Cool Glow','Gold','Tomorrow Night','Oceanic','Editorial']
	thm_nm= dialogs.list_dialog('Themes',light_themes+dark_themes)
	if thm_nm in light_themes:
		for x in background_changes:
			x.background_color='#fff'
	elif thm_nm in dark_themes:
		for x in background_changes:
			x.background_color='#373737'
	editor.apply_ui_theme(bible, theme_name=thm_nm)
	
def clear_search(sender):
	search_field.text=''

def forward_to_thoughts(sender):
	thoughts.text = thoughts.text +'\n\n'+search_selection.text
	sound.play_effect('rpg:BookFlip2')

# File name for our thoughts file.
def choose_file():
	global thoughts_file
	file_select= dialogs.list_dialog('Select A File',['New']+os.listdir('Notes'))
	if file_select=='New':
		thoughts_file = dialogs.input_alert('Name your thoughts file')+'.txt'
	elif file_select==None:
		pass
	else:
		thoughts_file= file_select

def view_files(sender):
	global thoughts_file
	file_select= dialogs.list_dialog('Select A File',['New']+os.listdir('Notes'))
	if file_select=='New':
		thoughts_file = dialogs.input_alert('Name your thoughts file')+'.txt'
	elif file_select==None:
		pass
	else:
		thoughts_file= file_select

def show_map(sender):
	#term='bason'
	map_view.present('sheet')

def show_settings(sender):
	settings_view.present('sheet')

def add_mark(sender):
	# Store tableview selections
	# Connect to the sqlite database and create a cursor to query it with
	con = sqlite3.connect(database)
	cursor=con.cursor()
	selected_book = books.data_source.items[books.data_source.selected_row]
	selected_chap = chapters.data_source.items[chapters.data_source.selected_row]
	#selected_testament = control_testaments.segments[control_testaments.selected_index]	
	# Select book from the key_english table where the name = the selected book/cell of a tableview
	num_query = "select b from key_english where n='{}'".format(selected_book)
	bk_num=[x for x in cursor.execute(num_query)][0][0]
	txt_query = "select c,v,t from '{}' where b = '{}' AND c = '{}'".format(translation,bk_num,selected_chap)
	txt = [row for row in cursor.execute(txt_query)]
	# Format the text as -- ''+chapter+text -- ('' can be replaced with whatever prefix you want)
	txt_formatted = "\n".join("{} {}: {}\n".format('',c,t) for b,c,t in txt)
	try:
		if selected_chap:
			book_marks.segments = book_marks.segments+tuple([selected_book+' '+str(selected_chap)+'\n'+txt_formatted])
	except: None

def load_mark(sender):
	txt=sender.segments[sender.selected_index]
	if txt=='':
		contents.text='empty'
	else:
		contents.text=txt
	heading.text = 'Bookmark'
	#heading.text=selected_book+' '+str(selected_chap)

def save_bookmarks(sender):
	bookmarks_file=dialogs.input_alert('name')+'.txt'
	txt=book_marks.segments
	for x in txt:
		with open('Notes/'+bookmarks_file,'a',encoding='utf-8')	as outfile:
			outfile.write(time_stamp+'\n'+str(x)+'\n')
	sound.play_effect('rpg:BookFlip2')
	console.alert('Saved to {}'.format(bookmarks_file))

def clear_bookmarks(sendr):
	selection=dialogs.alert('Delete Bookmarks','Are you sure?','Yes','No')
	print(selection)
	if selection==1:
		book_marks.segments=['']
	elif selection==2:
		None

def show_info(sender):
	info_view.present('sheet')

def change_font_size(sender):
	contents.font = ('TimesNewRomanPSMT',19+font_slider.value*5)
	thoughts.font = ('TimesNewRomanPSMT',19+font_slider.value*5)

def speak_scripture(sender):
	if speech.is_speaking():
		speech.stop()
	else: speech.say(contents.text)

def toggle_fullscreen(sender):
	global fullscreen_preview
	fullscreen_preview=settings_view['switch1'].value

def search_to_file(sender):
	tbl=table
	all = tbl.data_source.items
	string = ''.join(pairs[x[0]]+str(x)+'\n\n' for x in all)
	with open('Notes/'+'search: '+search_field.text+web_search_field.text+'.txt','a') as outfile:
		outfile.write(matches.text+'\n\n'+string)
	dialogs.alert('It is written')
# END FUNCTIONS


# I think it is okay to use single-letter variable names for small tasks, but certainly not all throughout your code. Comments help here also.


# IMPLEMENTATION
# Getting ui elements and setting actions
bible = ui.load_view()
left_pane = bible['view2']
right_pane = bible['view1']
panel = right_pane['panel']
panel.always_bounce_horizontal=False
panel.directional_lock_enabled=True
heading = left_pane['book_heading']
books = left_pane['books']
chapters = left_pane['chapters']
contents = left_pane['contents']
contents.font = ('TimesNewRomanPSMT',19)
contents2=left_pane['contents2']
testaments = left_pane['testaments']
testaments2 = left_pane['testaments2']
testaments.action=test
thoughts = right_pane['thought_bubble']
thoughts_switch = right_pane['panel']['switch']
thoughts_switch.action = freeze
thoughts_button = right_pane['panel']['btn_thoughts']
thoughts_button.action = selectionToThoughts
thoughts_save_button = right_pane['btn_save_thoughts']
thoughts_save_button.action = save_thoughts
load_button = right_pane['panel']['btn_load']
load_button.action = load_thoughts
clear_button = right_pane['panel']['btn_clear']
clear_button.action=clear_thoughts
fav_button = left_pane['btn_fav']
fav_button.action=save_selection
close_button = left_pane['btn_close']
close_button.action=close
clip_button = right_pane['panel']['btn_clip']
clip_button.action=clip
translate_button = right_pane['panel']['btn_translate']
translate_button.action=translate
share_button = right_pane['panel']['btn_share']
share_button.action=share
search_button = right_pane['btn_search']
search_button.action = show_search
search_close_button = bible['search']['btn_close']
search_close_button.action = hide_search
file_button = right_pane['panel']['btn_file']
file_button.action=view_files
theme_button = left_pane['btn_theme']
theme_button.action = choose_theme
translation_label = left_pane['label_translation']
map_button = right_pane['panel']['btn_map']
map_button.action = show_map
web_search_field = right_pane['web_search_field']
web_search_field.delegate = MyTextFieldDelegate()
book_marks = bible['book_marks']
book_mark_button = right_pane['panel']['btn_book_mark']
book_mark_button.action = add_mark
book_marks.action=load_mark
save_bookmarks_button=right_pane['btn_save_bookmarks']
save_bookmarks_button.action=save_bookmarks
clear_book_marks_button = right_pane['btn_clear_bookmarks']
clear_book_marks_button.action=clear_bookmarks
info_view = ui.load_view_str(info_view)
info_button = right_pane['panel']['btn_info']
info_button.action = show_info
speak_button=right_pane['panel']['btn_speak']
speak_button.action=speak_scripture
#chapters.data_source = ui.ListDataSource(range(1,100))


# SEARCH ENGINE
search=bible['search']
search.alpha=0
search.hidden=True
search.border_color = 'red'
search.border_width=1
search_field = search['search_field']
search_field.delegate = MyTextFieldDelegate()
search_clear_button = search['btn_clear_search']
search_clear_button.action = clear_search
forward_button = search['btn_forward']
forward_button.action= forward_to_thoughts
text = search['textview1']
search_selection = search['textview2']
search_selection.text = """Romans 13: 8
Owe no man any thing, but to love one another: for he that loveth another hath fulfilled the law."""
table= search['tableview1']
table.delegate = MyTableViewDelegate()
matches = search['matches']
save_all_button = search['btn_save_all']
save_all_button.action = search_to_file
# END SEARCH ENGINE


#SETTINGS
settings_view = ui.load_view_str(settings_view)
settings_button = right_pane['panel']['btn_settings']
settings_button.action = show_settings
font_slider = settings_view['slider_font']
font_slider.continuous = True
font_slider.action = change_font_size
fullscreen_switch = settings_view['switch1']
fullscreen_switch.action=toggle_fullscreen
# END SETTINGS

# THEMES
background_changes=[search_selection,search,books,contents,bible,thoughts,bible['view1'],heading,close_button,theme_button,book_marks]
for x in background_changes:
	x.background_color='#fff'
# END THEMES

# MAP
map_view=ui.load_view_str(map_view)
scroll=map_view['scrollview']
map = scroll['image']
map.image=ui.Image('IMG_0084.JPG')
map.width=map.image.size.width
map.height=map.image.size.height
scroll.content_size=(2000,2000)
scroll.content_size=tuple(map.image.size)
# END MAP


thoughts.text = instructions

# This lambda function is what allows me to pass arguments to a view's action function. This function is what makes it all work.
f = lambda sender: updates(sender,chapters.data_source,testaments)

# Quick and dirty query to preload a tableview with an sqlite record.
books.data_source.items = [x[0] for x in sqlite3.connect('bible-sqlite.db').execute('select n from key_english')]
books.data_source.action = f

splash = ui.load_view_str(splash_view)
splash.multitouch_enabled=True
splash.present(hide_title_bar=True)
#assembly=dialogs.list_dialog('Choose your Assembly',churches)
#dialogs.alert('Welcome {}'.format(assembly))
#choose_file()
# Display the bible witha hidden title bar and restrict its orientation to landscape.
#bible.present(orientations=['landscape'],hide_title_bar=True)


