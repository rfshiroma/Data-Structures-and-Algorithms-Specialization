# python3


def max_pairwise_product(n):
    a = sorted(n)
    max_product = max(a[0]*a[1], a[-1]*a[-2])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
