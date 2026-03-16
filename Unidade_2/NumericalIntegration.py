import numpy as np

def numIntegration(a, b, n):
    if n <= 0:
        print("The number of subdivisions 'n' must be a positive integer.")
        return
    if a >= b:
        print("The value of 'a' must be less than 'b'.")
        return
    if a == b:
        return 0

    h = (b - a) / n
    As = 0
    for k in range(1, n + 1):
        xi = a + (k - 1) * h
        xf = xi + h
        As += IntegrNC(xi, xf)
    return As

def IntegrNC(xi, xf, ps=1):
    match ps:
        case 1:
            h = xf - xi
            return (h * (func(xi) + func(xf)) / 2)
        case _:
            print("Invalid method selected. Please choose a valid method.")
            return

def func(x):
    return x ** 5 * np.cos(x)

if __name__ == "__main__":
    a = float(input("Choose the 'a' value: "))
    b = float(input("Choose the 'b' value: "))
    n = int(input("Choose the 'n' value: "))

    integrResult = numIntegration(a, b, n)

    print(f"The result of the numerical integration is: {integrResult}" )