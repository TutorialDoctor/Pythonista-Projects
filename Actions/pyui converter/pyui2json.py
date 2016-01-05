import editor,os,shutil

# Converts a .pyui file into a .json file
def pyui2json():
    python_file = editor.get_path()
    root,ext = os.path.splitext(python_file)
    ui_file = root+'.pyui'
    backup_folder = python_file+'backup'
    try:
        os.makedirs(backup_folder)
    except:
        None
    shutil.copy(ui_file,backup_folder)
    os.rename(ui_file,root+'.json')