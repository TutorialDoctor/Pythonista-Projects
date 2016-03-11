# coding: utf-8
import ui

main = ui.load_view('Views/main')
end = ui.load_view('Views/game_over')
start = ui.load_view('Views/menu')

img = end['view1']['imageview1']
text = end['view1']['label1']
img.image = ui.Image().named('iob:social_twitter_outline_256')
words =5
minutes='00:00'
text.text = 'I wrote {} words in {} minutes - and then I died using the Not as Dangerous Writing App @TutorialDoctor'.format(words,minutes)

start.present(hide_title_bar= True)
main.present(hide_title_bar = True)
end.present(hide_title_bar=True)