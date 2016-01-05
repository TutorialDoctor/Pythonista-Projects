import editor,os,shutil

# Converts a .json file into a .pyui file
def json2pyui():
    python_file = editor.get_path()
    root,ext = os.path.splitext(python_file)
    ui_file = root+'.json' 
    os.rename(ui_file,root+'.pyui')
    
