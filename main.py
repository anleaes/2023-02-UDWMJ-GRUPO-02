from item_pedido import Item_pedido
from produto import Produto

def main():
    itp1 = Item_pedido(100, 16.00, 'Erva', 'Erva mate')
    pr1 = Produto('Erva Mate', 'Erva especializada para chimas', '5/10/23', 'SIM', 'Chás')
    print(itp1.verificarPedido())
    print(pr1.verificarData())

if __name__ == "__main__":
    main()