from categoria import Categoria
from cliente_rede_social import Cliente_rede_social
from rede_social import Rede_social

def main():    
    cat = Categoria(123, 'Chá','Chás de todos os sabores')
    clrs = Cliente_rede_social('Luigi','luigivibias11@gmail.com')
    rs = Rede_social('e-mail', 'luigivibias11@gmail.com')
    print(cat.nome())
    print(clrs.cliente())
    print(rs.descricao())

if __name__ == "__main__":
    main()