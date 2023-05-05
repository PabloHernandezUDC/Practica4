# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from activity import Activity
from avl_tree import AVL

def print_indented_activity_tree(T, p, d):
    '''
    Taken from avl_tree., slightly modifed
    This function lets us print any tree with indents representing hierarchy.
    '''
    if p is not None:
        print(4*d*' ' + "(" + str(p.key()) + ",", f'coste: {round(p.value().get_total_needed_resources(), 2)}' + ")") 
        print_indented_activity_tree(T, T.left(p), d+1)
        print_indented_activity_tree(T, T.right(p), d+1)

def create_activity_from_line(params):
    '''
    '''
    name, duration, participants, cost = params
    return Activity(name, duration, participants, cost)

def create_activity_tree(path):
    '''
    '''
    with open(path) as f:
        tree = AVL()
        for element in f.readlines()[1:]: # we skip the first one since its just a header line
            current_activity = create_activity_from_line(element.split(';'))
            tree[current_activity.get_name().lower()] = current_activity
    return tree

def activity_sum(tree1, tree2):
    '''
    '''
    result_tree = AVL()
    print('Procediendo a crear la suma de actividades...')

    for i in tree1:
        result_tree[i] = tree1[i]
    for i in tree2:
        if i not in tree1 or tree2[i] < tree1[i]:
            result_tree[i] = tree2[i]
    
    print('La suma de actividades ha sido creada.\n')
    return result_tree

def min_shared_offer(tree1, tree2):
    '''
    '''
    result_tree = AVL()
    print('\nProcediendo a encontrar la oferta mínima común...')

    for i in tree1:
        if i in tree2:            
            if tree1[i] < tree2[i]:
                result_tree[i] = tree1[i]
            else:
                result_tree[i] = tree2[i]
    
    print('Ya hemos encontrado la oferta mínima común.')
    return result_tree

if __name__ == "__main__":
    print('\nIniciando el programa...')
    tree_A = create_activity_tree('actividadesA.txt')
    tree_B = create_activity_tree('actividadesB.txt')
    print('Los árboles han sido creados.\n')
    
    tree_C = activity_sum(tree_A, tree_B)
    print_indented_activity_tree(tree_C, tree_C.root(), 0)
    
    tree_C = min_shared_offer(tree_A, tree_B)
    print_indented_activity_tree(tree_C, tree_C.root(), 0)
    print('\nFin de la ejecución.\n')