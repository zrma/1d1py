def found_value(array: list, value: int):
    """
    looking through the array
    if the current value is equal to the value we are
    searching for,
    then we return the index of this element;
    if the sought value is not in the array, we return -1
    :param array: list
    :param value: int
    :return: int
    """
    for (i, n) in enumerate(array):
        if n == value:
            return i
    return -1


def learn_topic_linear_search():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = int(input('Enter the value you are looking for: '))
    print(found_value(array, value))


if __name__ == '__main__':
    learn_topic_linear_search()
