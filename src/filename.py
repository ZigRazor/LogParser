from .genericElement import GenericElement

class Filename(GenericElement):
    """Filename Class"""
    def __init__(self):
        """Constructor of Filename Class"""
        super().__init__()
        self.name = ""

    def set_name(self, name):
        """Set the name of the file"""
        self.name = name
    
    def get_name(self):
        """Get the name of the file"""
        return self.name
    
    def __str__(self):
        """Return a string representation of the object"""
        return self.name

    def __repr__(self):
        """Return a string representation of the object"""
        return self.name

    def __eq__(self, other):
        """Compare two objects"""
        return self.name == other.name
    
    def __hash__(self):
        """Return the hash of the object"""
        return hash(self.name)

    def __lt__(self, other):
        """Compare two objects"""
        return self.name < other.name

    def __le__(self, other):
        """Compare two objects"""
        return self.name <= other.name

    def __gt__(self, other):
        """Compare two objects"""
        return self.name > other.name

    def __ge__(self, other):
        """Compare two objects"""
        return self.name >= other.name

    def __ne__(self, other):
        """Compare two objects"""
        return self.name != other.name

    