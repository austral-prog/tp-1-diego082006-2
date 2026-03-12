def length():
    """
    Ejercicio 7 - Conversión de Unidades de Longitud

    Dada una distancia en metros, convertir e imprimir:
    1. Kilómetros (1 km = 1000 m)
    2. Millas (1 milla ≈ 1609.34 m)
    3. Pies (1 pie ≈ 0.3048 m)
    4. Pulgadas (1 pulgada ≈ 0.0254 m)
    """
    metros = 1000
    un_kilometro = 1000
    una_milla = 1609.34
    un_pie = 0.3048
    una_pulgada = 0.0254
    distancia_kilometros = metros / un_kilometro
    distancia_millas = metros / una_milla
    distancia_pies = metros / un_pie
    distancia_pulgadas = metros / una_pulgada
    print(distancia_kilometros)
    print(distancia_millas)
    print(distancia_pies)
    print(distancia_pulgadas)
