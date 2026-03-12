def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    total_segundos = 3665
    segundos_por_hora = 3600
    segundos_por_minuto = 60
    horas = total_segundos // segundos_por_hora
    print(horas)
    minutos_enteros = (total_segundos % segundos_por_hora) // segundos_por_minuto
    print(minutos_enteros)
    segundos_restantes = total_segundos % segundos_por_minuto
    print(segundos_restantes)
