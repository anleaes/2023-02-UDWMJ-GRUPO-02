from item_pedido import Item_pedido
from produto import Produto
from categoria import Categoria
from cliente_rede_social import Cliente_rede_social
from rede_social import Rede_social


def main():
    itp1 = Item_pedido(100, 16.00, 'Erva', 'Erva mate')
    pr1 = Produto('Erva Mate', 'Erva especializada para chimas', '5/10/23', 'SIM', 'Chás')
    print(itp1.verificarPedido())
    print(pr1.verificarData())
    
    cat = Categoria(123, 'Chá','Chás de todos os sabores')
    clrs = Cliente_rede_social('Luigi','luigivibias11@gmail.com')
    rs = Rede_social('e-mail', 'luigivibias11@gmail.com')
    print(cat.nome())
    print(clrs.cliente())
    print(rs.descricao())


if __name__ == "__main__":
    main()