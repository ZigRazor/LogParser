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

    def add_key(self, key):
        """Add key to keys"""
        self.keys.append(key)

    def remove_key(self, key):
        """Remove key from keys"""
        self.keys.remove(key)
    
    def parse_log(self):
        """Parse log files"""
        for file in self.file_list:
            with open(file, 'r') as f:
                for line in f:
                    #TODO: parse line
                    pass
