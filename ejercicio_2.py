def main():
    i = 1
    personas = []
    print("LEER PERSONAS:")
    while i < 51:

        print(f"Persona {i}:")
        try:
            sexo = input("Ingrese el sexo (M/F): ").strip().upper()
            if sexo != 'M' and sexo != 'F':
                raise ValueError()
            edad = int(input("Ingrese la edad: "))
            if edad < 0:
                raise ValueError()
        except ValueError:
            print('Error: el sexo debe ser indicado con M o F, y la edad debe ser mayor o igual a 0')
            continue
       	personas.append({"sexo": sexo, "edad": edad})
        i = i + 1

    mayores_edad = 0
    menores_edad = 0
    masculinos_mayores = 0
    femeninas_menores = 0
    mujeres = 0

    # Procesar los datos
    for persona in personas:
        if persona["edad"] >= 18:
            mayores_edad += 1
            if persona["sexo"] == "M":
                masculinos_mayores += 1
        else:
            menores_edad += 1
            if persona["sexo"] == "F":
                femeninas_menores += 1

        if persona["sexo"] == "F":
            mujeres += 1

    # Calcular porcentajes
    porcentaje_mayores = (mayores_edad / 50) * 100
    porcentaje_mujeres = (mujeres / 50) * 100

    # Mostrar resultados
    print("\nResultados:")
    print(f"a. Cantidad de personas mayores de edad: {mayores_edad}")
    print(f"b. Cantidad de personas menores de edad: {menores_edad}")
    print(f"c. Cantidad de hombres mayores de edad: {masculinos_mayores}")
    print(f"d. Cantidad de mujeres menores de edad: {femeninas_menores}")
    print(f"e. Porcentaje de personas mayores de edad: {porcentaje_mayores:.2f}%")
    print(f"f. Porcentaje de mujeres respecto al total: {porcentaje_mujeres:.2f}%")

# Ejecutar el programa
if __name__ == "__main__":
    main()
