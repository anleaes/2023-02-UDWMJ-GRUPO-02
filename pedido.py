class Pedido:
    def __init__(self, preco_total, status, cliente):
        self.preco_total = preco_total
        self.status = status
        self.cliente = cliente
    def situstatus(self):
        return self.status