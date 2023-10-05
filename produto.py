class Produto:
    def __init__(self, nome, descricao, data_fabricacao, e_ativo, categoria):
        self.nome = nome
        self.descricao = descricao
        self.data_fabricacao = data_fabricacao
        self.e_ativo = e_ativo
        self.categoria = categoria
    
    def verificarData(self):
        return self.data_fabricacao