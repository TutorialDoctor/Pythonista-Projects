#coding: utf-8
import ui
from faker import Faker
import clipboard
import console
import editor
import random
import platform

user_interface="""
[
  {
    "selected" : false,
    "frame" : "{{0, 0}, {540, 540}}",
    "class" : "View",
    "nodes" : [
      {
        "selected" : false,
        "frame" : "{{49, 120}, {363, 311}}",
        "class" : "TextView",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "WH",
          "font_size" : 17,
          "editable" : true,
          "frame" : "{{170, 170}, {200, 200}}",
          "spellchecking_type" : "default",
          "class" : "TextView",
          "uuid" : "1A6404DD-5697-4EAB-B901-7C8B86BEEE77",
          "alignment" : "left",
          "autocorrection_type" : "default",
          "name" : "textview1",
          "font_name" : "<System>"
        }
      },
      {
        "selected" : false,
        "frame" : "{{192, 16}, {305, 34}}",
        "class" : "Slider",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "W",
          "action" : "slider_changed",
          "continuous" : true,
          "frame" : "{{170, 253}, {200, 34}}",
          "uuid" : "F06B9CB3-83F7-4024-B7C4-14B1102954AF",
          "class" : "Slider",
          "value" : 0.5,
          "name" : "slider1"
        }
      },
      {
        "selected" : false,
        "frame" : "{{192, 58}, {305, 34}}",
        "class" : "Slider",
        "nodes" : [

        ],
        "attributes" : {
          "flex" : "W",
          "action" : "slider_changed",
          "continuous" : true,
          "frame" : "{{170, 253}, {200, 34}}",
          "uuid" : "385EFED8-F228-4615-90F1-9969A0FADB12",
          "class" : "Slider",
          "value" : 0.5,
          "name" : "slider2"
        }
      },
      {
        "selected" : true,
        "frame" : "{{64, 464}, {105, 54}}",
        "class" : "Button",
        "nodes" : [

        ],
        "attributes" : {
          "action" : "copy",
          "frame" : "{{230, 254}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "title" : "copy",
          "class" : "Button",
          "uuid" : "79C2488C-8E8E-4DC8-966D-77E93C35CC2E",
          "background_color" : "RGBA(0.872642,0.872642,0.349057,1.000000)",
          "font_size" : 15,
          "name" : "button1"
        }
      },
      {
        "selected" : false,
        "frame" : "{{205, 464}, {107, 54}}",
        "class" : "Button",
        "nodes" : [

        ],
        "attributes" : {
          "action" : "randomize",
          "frame" : "{{230, 254}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "title" : "Randomize",
          "class" : "Button",
          "uuid" : "79C2488C-8E8E-4DC8-966D-77E93C35CC2E",
          "background_color" : "RGBA(0.600000,0.866667,1.000000,1.000000)",
          "font_size" : 15,
          "name" : "button1"
        }
      },
      {
        "selected" : false,
        "frame" : "{{355, 464}, {104, 54}}",
        "class" : "Button",
        "nodes" : [

        ],
        "attributes" : {
          "action" : "insert",
          "frame" : "{{230, 254}, {80, 32}}",
          "tint_color" : "RGBA(1.000000,1.000000,1.000000,1.000000)",
          "title" : "Insert",
          "class" : "Button",
          "uuid" : "C8E2CFF7-1741-4A86-9771-DC81AA7E7D82",
          "background_color" : "RGBA(0.844444,0.533333,1.000000,1.000000)",
          "font_size" : 15,
          "name" : "button2"
        }
      },
      {
        "selected" : false,
        "frame" : "{{19, 18}, {150, 32}}",
        "class" : "Label",
        "nodes" : [

        ],
        "attributes" : {
          "font_size" : 18,
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "211836A3-0358-41D1-9728-E2D9CE37FE12",
          "text" : "Sentences",
          "alignment" : "left",
          "class" : "Label",
          "name" : "label1",
          "font_name" : "<System>"
        }
      },
      {
        "selected" : false,
        "frame" : "{{19, 60}, {150, 32}}",
        "class" : "Label",
        "nodes" : [

        ],
        "attributes" : {
          "font_name" : "<System>",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "211836A3-0358-41D1-9728-E2D9CE37FE12",
          "text" : "Labels",
          "alignment" : "left",
          "class" : "Label",
          "name" : "label1",
          "font_size" : 18
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
view = None

fake = Faker()
seed = random.randint(0, 9999)

def slider_changed(sender):
	fake.seed(seed)
	value1 = int(sender.superview['slider1'].value * 10) + 1
	value2 = int(sender.superview['slider2'].value * 10) + 1
	textview = sender.superview['textview1']
	paragraphs = []
	for i in range(value2):
		p = fake.paragraph(nb_sentences=value1, variable_nb_sentences=True)
		paragraphs.append(p)
	text = '\n\n'.join(paragraphs)
	textview.text = text

def copy(sender):
	clipboard.set(sender.superview['textview1'].text)
	console.hud_alert('Copied')

def insert(sender):
	text = sender.superview['textview1'].text
	start, end = editor.get_selection()
	editor.replace_text(start, end, text)
	if not platform.machine().startswith('iPad'):
		view.close()

def randomize(sender):
	global seed
	seed = random.randint(0, 9999)
	slider_changed(sender)

view = ui.load_view_str(user_interface)
view.present('popover')
slider_changed(view['slider1'])
