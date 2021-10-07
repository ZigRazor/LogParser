class GenericElement:
    """GenericElement Class"""
    def __init__(self):
        """Constructor of Generic Element Class"""
        self.element_name = ""
        self.format = None
    
    def set_element_name(self, element_name):
        """Setter for element name"""
        self.element_name = element_name

    def set_format(self, format):
        """Setter for format"""
        self.format = format

    def get_element_name(self):
        """Getter for element name"""
        return self.element_name

    def get_format(self):
        """Getter for format"""
        return self.format

    def __str__(self):
        """String representation of the class"""
        return self.element_name + " " + self.format

    def __repr__(self):
        """Representation of the class"""
        return self.element_name + " " + self.format

    def __eq__(self, other):
        """Equality operator"""
        return self.element_name == other.element_name and self.format == other.format
    
    def __ne__(self, other):
        """Inequality operator"""
        return not self.__eq__(other)

    def __hash__(self):
        """Hash function"""
        return hash(self.element_name) ^ hash(self.format)

