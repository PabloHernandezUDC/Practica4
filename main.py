# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from activity import Activity
from avl_tree import AVL

def create_activity_from_line(params):
    '''
    '''
    name, duration, participants, cost = params
    
    try:
        duration, participants, cost = int(duration), int(participants), int(cost)
    except ValueError:
        pass
    
    return Activity(name, duration, participants, cost)

def create_activity_tree(path):
    '''
    '''
    with open(path) as f:
        tree = AVL()
        for elemento in f.readlines():
            current_activity = create_activity_from_line(elemento.split(';'))
            if current_activity.get_name().lower() != 'nombre':
                tree[current_activity.get_name().lower()] = current_activity
            
    return tree

if __name__ == "__main__":
    create_activity_tree('actividadesA.txt')
    pass