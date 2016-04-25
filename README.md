# CapstoneStudentFileQueryer
assists in going through the many names and stats required for building a capstone team 

# How to Use

Ensure that the two files Bart gave use are in the the same folder as the script and that their names are reflected at the top of the code (right now i have them in there assuming you renamed them to 'prefs.csv' and 'inven.csv'. also they need to be csv files so you might have to convert them). 

As an aside, i changed the first category from "what is your name?" to simply "name" and the script assumes you have done the same.

Run the script and chose whether you want to perform a query on the preferences file or the inventory file or both. 

# Querying the Prefs file
This will allow you to compile lists of students with a particular interest in a specific project. Enter the project and the minimum ranking (keeping in mind the lower means more interested) and the queryer will return (and print) a list of students that fit the query, and ask if you want to save the results to a csv file.

# Querying the inventory file
Since this file has lots of information in it, ensure that you look for the type of parameter you're interested in. This can be a role ("Innovator") or a technology ("C++") because the queryer just searches if the word you input is in the catagory name, so it is pretty flexible. This will do the same as above, returning a dictionary of students with values being a dictionary of all the catagories that have your search item in it, and the students answers. Once again you can chose to export this to a csv file.

# Querying both
The humdinger of this tool. Allows you to first query the students rankings for a specific projects, constrained by a minimum rank (you can chose to export to a file at this point, but chosing no will put the data in the second query either way) and then use that to construct a list of those students inventory stats for a specific item in the list. 

# As always, feel free to pull this and change it or add to it to fit your needs. If you have a really helpful feature, don't hesitate to add it to the tool!
