def BinarySearch(lst, search_term):
    minimum = 0
    maximium = len(lst) -1

    while minimum <= maximium:

        guess = ((minimum+maximium) // 2)

        if lst[guess] == search_term:
            return guess

        elif lst[guess] < search_term:
            minimum = guess + 1

        elif lst[guess] > search_term:
            maximium = guess - 1

    return 'Not Found'


test_search_term = 4
test_lst = [1,4,6,7,8,10,11,14]
test_result = BinarySearch(test_lst, test_search_term)

print(test_result)