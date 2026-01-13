import math


def prodotto_parziale(n, k):
    """
    Calcola P_n(k) = (1*2*...*n) / (k*(k+1)*...*(n+k-1))
    """
    num = math.factorial(n)
    den = math.prod(range(k, n + k))
    return num / den


def verifica(k, max_n=20):
    print(f"Verifica empirica per k={k}")
    for n in [1, 2, 3, 5, 10, 15, max_n]:
        val = prodotto_parziale(n, k)
        print(f"n={n:2d} -> P_n(k) = {val:.6e}")
    print(f"Valore formale (cancellazione infinita): (k-1)! = {math.factorial(k-1)}")
    print("-" * 50)


def gammaprod(x, n=150):
    den = math.prod([(x + k) for k in range(n+1)])
    return math.factorial(n) * n**x / den


def verifica_gamma(max=10):
    for k in range(1, 100):
        x = k / 10
        print(f"{x} => \t {gammaprod(x)} \t {math.gamma(x)}")


# Esempi
verifica_gamma()
