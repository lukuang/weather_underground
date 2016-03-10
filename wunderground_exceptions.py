"""
define Exceptions
"""


class NoSuchCountryException(Exception):
    def __init__(self,name):
        self.name = name

    def __str__():
        error_message = "Cannot find country named %s" %self.name
        return error_message


class NoSuchMappingException(Exception):
    def __init__(self,name):
        self.name = name

    def __str__():
        error_message = "Cannot find mapping for country named %s" %self.name
        return error_message

class NoKeyFileException(Exception):
    def __init__(self,key_file_path):
        self.key_file_path = key_file_path

    def __str__():
        error_message = "No such key file %s" %self.key_file_path
        return error_message