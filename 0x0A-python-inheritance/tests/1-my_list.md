# Doctest document for the 1-my_list module

## Import the MyList Class from the module

    >>> MyList = __import__('1-my_list').MyList

### Inputs

    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)

### Print list

    >>> print(my_list)
    [1, 4, 2, 3, 5]

### Print sorted list using extended method

    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]