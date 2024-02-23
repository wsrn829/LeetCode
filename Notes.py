
1. sort() and sorted() are both functions in Python used to sort elements, but they work differently.

    sort() is a method that belongs to the list class in Python. It sorts the list in-place, meaning it modifies the original list. It does not return a new list. For example:

    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    my_list.sort()
    print(my_list) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    sorted() is a built-in function in Python. It returns a new list containing all items from the original list but in a sorted order. It does not modify the original list. For example:

    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sorted(my_list)
    print(sorted_list) # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    print(my_list) # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

    In summary, sort() sorts the list in-place and does not return a new list, while sorted() returns a new sorted list without modifying the original list.






