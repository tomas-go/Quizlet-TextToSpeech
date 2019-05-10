# File for all classes used

# Class for the items belong to each subject.
class Item:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def all_info(self):
        return "Term: " + self.term + "\nDefinition: " + self.definition + "\n"


# Class for the flashcard groups.
# Includes functions that get all info from each group
class Subject:
    def __init__(self, name, num_of_terms, link):
        self.name = name
        self.num_of_terms = num_of_terms
        self.link = link

    def info(self):
        return self.name + " (" + self.num_of_terms + " terms)"

    def all_info(self):
        return "Name: " + str(self.name) + "\nNumber of Terms: " + str(self.num_of_terms) + "\nLink: " + str(self.link)


# Exception when the flashcard group has no items
class NoItemsToConvert(Exception):
    pass