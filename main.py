from cliente import Cliente
from pedido import Pedido

def main():
    C1 = Cliente('Luigi', 'veloso',  'Rua manoel', '51 9999 9999', 'luigi_vava@hotmail.com', 'M')
    pd1 = Pedido(16.00, 'ativo', 'Luigi')
    print(C1.email())
    print(pd1.status())

if __name__ == "__main__":
    main()