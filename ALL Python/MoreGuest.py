#The list of Guest
#Changing Guest Name
name = ['vicent', 'morewei', 'ik', 'donald']

print(name[0].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[1].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[2].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[3].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[3].title() + "," + ' cannot make to my sister wedding.')

#Peplacing Guest Name
name[3] = 'danjuma'

print("\n" + name[3].title() + "," + ' I am inviting you special for the wedding of my sister')

#Printing second invitaion after guest that cannot make it has been replaced
print("\n" + name[0].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[1].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[2].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[3].title() + "," + ' I am inviting you special for the wedding of my sister')

#Adding more guest to a bigger table
print("Sorry everyone, I just found a bigger dinner table.")

#Using insert() to add one new guest to the beginning of your list.
#Using insert() to add one new guest to the middle of your list.
#Using append() to add one new guest to the end of your list.
name.insert(0,'drake')
name.insert(3,'travis')
name.append('billy')

print(name)

#Print a new set of invitation messages, one for each person in your list
print("\n" + name[0].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[1].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[2].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[3].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[4].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[5].title() + "," + ' I am inviting you special for the wedding of my sister')
print(name[6].title() + "," + ' I am inviting you special for the wedding of my sister')


#Shrinking Guest List

print

#Use pop() to remove guests from your list one at a time until only two 
#names remain in your list.
pop_name2 = name.pop()
print("\n" + "I am very sorry " + pop_name2 + " ,I can't invite you to my sisters wedding.")

pop_name3 = name.pop()
print("I am very sorry " + pop_name3 + " ,I can't invite you to my sisters wedding.")

pop_name4 = name.pop()
print("I am very sorry " + pop_name4 + " ,I can't invite you to my sisters wedding.")

pop_name5 = name.pop()
print("I am very sorry " + pop_name5 + " ,I can't invite you to my sisters wedding.")

pop_name6 = name.pop()
print("I am very sorry " + pop_name6 + " ,I can't invite you to my sisters wedding.")

print("\n" + name[0].title() + " ,you are still invited to my sisters wedding.")
print(name[1].title() + " ,you are still invited to my sisters wedding.\n")


#Use del to remove the last two names from your list, so you have an empty 
#list. Print your list to make sure you actually have an empty list at the end 
#of your program
del name[0]
print(name)

del name[0]
print(name)
