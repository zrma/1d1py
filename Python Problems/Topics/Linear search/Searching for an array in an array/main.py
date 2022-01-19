def solve_searching_for_an_array_in_an_array():
    lst1 = map(int, input().split(' '))
    lst2 = list(map(int, input().split(' ')))

    tot = 0
    for n in lst1:
        try:
            tot += (lst2.index(n) + 1)
        except ValueError:
            tot += len(lst2)

    print(tot)


if __name__ == '__main__':
    solve_searching_for_an_array_in_an_array()
