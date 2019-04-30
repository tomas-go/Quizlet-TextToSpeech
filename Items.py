

# Class for the items belong to each subject.
class Item:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def all_info(self):
        return "Term: " + self.term + "\nDefinition: " + self.definition + "\n"