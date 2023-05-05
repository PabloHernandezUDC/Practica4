# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
from activity import Activity
from avl_tree import AVL
import time

def print_indented_activity_tree(T, p, d):
    '''
    Taken from avl_tree, slightly modified.
    This function lets us print with indents any tree with activity objects.
    '''
    if p is not None:
        print(4*d*' ' + "(" + str(p.key()) + ",", f'coste: {round(p.value().get_total_needed_resources(), 2)}' + ")") 
        print_indented_activity_tree(T, T.left(p), d+1)
        print_indented_activity_tree(T, T.right(p), d+1)

def create_activity_from_line(params):
    '''
    Creates an activity object from the list of parameters.

    Parameters
    ----------
        params (list): List of parameters of an activity.

    Returns
    -----------
        Activity: An activity object created from the list of parameters.
    '''
    name, duration, participants, cost = params
    return Activity(name, duration, participants, cost)

def create_activity_tree(path):
    '''
    Creates a tree of activity nodes from a file.

    Parameters
    -----------
        path (str): Path of the file containing the activities.

    Returns
    --------
        tree: An AVL tree of activity nodes created from the file.
    '''
    with open(path) as f:
        tree = AVL()
        for element in f.readlines()[1:]: # we skip the first one since its just a header line
            current_activity = create_activity_from_line(element.split(';'))
            tree[current_activity.get_name().lower()] = current_activity
    return tree

def activity_sum(tree1, tree2):
    '''
    Calculates the sum of two AVL trees of activity nodes.

    Parameters
    ----------
        tree1 (AVL): First AVL tree of activity nodes.
        tree2 (AVL): Second AVL tree of activity nodes.

    Returns
    ----------
        result_tree: An AVL tree of activity nodes containing the sum of the two AVL trees.
    '''
    print('Procediendo a crear la suma de actividades...')

    result_tree = AVL()
    result_tree.update(tree1)

    for i in tree2:
        if i not in result_tree or tree2[i] < result_tree[i]:
            result_tree[i] = tree2[i]
    
    print('La suma de actividades ha sido creada.\n')
    return result_tree

def min_shared_offer(tree1, tree2):
    '''
    Calculates the minimum shared offer of two AVL trees of activity nodes.

    Parameters:
        tree1 (AVL): First AVL tree of activity nodes.
        tree2 (AVL): Second AVL tree of activity nodes.

    Returns:
       result_tree: An AVL tree of activity nodes containing the minimum shared offer of the two AVL trees.
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
    start_time = time.perf_counter_ns() # starting the timer to test performance at the end
    print('\nIniciando el programa...')
    tree_A = create_activity_tree('actividadesA.txt')
    tree_B = create_activity_tree('actividadesB.txt')
    print('Los árboles han sido creados.\n')
    
    tree_C = activity_sum(tree_A, tree_B)
    #print_indented_activity_tree(tree_C, tree_C.root(), 0)
    
    tree_C = min_shared_offer(tree_A, tree_B)
    #print_indented_activity_tree(tree_C, tree_C.root(), 0)
    
    end_time = time.perf_counter_ns() # getting the final time
    print(f"\nTiempo de ejecución: {(end_time - start_time) / (10**6)}ms.\n") # printing it in miliseconds