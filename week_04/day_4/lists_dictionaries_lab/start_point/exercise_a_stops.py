stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh Waverly")
#print(stops)

#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St") # CHECK THIS, IT REMOVED CROY OUT OF THE LIST
# print(stops)
#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(4, "Polmont")
# print(stops)
#4. Print out the index position of "Linlithgow"
index = stops.index("Linlithgow")
print(index)
#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
# print(stops)
#6. Delete "Cumbernauld" from the list by index
stops.pop()
print(stops)
#7. Print the number of stops there are in the list
number_of_items = len(stops)
# print(number_of_items)
#8. Sort the list alphabetically
alphabetical_list = sorted(stops)
print(alphabetical_list)
#9. Reverse the positions of the stops in the list
stops.reverse()
#10 Print out all the stops using a for loop
#11. Print out only the stops that begin with the letter L using a for loop
#12. Remove all stops that begin with the letter C using a for loop
