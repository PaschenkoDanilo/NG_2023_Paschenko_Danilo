from math import sqrt

print ("Input coefficients of quadratic equation.")
quadraticCoefficient = int(input("Input quadratic coefficient: "))
linearCoefficient = int(input("Input linear coefficient: "))
constantTerm = int(input("Input constant term: "))

discriminant = linearCoefficient**2 - 4*quadraticCoefficient*constantTerm

if discriminant < 0:
    print ("Negative discriminant. Quadratic equation hasn't a real roots.")
elif discriminant == 0:
    root = (-linearCoefficient / 2*quadraticCoefficient)
    print ("Real root = " + str(root))
else:
    firstRoot = (-linearCoefficient + sqrt(discriminant)) / (2*quadraticCoefficient)
    secondRoot = (-linearCoefficient - sqrt(discriminant)) / (2*quadraticCoefficient)
    print ("First real root = " + str(firstRoot) + "\n" + "Second real root = " + str(secondRoot))