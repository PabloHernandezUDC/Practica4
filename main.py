# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from activity import Activity
from avl_tree import AVL

def print_indented_tree(T, p, d):
    '''
    robado
    '''
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        print_indented_tree(T, T.left(p), d+1) # left child depth is d+1
        print_indented_tree(T, T.right(p), d+1) # right child depth is d+1

def create_activity_from_line(params):
    '''
    TODO: arreglar pa q furrule si es todo strings.
    '''
    name, duration, participants, cost = params
    return Activity(name, duration, participants, cost)

def create_activity_tree(path):
    '''
    '''
    with open(path) as f:
        tree = AVL()
        for elemento in f.readlines()[1:]:
            current_activity = create_activity_from_line(elemento.split(';'))
            tree[current_activity.get_name().lower()] = current_activity
            
    return tree

if __name__ == "__main__":
    tree_A = create_activity_tree('actividadesA.txt')
    tree_B = create_activity_tree('actividadesB.txt')
    
    print_indented_tree(tree_A, tree_A.root(), 0)
    print_indented_tree(tree_B, tree_B.root(), 0)