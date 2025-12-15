data1 = '''987654321111111
811111111111119
234234234234278
818181911112111'''

def procesarFichero(nombreFichero):
    with open(nombreFichero, 'r', encoding="UTF-8") as reader:
        return reader.read()
# data99 = procesarFichero("Aoc2025ej03_input.txt")

# 818181911112111
def getBankJoltage(bank):
    num_mayor = 0
    for i in range(len(bank) - 1):
        decenas = 10 * int(bank[i])
        for j in range(i+1,len(bank)):
            num_actual = decenas + int(bank[j])
            if num_actual > num_mayor:
                num_mayor = num_actual
    return num_mayor

def getTotalJoltage(input):
    totalJoltage = 0
    banks = input.split()
    for bank in banks:
        totalJoltage += getBankJoltage(bank)
    return totalJoltage

print(getTotalJoltage(data1))