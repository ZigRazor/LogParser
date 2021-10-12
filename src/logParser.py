import re
import copy
from . import genericElement
from . import date
from . import severity
from . import filename


class LogParser:
    """LogParser Class"""

    def __init__(self):
        """Constructor of LogParser Class"""
        self.file_list = []
        self.elements = {}
        self.keys = []

    def add_file(self, _filename: str):
        """Add file to file_list"""
        self.file_list.append(_filename)

    def remove_file(self, _filename: str):
        """Remove file from file_list"""
        self.file_list.remove(_filename)

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
        if key not in self.elements:
            raise Exception("Key not present in Elements")
        if key in self.keys:
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

    def add_element(self, key: str, value: genericElement.GenericElement):
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
        print(self.keys)
        for key in self.keys:
            result[key] = {}
        for file in self.file_list:
            with open(file, 'r') as f:
                for line in f:
                    # print(line)
                    for element in self.elements.items():
                        if isinstance(element[1], filename.Filename):
                            element[1].set_name(file)
                            if element[0] in self.keys:
                                result[element[0]][copy.deepcopy(
                                    element[1])] = None
                        else:
                            # print(element)
                            regex = re.compile(element[1].get_format())
                            # print(regex)
                            match = regex.search(line)
                            print(match)
                            if match:
                                if isinstance(element[1], date.Date):
                                    element[1].set_date_from_string(
                                        match.group())
                                    print(element)
                                    if element[0] in self.keys:
                                        result[element[0]][copy.deepcopy(
                                            element[1])] = None
                                elif isinstance(element[1], severity.Severity):
                                    element[1].set_severity_from_string(
                                        match.group())
                                    print(element)
                                    if element[0] in self.keys:
                                        result[element[0]][copy.deepcopy(
                                            element[1])] = None
                                else:
                                    raise Exception("Not Known Element Type")
                            else:
                                raise Exception("No Match")
                            # pass
        print(result)
        return True
