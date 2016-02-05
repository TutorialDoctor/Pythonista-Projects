# coding: utf-8
import ui
from master import master_root_view
from detail import detail_root_view

data = list('abcdefghijklmnopqrstuvwxyz')


splitView = ui.View()
splitView.width = 800
splitView.height = 800
splitView.background_color='white'
splitView.add_subview(master_root_view)
splitView.add_subview(detail_root_view)

master_root_view.width = 300
master_root_view.height = splitView.height
master_root_view.flex='H'

detail_root_view.flex='WHR'
detail_root_view.x+=master_root_view.width
detail_root_view.width=splitView.width-master_root_view.width
detail_root_view.height = splitView.height

tableview = master_root_view['tableview1']
tableview.data_source = ui.ListDataSource(data)

splitView.present()

# If you change the width of the master view, the detail view will shift accordingly.

# This script is still a controller that controls a split view. the splitview controller's view could have been in its own ui file like the detail and master views, but I didnt want to do that.

# You can use any type of view you want. I will try to use navigation views later.

# Hopefully this is the effect of the splitviewController.

# > Tutorial Doctor