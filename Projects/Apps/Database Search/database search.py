import sqlite3,re,ui

# I will leave the results as a list so that I can load them into a tableview data source
# TEXTFIELD
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
		try:
			text.text = str(re.findall(textfield.text+'.+',verses))
			table.data_source = ui.ListDataSource(re.findall(textfield.text+'.+',verses))
			table.reload()
			table.reload_data()
		except:
			None

#TEXTVIEW
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


class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		# Called when a row was selected.
		pass

	def tableview_did_deselect(self, tableview, section, row):
		# Called when a row was de-selected (in multiple selection mode).
		pass

	def tableview_title_for_delete_button(self, tableview, section, row):
		# Return the title for the 'swipe-to-***' button.
		return 'Delete'

verses = """
Romans 12
A Living Sacrifice

Rom 12:1  I beseech you therefore, brethren, by the mercies of God, that ye present your bodies a living sacrifice, holy, acceptable unto God, which is your reasonable service.

Rom 12:2  And be not conformed to this world: but be ye transformed by the renewing of your mind, that ye may prove what is that good, and acceptable, and perfect, will of God.

Gifts of Grace

Rom 12:3  For I say, through the grace given unto me, to every man that is among you, not to think of himself more highly than he ought to think; but to think soberly, according as God hath dealt to every man the measure of faith.

Rom 12:4  For as we have many members in one body, and all members have not the same office:

Rom 12:5  So we, being many, are one body in Christ, and every one members one of another.

Rom 12:6  Having then gifts differing according to the grace that is given to us, whether prophecy, let us prophesy according to the proportion of faith;

Rom 12:7  Or ministry, let us wait on our ministering: or he that teacheth, on teaching;

Rom 12:8  Or he that exhorteth, on exhortation: he that giveth, let him do it with simplicity; he that ruleth, with diligence; he that sheweth mercy, with cheerfulness.

Marks of the True Christian

Rom 12:9  Let love be without dissimulation. Abhor that which is evil; cleave to that which is good.

Rom 12:10  Be kindly affectioned one to another with brotherly love; in honour preferring one another;

Rom 12:11  Not slothful in business; fervent in spirit; serving the Lord;

Rom 12:12  Rejoicing in hope; patient in tribulation; continuing instant in prayer;

Rom 12:13  Distributing to the necessity of saints; given to hospitality.

Rom 12:14  Bless them which persecute you: bless, and curse not.

Rom 12:15  Rejoice with them that do rejoice, and weep with them that weep.

Rom 12:16  Be of the same mind one toward another. Mind not high things, but condescend to men of low estate. Be not wise in your own conceits.

Rom 12:17  Recompense to no man evil for evil. Provide things honest in the sight of all men.

Rom 12:18  If it be possible, as much as lieth in you, live peaceably with all men.

Rom 12:19  Dearly beloved, avenge not yourselves, but rather give place unto wrath: for it is written, Vengeance is mine; I will repay, saith the Lord.

Rom 12:20  Therefore if thine enemy hunger, feed him; if he thirst, give him drink: for in so doing thou shalt heap coals of fire on his head.

Rom 12:21  Be not overcome of evil, but overcome evil with good.
"""

interface="""
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
        "class" : "TextField",
        "attributes" : {
          "font_size" : 17,
          "font_name" : "<System>",
          "text" : "",
          "autocorrection_type" : "default",
          "name" : "textfield1",
          "uuid" : "4883FC8D-6406-484A-B2C0-0ED939EE4169",
          "class" : "TextField",
          "alignment" : "left",
          "placeholder" : "mercies",
          "frame" : "{{170, 254}, {200, 32}}",
          "spellchecking_type" : "default"
        },
        "frame" : "{{39, 97}, {460, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "TextView",
        "attributes" : {
          "font_size" : 17,
          "font_name" : "<System>",
          "flex" : "WH",
          "autocorrection_type" : "default",
          "name" : "textview1",
          "uuid" : "1D3A9DBB-AFC7-4563-B023-8A40761BC092",
          "class" : "TextView",
          "editable" : true,
          "alignment" : "left",
          "frame" : "{{170, 170}, {200, 200}}",
          "spellchecking_type" : "default"
        },
        "frame" : "{{39, 172}, {255, 339}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "Label",
        "attributes" : {
          "font_size" : 18,
          "text" : "Enter a query below:",
          "font_name" : "AppleSDGothicNeo-Regular",
          "name" : "label1",
          "class" : "Label",
          "alignment" : "center",
          "frame" : "{{195, 254}, {150, 32}}",
          "uuid" : "013A8223-5B0A-4477-9778-CB4E74D360E2"
        },
        "frame" : "{{142, 40}, {255, 32}}",
        "selected" : false,
        "nodes" : [

        ]
      },
      {
        "class" : "TableView",
        "attributes" : {
          "data_source_font_size" : 18,
          "data_source_number_of_lines" : 1,
          "flex" : "WH",
          "name" : "tableview1",
          "row_height" : 44,
          "data_source_delete_enabled" : true,
          "class" : "TableView",
          "data_source_items" : "Row 1\nRow 2\nRow 3",
          "frame" : "{{170, 170}, {200, 200}}",
          "background_color" : "RGBA(1.0, 1.0, 1.0, 1.0)",
          "uuid" : "8657D611-5F75-4C8B-8537-59BBBC2D9ACF"
        },
        "frame" : "{{302, 172}, {220, 339}}",
        "selected" : false,
        "nodes" : [

        ]
      }
    ]
  }
]
"""

v=ui.load_view()
field=v['textfield1']
field.delegate = MyTextFieldDelegate()
text = v['textview1']
table= v['tableview1']
v.present()
#print(re.findall('\d+[:]\d+',verses))
