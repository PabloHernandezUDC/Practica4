# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es

def create_element(path):
    '''
    '''
    with open(path) as f:
        for elemento in f.readlines():
           print(elemento.split('; '))
            
    return None

if __name__ == "__main__":
    create_element('actividadesA.txt')
    pass