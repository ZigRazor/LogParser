import re
import GenericElement

class LogParser:
    """LogParser Class"""
    def __init__(self):
        """Constructor of LogParser Class"""
        self.file_list = []
        self.elements = {}
        self.keys = []

    def add_file(self, filename : str):
        """Add file to file_list"""
        self.file_list.append(filename)

    def remove_file(self, filename : str):
        """Remove file from file_list"""
        self.file_list.remove(filename)

    def clear_file_list(self):
        """Clear file list"""
        self.file_list.clear()
    
    def get_file_list_string(self):
        """Get file list string"""
        return '\n'.join(self.file_list)    
    
    def get_file_list(self):
        """Get file list"""
        return self.file_list

    def get_file_count(self):
        """Get file count"""
        return len(self.file_list)

    def get_key_count(self):
        """Get key count"""
        return len(self.keys)
    
    def get_key_list(self):
        """Get key list"""
        return self.keys

    def get_key_list_string(self):
        """Get key list string"""
        return '\n'.join(self.keys)

    def add_key(self, key: str):
        """Add key to keys"""
        if(key not in self.elements):
            raise Exception("Key not present in Elements")
        if(key in self.keys):
            raise Exception("Key already present in Keys")
        self.keys.append(key)

    def remove_key(self, key: str):
        """Remove key from keys"""
        self.keys.remove(key)

    def clear_keys(self):
        """Clear keys"""
        self.keys.clear()
    
    def clear_elements(self):
        """Clear elements"""
        self.elements.clear()
        self.keys.clear()   

    def get_element_count(self):
        """Get element count"""
        return len(self.elements)

    def get_element_list(self):
        """Get element list"""
        return self.elements

    def get_element_list_string(self):
        """Get element list string"""
        return '\n'.join(self.elements)
    
    def add_element(self, key: str, value: GenericElement.GenericElement):
        """Add element to elements"""
        self.elements[key] = value

    def remove_element(self, key: str):
        """Remove element from elements"""
        self.elements.pop(key)
        if key in self.keys:
            self.keys.remove(key)
            
    def parse_log(self):
        """Parse log files"""
        result = {}
        for key in self.keys:
            result[key] = {}
        for file in self.file_list:
            with open(file, 'r') as f:
                for line in f:
                    print (line)
                    for element in self.elements.items():
                        print (element)
                        regex = re.compile(element[1].get_format())
                        print (regex)
                        match = regex.search(line)
                        element[1].set_date_from_string(match.group())
                        print (match)
                        print (element)
                        #pass
        return True