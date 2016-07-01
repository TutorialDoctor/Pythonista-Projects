import ui

v = ui.load_view('Basic Bible')
v.background_color='#e8e8e8'

_book='Romans '
_chapter = '12'
label_text = _book + _chapter
v['label'].text=label_text

v.present('fullscreen',orientations='landscape',hide_title_bar='true')

login = ui.load_view('login')
login.background_color='purple'
#login.present('sheet',hide_title_bar='true')


#v.add_subview(ui.load_view('a'))
# name views
"""
testament
book
chapter
chapter_label

view_control
search_bar
search_results
search_verse
"""


# segmented control > toggle views hide/show (search and journal)

