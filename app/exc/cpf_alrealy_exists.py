class CpfAlrealyExists(Exception):
    def __init__(self):
        self.message = {"error": "Alrealy exists an people with this cpf"}, 409
