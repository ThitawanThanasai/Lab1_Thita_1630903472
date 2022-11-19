def sum_harmonic(n, i=1):
    # recursion version
    if n == 1:
        return 1
    else:

        return 1 / n + sum_harmonic(n - 1, i + 1)


def main():
    n = int(input("Harmonic step = "))
    print(sum_harmonic(n))


if __name__ == "__main__":
    main()