name = raw_input('What name would you like to enter? ' )
address = raw_input('What is the address you are looking for? ' ) 
number = raw_input('What is the number you are looking for? ' )

phonebook = {}

phonebook[address] = address
phonebook[number] = number
phonebook[name]= (name, address, number)

search = raw_input('Who are you looking for? ' )

print(phonebook[search])

