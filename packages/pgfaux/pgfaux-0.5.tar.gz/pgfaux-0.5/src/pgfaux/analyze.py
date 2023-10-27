# -*- coding: utf-8 -*-

import pgf
import hashlib
import graphviz
import os

EMPTY="?"
SYMB="symb"

def get_image(dot_code: str,tree_str: str,suffix='',filename=None,dir='.',format = 'png'):
    if not filename:
        hash_object = hashlib.md5(tree_str.encode())
        filename_base = hash_object.hexdigest()+suffix
    else:
        filename_base = filename
    dot_filename = os.path.join(dir,filename_base + '.dot')
    img_filename = dot_filename + '.' + format
    dot_graph = graphviz.Source(dot_code)
    dot_graph.format = format
    dot_graph.render(dot_filename)
    return img_filename

def get_abs_image(tree,grammar,filename=None,dir='.',format = 'png'):
    '''Given a pgf.Expr tree and a pgf.Concr module, creates an abstract syntax
       image using Graphviz and returns the file name.'''
    dot_code = grammar.graphvizAbstractTree(tree)
    tree_str = str(tree)
    return get_image(dot_code,tree_str,'_abs',filename,dir,format)

def get_parse_image(tree,concrete,filename=None,dir='.',format = 'png'):
    '''Given a pgf.Expr tree and a pgf.Concr module, creates a parse syntax
       image using Graphviz and returns the file name.'''
    dot_code = concrete.graphvizParseTree(tree)
    tree_str = str(tree)
    return get_image(dot_code,tree_str,'_parse',filename,dir,format)

def node_is_empty(tree):
    '''Checks whether a pgf.Expr tree is empty'''
    tree = pgf.readExpr(str(tree))
    if not tree.unpack()[0]:
        return True
    return False

def is_equal(tree1,tree2):
    '''Naïve equivalence check between two pgf.Expr trees or their string representations'''
    if str(tree1) == str(tree2):
        return True
    return False

def depth(tree):
    '''Calculates the depth of a pgf.Expr tree or its string representation'''
    tree = pgf.readExpr(str(tree))
    children = children_trees(tree)
    if len(children) == 0:
        return 0
    children_lens = []
    for c in children:
        children_lens.append(depth(c))
    return max(children_lens) + 1

def root_str(tree):
    '''Gives the root function of a pgf.Expr tree as a string'''
    tree = pgf.readExpr(str(tree))
    try:
        (fun_str,children) = tree.unpack()
        return fun_str
    except ValueError:
        return str(tree)
    except AttributeError:
        return str(tree)
    except TypeError:
        return str(tree)

def root_cat(tree,grammar):
    '''Gives the root category of a pgf.Expr tree as a string'''
    tree = pgf.readExpr(str(tree))
    try:
        fun_str = root_str(tree)
        if fun_str:
            fun_type = grammar.functionType(fun_str)
            return fun_type.cat
        else:
            return EMPTY
    except KeyError:
        return SYMB

def children_trees(tree):
    '''Provides a list of direct children of a pgf.Expr tree'''
    tree = pgf.readExpr(str(tree))
    try:
        (fun_str,children) = tree.unpack()
        return children
    except ValueError:
        return []
    except AttributeError:
        return []
    except TypeError:
        return []

def subtrees_of_cat(tree,cat: str,grammar,overlap=True):
    '''Provides a list of subtrees of a pgf.Expr tree by category'''
    tree = pgf.readExpr(str(tree))
    trees = []
    children = children_trees(tree)
    if root_cat(tree,grammar) == cat:
        if overlap:
            trees.append(tree)
        else:
            return [tree]
    if len(children) == 0:
        return trees
    for c in children_trees(tree):
        trees += subtrees_of_cat(c,cat,grammar,overlap)
    return trees

def subtrees_of_fun(tree,fun: str,overlap=True):
    '''Provides a list of subtrees of a pgf.Expr tree by function'''
    tree = pgf.readExpr(str(tree))
    trees = []
    children = children_trees(tree)
    if root_str(tree) == fun:
        if overlap:
            trees.append(tree)
        else:
            return [tree]
    if len(children) == 0:
        return trees
    for c in children_trees(tree):
        trees += subtrees_of_fun(c,fun,overlap)
    return trees

def sanity_check_tree(tree,grammar):
    '''Simple sanity check using checkExpr'''
    tree = pgf.readExpr(str(tree))
    try:
        f_cat = root_cat(tree,grammar)
        grammar.checkExpr(tree,pgf.readType(f_cat))
        return True
    except Exception as e:
        return False

def leaf_function_names_by_cat(cat: str,grammar) -> 'list[str]':
    '''List of pgf.Expr trees with depth 0 by category'''
    function_names = grammar.functionsByCat(cat)
    leaf_function_names = []
    for f in function_names:
        fun_type = grammar.functionType(f)
        args,cat,x = fun_type.unpack()
        if len(args) == 0:
            leaf_function_names.append(f)
    return leaf_function_names

def alternative_leaf_function_names(tree,grammar,conc_name):
    '''List of alternative pgf.Expr trees of depth 0 for a given tree'''
    concrete = grammar.languages[conc_name]
    tree = pgf.readExpr(str(tree))
    fun_name = root_str(tree)
    fun_cat = root_cat(tree,grammar)
    leaf_nodes = leaf_nodes_with_ids(tree)
    all_funs = leaf_function_names_by_cat(fun_cat,grammar)
    all_leaf_funs = [f for f in all_funs if depth(f) == 0 and concrete.hasLinearization(f)]
    other_leaf_funs = [f for f in all_leaf_funs if f != fun_name]
    return [fun_name] + other_leaf_funs

