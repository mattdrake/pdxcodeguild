done = False
phonebook = {}

class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def prompts(self):
        name = raw_input("Please enter a first and last name. ")
        address = raw_input("Please enter an address. ")
        number = raw_input("Please enter a telephone number. ")
        phonebook[name] = (name, address, number)

    def entry(self):
        search = raw_input("Who are you looking for? ")
        if search in phonebook.keys():
            print(phonebook[search])
            complete = raw_input("Would you like to search for someone else? ").lower()
            if complete == 'yes':
                entry(self)
            else:
                print("Thank you for using the Phonebook.")

        else:
            answer = raw_input("This user is not in the Phonebook. Would you like to enter them now? Yes or No. ").lower()
            if answer == 'yes':
                prompts(self)
                entry(self)

            else:
                finished = raw_input("Are you finished using the Phonebook? Yes or No. ").lower()
                if finished == 'yes':
                    print("Thank you for using the Phonebook.")
                    print(phonebook)
                else:
                    entry()
    entry()


