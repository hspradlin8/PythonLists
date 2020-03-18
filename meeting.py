#list append() method: Adds an element at the end of the list

# list extend() method: Add the elements of a list(or any iterable), to the end of the current list

# list index() method: Returns the index of the first element with the specified value. 

#join- it is off of strings and you can join any iterable together. 

attendees = ["Ken", "Alena", "Treasure"]
attendees.append("Ashley")
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are", len(potential_attendees), "potential attendees currently")

to_line = ", ".join(attendees)
cc_line = ", ".join(optional_invitees)
print("To: "+ to_line)
print("Cc: "+ cc_line)

