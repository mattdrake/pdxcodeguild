name = raw_input('What is your name? ')
location = raw_input('Where are you from? ')
transportation = raw_input('Did you arrive by driving, walking, or using public transportation? ')
hobby = raw_input('What do you like to do in your spare time? ')
dislike = raw_input('What do you really hate? ')

story = """Hello, my name is %(name)s. I'm from %(location)s. I arrived here by %(transportation)s. In my spare time I like to %(hobby)s. I really hate %(dislike)s."""

variables = {'name': name.capitalize(), 'location': location.capitalize(), 'transportation': transportation, 'hobby': hobby, 'dislike': dislike}

print (story % variables)

