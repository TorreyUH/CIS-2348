def equation_num():
    x_num_1 = int(input())
    y_num_1 = int(input())
    n_num_1 = int(input())
    x_num_2 = int(input())
    y_num_2 = int(input())
    n_num_2 = int(input())

    solution = False

    for i in range(-10, 11):
        for x in range(-10, 11):
            if x_num_1 * i + y_num_1 * x == n_num_1 and x_num_2 * i + y_num_2 * x == n_num_2:
                print(i, x)
                solution = True

    if not solution:
        print("No solution")


if __name__ == '__main__':
    equation_num()
