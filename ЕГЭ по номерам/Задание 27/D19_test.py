from numba import njit


@njit
def optimize_code():
    try:
        filename = 'files_compege/27B_2764.txt'
        f = open(filename)
        lines = f.readlines()
        f.close()

        n = int(lines[0])
        a = [int(x) for x in lines[1:]]
        a = np.array(a, dtype=np.int64)
        k = 7
        mn = np.int64(10 ** 20)

        for i in range(k, n):
            f = a[:i - 7]
            indices = np.where((a[i] + f) % 23 == 0)[0]
            filtered_f = f[indices]
            filtered_indices = np.where((a[i] * filtered_f) % 6 == 0)[0]

            if filtered_indices.size > 0:
                temp = np.min(a[i] + filtered_f[filtered_indices])
                mn = min(mn, temp)

        print(mn)
    except:
        print("An error occurred")


optimize_code()
