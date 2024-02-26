
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

2. In Python, you can check if a key exists in a dictionary using key in dict. However, you cannot check if a value exists in a dictionary using value in dict. This is because dictionaries are optimized for key-based lookups, and checking for the presence of a value in a dictionary would require iterating over all the values in the dictionary, which is not efficient.

If you want to check if a value exists in a dictionary, you can use the values() method to get a list of all the values in the dictionary and then use the in operator to check if the value is in that list.

3. In Python, key in dict and key in dict.keys() are essentially the same operation. Both of them check if a key exists in the dictionary. However, there is a subtle difference in performance and readability.

key in dict: This checks if the key exists in the dictionary. It is a more readable and efficient way of checking for the presence of a key in a dictionary. This is because Python's dictionaries are implemented using a hash table, so checking for the presence of a key in a dictionary is an O(1) operation.

key in dict.keys(): This creates a list of all the keys in the dictionary and then checks if the key exists in that list. This is less efficient because creating the list of keys takes O(n) time, where n is the number of keys in the dictionary. Additionally, it is less readable because it is not immediately clear that you are checking for the presence of a key in a dictionary.

4. The choice of -1 as the return value for indicating that the target is not found in the array is a convention that has been widely adopted in programming, especially in languages like C, C++, and Python, where array indices start from 0. 

5. The % operator is used for the modulo operation, which calculates the remainder of the division of two numbers, while the // operator is used for floor division, which calculates the quotient of the division of two numbers, rounded down to the nearest whole number.

6. Matrix is a special case of two dimensional array where each data element is of strictly same size. So every matrix is also a two dimensional array but not vice versa.