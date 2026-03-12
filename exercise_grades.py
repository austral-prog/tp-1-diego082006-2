def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio_tres_notas = (nota1 + nota2 + nota3)/3
    print(promedio_tres_notas)
    maximo_tres_notas = max(nota1, nota2, nota3)
    print(maximo_tres_notas)
    minimo_tres_notas = min(nota1, nota2, nota3)
    print(minimo_tres_notas)
    cuantos_puntos_faltan = 10 - promedio_tres_notas
    print(cuantos_puntos_faltan)
