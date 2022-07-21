import math


def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = low + high
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def count_the_step(count_of_list):
    return math.log(count_of_list, 2)


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))

    # TODO: Exercise 1.1:
    #  Suppose you have a sorted list of 128 names, and you’re searching
    #  through it using binary search. What’s the maximum number of steps it would take?

    print(count_the_step(128))

    # TODO: Exercise 1.2:
    #  Suppose you double the size of the list. What’s the maximum number of steps now?

    print(count_the_step(128*2))

    # Big O notation

    # TODO: Exercise 1.3: You have a name, and you want to find the person’s phone number
    #  in the phone book.

    # O(log n)

    # TODO: Exercise 1.4: You have a phone number, and you want to find the person’s name
    #  in the phone book. (Hint: You’ll have to search through the whole book!)

    # O(n)

    # TODO: Exercise 1.5: You want to read the numbers of every person in the phone book.

    # O(n)

    # TODO: Exercise 1.6: You want to read the numbers of just the As.

    # O(n)
    # Because: O(n + 26), O(n - 26), O(n * 26), O(n / 26) same as O(n) (26 letters)