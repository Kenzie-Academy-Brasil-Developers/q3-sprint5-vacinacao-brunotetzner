class InvalidKeyValue(Exception):
    def __init__(self, invalid_key):
        self.message = {
            "error": 
            f"The keys {invalid_key} have invalid values. All the keys needs to are strings"
            }, 400