data0 = "11-22,95-115"
data1 = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

def procesarInput(nombreFichero):
    with open(nombreFichero, 'r', encoding='UTF-8') as reader:
        return reader.read()
data99 = procesarInput("AoC2025ej02_input.txt")

def isNumInvalid(num):
    numStr = str(num)
    numDigitis = len(numStr)
    for i in range(1, (numDigitis // 2) + 1):
        if numDigitis % i == 0:
            numToCheck = numStr[:i]
            index = 2 * i
            isDuplicated = True
            while isDuplicated and index <= numDigitis:
                nextNum = numStr[index - i: index]
                if nextNum != numToCheck:
                    isDuplicated = False
                index += i
            if isDuplicated:
                return num
    return 0

def getPassword(input):
    rangos = input.split(",")
    numInvalidIDs = 0

    for rango in rangos:
        nums = rango.split("-")
        n1 = int(nums[0])
        n2 = int(nums[1])
        for num in range(n1, n2 + 1):
            numInvalidIDs += isNumInvalid(num)
    return numInvalidIDs

print(isNumInvalid(11))
print(isNumInvalid(12))
print(isNumInvalid(13))
print(isNumInvalid(1212))
print(isNumInvalid(121212))

print("Data0: ", getPassword(data0))
print("Data1: ", getPassword(data1))
print("Data99: ", getPassword(data99))
