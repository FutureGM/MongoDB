

# A. Use the command line to create a classDB database.
# Insert entries for yourself and the people in your row in a classroom collection.
# Each document should have:

# 1. A field of name with the person's name.
# 2. A field of rownumber which will contain the row number that they are in.
# 3. A field of the person's favorite Python library, e.g. pandas.
# 4. A field of a list of the person's hobbies .

# Example:
use classDB;
switched to db classDB
db.destinations.insert({"name": "Nisha", rownumber: 1, favorite_PyLibrary: "Matplotlib", hobbies: "coding"})

db.destinations.insert({name": "Nisha", "rownumber": 1, "favorite_PyLibrary": "Matplotlib", "hobbies": "coding"})
2018-04-28T12:03:32.674-0400 E QUERY    [thread1] SyntaxError: missing ) after argument list @(shell):1:29
db.destinations.insert({name": "Nisha", "rownumber": 1, "favorite_PyLibrary": "Matplotlib", "hobbies": "coding"})



# B. Use find commands to get:
# 1. A list of everyone in a particular row.
db.destinations.find({row: 1}).pretty()
# 2. An entry for a single person.
db.destinations.find({name: "Nisha"}).pretty()

# Bonus:
# If you finish early, check out the MongoDB documentation
# and figure out how to find users by an entry in an array.
