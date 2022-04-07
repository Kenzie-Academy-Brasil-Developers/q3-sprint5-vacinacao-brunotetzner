class NotFoundKey(Exception):
    def __init__ (self, valid_keys, not_found_keys):
        self.message = {
            "error":
             f"The keys {valid_keys} are require, but the keys {not_found_keys} are not received"
             }, 400