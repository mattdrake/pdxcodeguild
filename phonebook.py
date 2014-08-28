#input to determine what entry to add to phonebook
name = raw_input('What name would you like to enter? ' )
address = raw_input('What is the address you are looking for? ' ) 
number = raw_input('What is the number you are looking for? ' )

#phonebook created with no entries until user input
phonebook = {}

#assigning user input to items in the phonebook
phonebook[address] = address
phonebook[number] = number
phonebook[name]= (name, address, number)

#input to search for entry that was just collected
search = raw_input('Who are you looking for? ' )

#show result of search
print(phonebook[search])

