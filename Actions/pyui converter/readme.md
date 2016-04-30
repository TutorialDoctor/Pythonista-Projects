Easily convert `.pyui` to files to `.json` and vice-versa.

Save these two scripts as actions and run them from whatever python file that has an associated ui file.

Running `pyui2json.py` from a python file that has a `.pyui` file will turn the `.pyui` file into a `.json` file. This makes it easy to share user interfaces.

If you are downloading a project that has a `.py` file and a `.json` file, running `json2pyui.py` will change the `.json` file back into a `.pyui` file. 

If you need to open the `.json` file in another app on IOS, I have added a small `openIn.py` script. Add this as an action also, to open the current document in another app. This was needed mainly for `.json` files, since the export action doesn't recognize them. It works for .txt files also.

I may add the ability to automatically zip all of these files up for export if it is wanted.

Now it is time to really get some projects going in Pythonista!


