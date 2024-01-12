


def is_tuple_or_list(Objeto):
    if not isinstance(Objeto,(list,tuple,dict)):
        raise TypeError('Objeto precisa ser uma lista ou tupla.')
tupla = ('Salvador', 'Ubatuba', 'Belo Horizonte','Rio de Janeiro','Porto Alegre','Belém')

