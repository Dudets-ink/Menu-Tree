def build_parent(level):
    parent = 'parent'
    parent_list = [parent]
    for i in range(level):
        parent += '__parent'
        parent_list.append(parent)
    return parent_list