def _leaf_nodes_with_ids(tree,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    children = children_trees(tree)
    leaves = []
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        return [(tree,cur_id)],cur_id
    for c in children:
        new_leaves,prev_id = _leaf_nodes_with_ids(c,prev_id)
        leaves += new_leaves
        cur_id = prev_id + 1
    return leaves,cur_id

def leaf_nodes_with_ids(tree):
    '''List of a pgf.Expr tree's leaf nodes with their postfix id's'''
    leaves,root_id = _leaf_nodes_with_ids(tree,-1)
    return leaves

def _empty_node_ids(tree,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    empty_ids = []
    if str(tree) == EMPTY:
        cur_id = prev_id + 1
        return empty_ids + [cur_id],cur_id
    children = children_trees(tree)
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        return empty_ids,cur_id
    for c in children:
        new_ids,prev_id = _empty_node_ids(c,prev_id)
        empty_ids += new_ids
        cur_id = prev_id + 1
    return empty_ids,cur_id

def empty_node_ids(tree):
    '''List of empty nodes in a pgf.Expr with their postfix id's'''
    empty_ids,root_id = _empty_node_ids(tree,-1)
    return empty_ids

def _fun_node_ids(tree,fun,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    fun_ids = []
    found_this_node = False
    if root_str(tree) == fun:
        cur_id = prev_id + 1
        found_this_node = True
    children = children_trees(tree)
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        if found_this_node:
            fun_ids.append(cur_id)
        return fun_ids,cur_id
    for c in children:
        new_ids,prev_id = _fun_node_ids(c,fun,prev_id)
        fun_ids += new_ids
        cur_id = prev_id + 1

    if found_this_node:
        fun_ids.append(cur_id)
    return fun_ids,cur_id

def fun_node_ids(tree,fun: str):
    '''List of postfix id's of nodes by function'''
    fun_ids,root_id = _fun_node_ids(tree,fun,-1)
    return fun_ids

def _cat_node_ids(tree,cat,grammar,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    cat_ids = []
    found_this_node = False
    if root_cat(tree,grammar) == cat:
        cur_id = prev_id + 1
        found_this_node = True
    children = children_trees(tree)
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        if found_this_node:
            cat_ids.append(cur_id)
        return cat_ids,cur_id
    for c in children:
        new_ids,prev_id = _cat_node_ids(c,cat,grammar,prev_id)
        cat_ids += new_ids
        cur_id = prev_id + 1
    
    if found_this_node:
        cat_ids.append(cur_id)
    return cat_ids,cur_id

def cat_node_ids(tree,cat: str,grammar):
    '''List of postfix id's of nodes by category'''
    cat_ids,root_id = _cat_node_ids(tree,cat,grammar,-1)
    return cat_ids

def _subtree_node_ids(tree,subtree,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    found_this_node = False
    sub_ids = []
    if str(tree) == str(subtree):
        cur_id = prev_id + 1
        found_this_node = True
    children = children_trees(tree)
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        if found_this_node:
            sub_ids.append(cur_id)
        return sub_ids,cur_id
    for c in children:
        new_ids,prev_id = _subtree_node_ids(c,subtree,prev_id)
        sub_ids += new_ids
        cur_id = prev_id + 1
    if found_this_node:
        sub_ids.append(cur_id)
    return sub_ids,cur_id

def subtree_node_ids(tree,subtree):
    '''List of postfix id's of nodes matching pgf.Expr subtree'''
    sub_ids,root_id = _subtree_node_ids(tree,subtree,-1)
    return sub_ids

def _subtree_at_id(tree,sub_id,prev_id=-1):
    tree = pgf.readExpr(str(tree))
    children = children_trees(tree)
    if len(children) == 0: # tree is a leaf
        cur_id = prev_id + 1
        if cur_id == sub_id:
            return tree,cur_id
    for c in children:
        found,prev_id = _subtree_at_id(c,sub_id,prev_id)
        cur_id = prev_id + 1
        if found:
            return found,cur_id
        
    if cur_id == sub_id:
        return tree,cur_id
    return None,cur_id

def subtree_at_id(tree,sub_id: int):
    '''pgf.Expr at postfix id'''
    subtree,root_id = _subtree_at_id(tree,sub_id,-1)
    return subtree

def _path_to_root(tree,id,prev_id=-1,path=[]):
    tree = pgf.readExpr(str(tree))
    children = children_trees(tree)
    if len(children) == 0: # leaf node
        cur_id = prev_id + 1
        if cur_id == id:
            path.append((root_str(tree),cur_id))
            # print(f'path is: {path}')
    else:
        parent_state = [p for p in path]
        for c in children:
            path,prev_id = _path_to_root(c,id,prev_id,path)
            cur_id = prev_id + 1
        if tuple(parent_state) != tuple(path):
            path.append((root_str(tree),cur_id))
        if cur_id == id:
            path.append((root_str(tree),cur_id))

    return path,cur_id

def path_to_root(tree,id: int):
    '''Path of nodes from node with postfix id to root, by function name'''
    path,root_id = _path_to_root(tree,id,prev_id=-1,path=[])
    return path

def size(tree,prev_id=-1):
    '''Counts the number of nodes in a pgf.Expr tree'''
    tree = pgf.readExpr(str(tree))
    children = children_trees(tree)
    if len(children) == 0: # leaf node
        cur_id = prev_id + 1
    else:
        for c in children:
            prev_id = size(c,prev_id)
            cur_id = prev_id + 1

    return cur_id
