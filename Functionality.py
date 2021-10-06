import GenericElement

class Functionality(GenericElement.GenericElement):
    """ Functionality Class"""
    def __init__(self):
        """Constructor of Functionality Class"""
        self.name = ""

    def set_name(self, name):
        """Setter of name"""
        self.name = name
    
    def get_name(self):
        """Getter of name"""
        return self.name
    
    def __str__(self):
        """String representation of Functionality Class"""
        return "Functionality: " + self.name
    
    def __repr__(self):
        """String representation of Functionality Class"""
        return "Functionality: " + self.name
    
    def __eq__(self, other):
        """Equality of Functionality Class"""
        return self.name == other.name
    
    def __hash__(self):
        """Hash of Functionality Class"""
        return hash(self.name)
    
    def __lt__(self, other):
        """Less than of Functionality Class"""
        return self.name < other.name
    
    def __le__(self, other):
        """Less than or equal to of Functionality Class"""
        return self.name <= other.name
    
    def __gt__(self, other):
        """Greater than of Functionality Class"""
        return self.name > other.name
    
    def __ge__(self, other):
        """Greater than or equal to of Functionality Class"""
        return self.name >= other.name
    
    def __ne__(self, other):
        """Not equal to of Functionality Class"""
        return self.name != other.name
    
    