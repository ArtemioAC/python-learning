# Code examples

def printHeader(header):
    print("\n========================================")
    print(header.center(40, '='))
    print("========================================\n")

def integerExamples():
    print("Some integer numbers in Python:\nSyntax :\t[200, 400, 500000, 0b10, 0x0F, 0o7]")
    numberList = [200, 400, 500000, 0b10, 0x0F, 0o7]
    print("Python value :\t%s" % numberList)
    print("Note that Python numbers in base 2, 8 and 16 are also integers.\n")

def floatExamples():
    print("Some floating-point numbers in Python:\nSyntax :\t[2.5, 100.0, 4., .2, .4e7, 4.2E-4]")
    numberList = [2.5, 100.0, 4., .2, .4e7, 4.2E-4]
    print("Python value :\t%s" % numberList)
    print("The scientific notation is also implemented in Python, take advantage of that when working with floating-point numbers")
    print("Biggest floating-point number :\n1.79e308")
    print("A bigger number would be considered as inf : 1.8e308 is %f" % 1.8e308)
    print("Smallest floating-point number :\n5e-324")
    print("A smaller number would be considered as inf : 4e-324 is %f\n" % 4e-324)

def main():
    printHeader("Data Types")

    integerExamples()
    floatExamples()



if __name__ == "__main__":
    main()