"""
This following is an example of using the Database module
as tester; there is no front-end connection. Only communication
between the code and Database is needed.
"""

# From the Database module import the Database object that we created
from Database import Database

# initialize a new Database object
catalog = Database()

# display all the information currently in the database
catalog.displayAll()

catalog.addRow()

catalog.displayAll()

