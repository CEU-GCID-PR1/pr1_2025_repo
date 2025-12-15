data1 = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def procesarInput(nombreFichero):
    with open(nombreFichero, 'r', encoding='UTF-8') as reader:
        return reader.read()

data99 = procesarInput("AoC2025ej03_input.txt")

def getLargestNum(bank, leftIndex, rightIndex):
    index = leftIndex
    for i in range(leftIndex + 1, rightIndex):
        if bank[i] > bank[index]:
            index = i
    return index

def getBankJoltage(bank):
    numero = ""
    leftIndex = 0
    for i in range(len(bank) - 11, len(bank) + 1):
        index = getLargestNum(bank, leftIndex, i)
        numero += bank[index]
        leftIndex = index + 1
    return int(numero)

def getTotalJoltage(input):
    totalJoltage = 0
    banks = input.split()
    for bank in banks:
        totalJoltage += getBankJoltage(bank)
    return totalJoltage

# print(getBankJoltage("818181911112111"))
print(getTotalJoltage(data99))
