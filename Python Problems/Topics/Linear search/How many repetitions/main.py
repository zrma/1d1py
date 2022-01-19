def solve_how_many_repetitions():
    num = int(input())
    lst = list(map(int, input().split(' ')))

    print(lst.count(num))


if __name__ == '__main__':
    solve_how_many_repetitions()
