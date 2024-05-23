"""
This acts as a Database for our program
The Database object contains hardcoded preset information containing three courses
in order to show proof of concept 
"""

class Database:
    # constructor that defines our object
    def __init__(self):
       # initialize an emtpy dictionary
       self.db = dict()

       # add three items to use for examples
       """
       The following is the format of the dictionary:
       key : the class ID, item: another dictionary (nested) containing course information
       """
       self.db["26657"] = {"title" : "Intro to Hardware and OS",
                           "course" : "CS 103",
                           "credits" : 5}
       
       self.db["26652"] = {"title" : "Intro to Virtualization",
                           "course" : "CS 106",
                           "credits" : 5}
       
       self.db["26664"] = {"title" : "Professional Preperation",
                           "course" : "WKED 101",
                           "credits" : 1}

    # GET request
    # get a "row", or item, by the dictionary key
    def findById(self, id):
        for key in self.db:
            if key == id:
                return self.db[id]
        
        else:
            return {"error" : "record not found"}

    # POST request        
    def addRow(self):
        id = input("Enter the new course id: ")
        title = input("Enter new course title: ")
        course = input("Enter new course code: ")
        credits = -1

        while True:
            try:
                credits = int(input("Enter new course credits:"))
                
                if credits < 0:
                    print("Error; credits must be zero or greater")
                    continue

                break
            except:
                print("Invalid input; credits must be a number")

        self.db[id] = {"title" : title,
                       "course" : course,
                       "credits": credits}
        
        print("New record with id of ", id, " added")

    
    # DELETE request
    def deleteById(self, id):
        
        if id in self.db:
            del self.db[id]
            print("Item with id of ", id, "deleted.")
        else:
            print("Error; id", id, " not found.")

    
    # READ request
    def displayAll(self):
        for i in self.db:
            print(i, ": ")
            for j in self.db[i]:
                print("\t", j, ": ", self.db[i][j])