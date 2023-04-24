# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es

def create_book_from_line(params):
    '''
    '''
    titulo, autor = params[0:2]
    año, prestamos = int(params[2]), int(params[3])
    
    return Book(titulo, autor, año, prestamos)

def create_book_list(path, t):
    '''
    '''
    with open(path) as f:
        if t == 1:
            book_list = PositionalList1()
        else:
            book_list = PositionalList2()

        for elemento in f.readlines():
            book_list.add(create_book_from_line(elemento.split('; ')))
            
    return book_list


if __name__ == "__main__":
    pass