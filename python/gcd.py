
def find_multiples(a):
    arr = []
    i = a
    while i > 0:
        if a % i == 0:
            arr.append(i)
        i-=1
    return arr



def gcd(a, b):
    arr_a = find_multiples(a)
    arr_b = find_multiples(b)
    res = set(arr_a) & set (arr_b)
    return sorted(res)[::-1][0]

if __name__ == '__main__':
    assert gcd(12, 4) == 4
    assert gcd(11, 22) == 11
    assert gcd(64, 32) == 32
    assert gcd(1, 1) == 1
