from cliente import Cliente
from pedido import Pedido
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
    print(cat.verificarNome())
    print(clrs.verificarCliente())
    print(rs.verificarDescricao())
    
    C1 = Cliente('Luigi', 'veloso',  'Rua manoel', '51 9999 9999', 'luigi_vava@hotmail.com', 'M')
    pd1 = Pedido(16.00, 'ativo', 'Luigi')
    print(C1.endemail())
    print(pd1.situstatus())

if __name__ == "__main__":
    main()