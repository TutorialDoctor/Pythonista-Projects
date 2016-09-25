from shutil import copyfile
import editor,dialogs

src = editor.get_path()

copyfile(src,dialogs.input_alert('New Name'))
