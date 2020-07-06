from .general_quadratic import Quadratic

while True:
    try:
        a = float(input(">>> Enter the coefficient of x² i.e 'a': "))
        break
    except:
        print('..input must be a float or an integer ...')

while True:
    try:
        b = float(input(">>> Enter the coefficient of x i.e 'b': "))
        break
    except:
        print('..input must be a float or an integer ...')

while True:
    try:
        c = float(input(">>> Enter the coefficient of x^0 i.e 'c': "))
        break
    except:
        print('..input must be a float or an integer ...')

quadratic = Quadratic(a, b, c)

print('\n==> Roots of the equation are {}'.format(quadratic.roots()))
print('\n==> Sum of roots of the equation is {}'.format(quadratic.sum_of_roots()))
print('\n==> Product of roots of the equation is {}'.format(quadratic.product_of_roots()))
print('\n==> Sum of squared roots of the equation is {}'.format(quadratic.sum_of_squared_roots()))
print('\n==> Inverse of roots of the equation is {}'.format(quadratic.inverse_of_roots()))
