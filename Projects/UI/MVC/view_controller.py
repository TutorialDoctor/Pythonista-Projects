# coding: utf-8
import ui

#M
# Create the data/model
data = ['a',45,True,3.17]

# This data should be defined elsewhere and not here in the controller code. Perhaps it can be stored in JSON format.
# If this data were in a dictionary, it would more object-like and this is why models are usually classes.
# Even so, the model isn't the data, but perhaps a class that gets or manipulates the data. A model is more of an object, thus the name 'model' makes more sense now.

#V
# Get the views/user interface
root_view = ui.load_view('root_view')
view1=root_view['view1']
view2=root_view['view2']
tableview=view2['tableview1']

#C
# Connect the model to the view
tableview.data_source = ui.ListDataSource(data)

# The above code should be the only code in this controller as it is the logic that connects the model to the view(s).


# Now let's present it
root_view.present()




# Now the idea of a splitView controller makes sense. It just contols two views instead of one and handles how data gets exchanged between them. You would have two root views, one that is a masterview, and another that is a detail view. 

# However, the master and detail are not exactly views only, but viewcontrollers thenselves. In the case of pythonista, they would be python files with attatched views. So, these scripts could be impoorted into the splitViewController script.
