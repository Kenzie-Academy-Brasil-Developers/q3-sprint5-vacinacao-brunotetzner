class InvalidCpf(Exception):
    def __init__(self, cpf): 
        self.cpf = cpf,
        self.message = {"error": f"The cpf {self.cpf} needs have eleven caracteres"}, 400

    
