# coding: utf-8
import ui
from data.test1 import *

main = ui.load_view('views/main')
question = main['question']
info = main['info']
info.text = q1['i']
question.text = q1['q']
main.present()