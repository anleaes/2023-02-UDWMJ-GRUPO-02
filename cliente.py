class Cliente:
    def __init__(self, primeiro_nome, ultimo_nome, endereco, telefone, email, genero):
        self.primeiro_nome = primeiro_nome
        self.ultimo_nome = ultimo_nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.genero = genero
    def endemail(self):
        return self.email 