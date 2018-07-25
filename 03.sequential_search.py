def sequential_search(item_list, search_item):
    found = False
    for position in range(len(item_list)):
        if item_list[position] == search_item:
            found = True
            print('Got it at position', position)
            break
    return found

item_list = [11, 23, 58, 31, 56, 77, 43, 12, 65, 19]
search_item = 77

print(sequential_search(item_list, search_item))
