#Prompting user for input.
name = raw_input('\033[0;34mWhat is your name?\033[0;m ')
location = raw_input('Where are you from? ')
transportation = raw_input('\033[0;34mDid you arrive by driving, walking, or using public transportation?\033[0;m ')
hobby = raw_input('What do you like to do in your spare time? ')
dislike = raw_input('\033[0;34mWhat do you really hate?\033[0;m ')

#Story that input will be put into.
story = """
\033[1;42mHello, my name is %(name)s. I'm from %(location)s. 
I arrived here by %(transportation)s. In my spare time I like to %(hobby)s. 
I really hate %(dislike)s.\033[1;m"""

#variables being replaced inside story with user prompts.
variables = {'name': name.capitalize(), 'location': location.capitalize(), 'transportation': transportation, 'hobby': hobby, 'dislike': dislike}

#end result running story. 
print (story % variables)


