# Problem
# A group of friends have decided to start a secret society. 
# The name of the society will be the first letter of each of their names.
# Task
# Create a function society_name that takes in a list of names and returns the name of the secret society.
#
# (Try to solve this without using any built-in python methods)
def society_name(names):
  for n in range(0,len(names)):
      print(names[n][0])
      
      
# Tests
name_1 = society_name(["Adam", "Sarah", "Malcolm"]) 
#print(name_1) # should print "AMS"
name_2 = society_name(["Harry", "Newt", "Luna", "Cho"]) 
#print(name_1) # should print "CHLN"
name_3 = society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"])
#print(name_3) # should print "CJMPRR"