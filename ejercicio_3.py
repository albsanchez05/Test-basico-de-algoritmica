
def main():
    extra = 1.5
    try:
        horas_trabajadas = int(float(input("LEER HORASTRABAJADAS: ")))
        tarifa = float(input("LEER TARIFA: "))
        if horas_trabajadas <= 0 or tarifa <= 0:
            raise ValueError()
    except ValueError:
        print('Error: HORASTRABAJADAS y TARIFA deben ser numeros mayores a 0')
        exit()
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        salario = (40 * tarifa) + (horas_extras * tarifa * extra)
    else:
        salario = horas_trabajadas * tarifa

    print(f"El salario del trabajador es: {salario:.2f}")

if __name__ == "__main__":
    main()
