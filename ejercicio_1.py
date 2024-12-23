def main():
    numero = ''
    while not isinstance(numero, int):
        try:
            numero = int(input("LEER número: "))
        except ValueError:
            print(f" El valor agregado no es un número valido. Intenta de nuevo.")

    if numero % 2 == 0:
        print(f"El número {numero} es par.")
        if numero < 0:
            print(f"El número {numero} es negativo, no hay números que desciendan hasta cero")
            exit()
        print("Números pares descendientes desde el número hasta cero:")
        for i in range(numero, -1, -2):
            print(i)
    else:
        print(f"El número {numero} es impar.")
        if numero < 0:
            print(f"El número {numero} es negativo, no hay números que desciendan hasta cero")
            exit()
        print("Números impares descendientes desde el número hasta uno:")
        for i in range(numero, 0, -2):
            print(i)

if __name__ == "__main__":
    main()
