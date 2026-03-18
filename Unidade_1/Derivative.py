import numpy as np


def derivative(x, delta_x):
    philosophy = int(input("Choose the 'philosophy' value (1 - Forward | 2 - Backward | 3 - Central): "))
    match philosophy:
        case 1:
            return forward_derivative(x, delta_x)
        case 2:
            return backward_derivative(x, delta_x)
        case 3:
            return central_derivative(x, delta_x)
        case _:
            return "Unknown philosophy!"

def forward_derivative(x, delta_x):
    derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
    match derivative_order:
        case 1:
            return (func(x + delta_x) - func(x)) / delta_x
        case 2:
            return (func(x + (2 * delta_x)) - (2 * func(x + delta_x)) + func(x)) / (delta_x ** 2)
        case 3:
            return (func(x + (3 * delta_x)) - (3 * func(x + (2 * delta_x))) + (3 * func(x + delta_x)) - func(x)) / (delta_x ** 3)      
        case 4:
            return (func(x + (4 * delta_x)) - (4 * func(x + (3 * delta_x))) + (6 * func(x + (2 * delta_x))) - (4 * func(x + delta_x)) + func(x)) / (delta_x ** 4)
            return
        case _:
            return "Invalid derivative order!"

def backward_derivative(x, delta_x):
    derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
    match derivative_order:
        case 1:
            return (func(x) - func(x + delta_x)) / delta_x
        case 2:
            return (func(x) - (2 * func(x - delta_x)) + func(x - (2 * delta_x))) / (delta_x ** 2)
        case 3:
            return (func(x) - (3 * func(x - delta_x)) + (3 * func(x - (2 * delta_x))) - func(x - (3 * delta_x))) / (delta_x ** 3)
        case 4:
            return (func(x) - (4 * func(x - delta_x)) + (6 * func(x - (2 * delta_x))) - (4 * func(x - (3 * delta_x))) + func(x - (4 * delta_x))) / (delta_x ** 4)
        case _:
            return "Invalid derivative order!"

def central_derivative(x, delta_x):
    derivative_order = int(input("Choose the 'derivative_order' value (1 - First | 2 - Second | 3 - Third | 4 - Fourth): "))
    match derivative_order:
        case 1:
            return (func(x + delta_x) - func(x - delta_x)) / (delta_x)
        case 2:
            return (func(x + delta_x) - (2 * func(x)) + func(x - delta_x)) / (delta_x ** 2)
        case 3:
            return (func(x + (2 * delta_x)) - (2 * func(x + delta_x)) + (2 * func(x - delta_x)) - func(x - (2 * delta_x))) / (delta_x ** 3)
        case 4:
            # TODO: montar e aplicar aqui
            return
        case _:
            return "Invalid derivative order!"

def func(x):
    return x ** 5 * np.cos(x)

if __name__ == "__main__":
    x = float(input("Choose the 'x' value: "))
    delta_x = float(input("Choose the 'delta_x' value: "))

    derivResult = derivative(x, delta_x)

    print(f"The result of the derivative is: {derivResult}" )