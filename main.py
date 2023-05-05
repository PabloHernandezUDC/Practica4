# Pablo Hernandez Martinez, pablo.hernandez.martinez@udc.es - Marcelo Ferreiro Sánchez, marcelo.fsanchez@udc.es
import time
from activity import Activity
from avl_tree import AVL

def print_indented_activity_tree(T, p, d):
    '''
    Taken from avl_tree, slightly modified.
    This function lets us print with indents any tree with activity objects.
    '''
    if p is not None:
        print(4*d*' ' + "(" + str(p.key()) + ",", f'coste: {round(p.value().get_total_needed_resources(), 2)}' + ")") # showing total cost for each activity
        print_indented_activity_tree(T, T.left(p), d+1)
        print_indented_activity_tree(T, T.right(p), d+1)

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
    with open(path, encoding='utf-8') as f:
        tree = AVL()
        for element in f.readlines()[1:]: # we skip the first one since its just a header line
            current_activity = Activity(*(element.split(';')))
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
    result_tree = AVL()
    result_tree.update(tree1)

    for i in tree2:
        if i not in result_tree or tree2[i] < result_tree[i]:
            result_tree[i] = tree2[i]
    
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
    node1_position, node2_position = tree1.first(), tree2.first()
    
    while node1_position is not None and node2_position is not None:
        node1_object, node2_object = node1_position.key(), node2_position.key()
                
        if node1_object == node2_object:
            if node1_object < node2_object:
                result_tree[node1_object] = tree1[node1_object]
            else:
                result_tree[node2_object] = tree2[node2_object]
            node1_position, node2_position = tree1.after(node1_position), tree2.after(node2_position)
        elif node1_object < node2_object:
            node1_position = tree1.after(node1_position)
        else:
            node2_position = tree2.after(node2_position)

    return result_tree

if __name__ == "__main__":
    start_time = time.perf_counter_ns() # starting the timer to test performance at the end
    tree_A = create_activity_tree('actividadesA.txt')
    tree_B = create_activity_tree('actividadesB.txt')
    tree_sum = activity_sum(tree_A, tree_B)
    tree_mins_shared = min_shared_offer(tree_A, tree_B)
    end_time = time.perf_counter_ns() # getting the end time to print it later
     
    print('\nSuma de actividades:')
    print_indented_activity_tree(tree_sum, tree_sum.root(), 0)
    print('Oferta mínima común:')
    print_indented_activity_tree(tree_mins_shared, tree_mins_shared.root(), 0)
    
    print(f'Tiempo de ejecución: {(end_time - start_time) / (10**6)}ms.\n') # print execution time converted to miliseconds