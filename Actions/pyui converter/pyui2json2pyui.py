# coding: utf-8

import editor, os

file_types = ('.json', '.pyui')

# Converts a .pyui file into a .json file
def pyui2json2pyui():
    srce_file = editor.get_path()
    root, ext = os.path.splitext(srce_file)
    assert ext in file_types, "'{}' must be in {}".format(ext, file_types)
    other_ext = [file_type for file_type in file_types if file_type != ext][0]
    dest_file = root + other_ext
    os.rename(srce_file, dest_file)
    fmt = '{} was renamed to {}.'
    print(fmt.format(os.path.basename(srce_file), os.path.basename(dest_file)))

pyui2json2pyui()
