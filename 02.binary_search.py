def binary_search(number_list, search_element):
    found = False
    high = len(number_list) - 1
    low = 0

    while low <= high and not(found):
        mid = (low + high) / 2
        if number_list[mid] == search_element:
            print 'Got it at index', mid
            found = True
        else:
            if number_list[mid] < search_element:
                low = mid + 1
            else:
                high = mid - 1
    return found

number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search_element = 9
print(binary_search(number_list, search_element))
