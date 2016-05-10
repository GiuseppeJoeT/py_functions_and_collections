n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
        return x


print double_list(n)
