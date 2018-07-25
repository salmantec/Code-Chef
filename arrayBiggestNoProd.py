array1 = [1,5,2,3,76,34,22,54,34]

firstMax = max(array1)
print(firstMax)

array1.remove(firstMax)

secondMax = max(array1)
print(secondMax)

prod = firstMax * secondMax
print("product of two biggest integers in an array " + str(prod))
