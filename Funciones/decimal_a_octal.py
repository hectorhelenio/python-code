def decimal_a_octal(decimal):
    octal = 0
    i = 1
    while (decimal != 0):
        octal = octal + (decimal % 8) * i
        decimal = int(decimal / 8)
        i = i * 10;
    return octal;

decimal = int(input("Ingrese un número decimal: "))
print("Equivalente número octal : ",decimal_a_octal(decimal))