import math

print("")
print("      Welcome to Quadratic")
print("         Formula Solver!")
print("    Created by Spencer Boggs")
print("")
print("  Make sure to use the correct")
print("  variables.")
print("  Equation: ax^2 + bx + c")
print("")
print("")
input("    Press [Enter] to Start")
while True:
    negativeInSqrt = False
    print('')
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    print('')
    if (a) and (b) and (c):
        a = float(a)
        b = float(b)
        c = float(c)

        print("Equation: (-" + str(b) + " +- sqrt(" + str(b) + "^2 - 4(" + str(a) + ")(" + str(c) + ")))/2(" + str(a) + ")")

        try: math.sqrt((b**2) - 4 * a * c)
        except ValueError: negativeInSqrt = True

        if (negativeInSqrt != True):
            solvedSqrt = math.sqrt((b**2) - 4 * a * c)
        else:
            negativeValue = (abs((b**2) - 4 * a * c))
            solvedSqrt = "i*sqrt(" + str(negativeValue) + ")"
        

        if (negativeInSqrt != True):
            posAnswer = -b + solvedSqrt
            print(posAnswer)
            negAnswer = -b - solvedSqrt
            print(negAnswer)
        else:
            positiveNumerator = "-" + str(b) + " + " + str(solvedSqrt)
            print("(" + str(positiveNumerator) + ")/" + str(2 * a))
            negativeNumerator = "-" + str(b) + " - " + str(solvedSqrt)
            print("(" + str(negativeNumerator) + ")/" + str(2 * a))

    else:
        print("Please enter valid")
        print("variables")
