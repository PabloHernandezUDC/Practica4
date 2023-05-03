# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from activity import Activity
from avl_tree import AVL
import time

def print_indented_tree(T, p, d):
    '''
    Taken from avl_tree.
    This function lets us print any tree with indents representing hierarchy.
    '''
    if p is not None:
        print(2*d*' ' + "(" + str(p.key()) + "," + str(p.value()) + ")") 
        print_indented_tree(T, T.left(p), d+1)
        print_indented_tree(T, T.right(p), d+1)

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

    for leaf in tree1:
        result_tree[leaf] = tree1[leaf]
    for leaf in tree2:
        if leaf not in tree1 or tree2[leaf] < tree1[leaf]:
            result_tree[leaf] = tree2[leaf]
    
    print('La suma de actividades ha sido creada.\n')
    return result_tree

def min_shared_offer(tree1, tree2):
    '''
    '''
    result_tree = AVL()
    print('\nProcediendo a encontrar la oferta mínima común...')

    for leaf in tree1:
        if leaf in tree2:            
            if tree1[leaf] < tree2[leaf]:
                result_tree[leaf] = tree1[leaf]
            else:
                result_tree[leaf] = tree2[leaf]
    
    print('Ya hemos encontrado la oferta mínima común.')
    return result_tree

if __name__ == "__main__":
    start_time = time.perf_counter_ns()
    print('\nIniciando el programa...')
    tree_A = create_activity_tree('actividadesA.txt')
    tree_B = create_activity_tree('actividadesB.txt')
    print('Los árboles han sido creados.\n')
    
    sum_tree = activity_sum(tree_A, tree_B)
    print_indented_tree(sum_tree, sum_tree.root(), 0)
    
    common_tree = min_shared_offer(tree_A, tree_B)
    print_indented_tree(common_tree, common_tree.root(), 0)
    print('\nFin de la ejecución.\n')
    
    end_time = time.perf_counter_ns()
    print(f"Tiempo de ejecución {(end_time - start_time)/(10**6)} ms.\n")