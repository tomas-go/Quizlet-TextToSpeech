

# Class for the flashcard groups.
# Includes functions that get all info from each group
class Subject:
    def __init__(self, name, num_of_terms, link):
        self.name = name
        self.num_of_terms = num_of_terms
        self.link = link

    def info(self):
        return "Group:" + self.name + "has " + self.num_of_terms + "terms."

    def all_info(self):
        print("Name: " + str(self.name) + "\nNumber of Terms: " + str(self.num_of_terms) + "\nLink: " + str(self.link))
        print("---------------------------------")

