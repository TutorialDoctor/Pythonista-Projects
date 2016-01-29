# coding: utf-8
import ui

view = ui.View()
view.background_color='white'
nav = ui.NavigationView(view)
nav.present()

view2 = ui.View()
view2.name='View 2'
view2.background_color='blue'
nav.push_view(view2)

view3 = ui.View()
view3.name='View 3'
view3.background_color='#e5ffaa'
nav.push_view(view3)

view4 = ui.View()
view4.name='View 4'
view4.background_color='#717171'

nav.push_view(view4)