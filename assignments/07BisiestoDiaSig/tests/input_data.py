# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test Case 1
    (
        ["2015", "2", "13"],
        ["Año: ", "Mes: ", "Día: ", '2015', '2', '14'],
        ["Revisa qué pasa en un día siguiente sin problemas de fin de mes"]
    ),
    # Test Case 2
    (
        ["2015", "2", "28"],
        ["Año: ", "Mes: ", "Día: ", '2015', '3', '1'],
        ["Revisa qué debe pasar en el mes 2 que no es bisiesto después del día 28"]
    ),
    # Test Case 3
    (
        ["2020", "2", "28"],
        ["Año: ", "Mes: ", "Día: ", '2020', '2', '29'],
        ["Revisa qué debe pasar en el mes 2 que es bisiesto después del día 28"]
    ),
    # Test Case 4
    (
        ["2021", "12", "31"],
        ["Año: ", "Mes: ", "Día: ", '2022', '1', '1'],
        ["Revisa qué debe pasar si el día que te dan es el último del año"]
    ),
    # Test Case 5
    (
        ["2019", "4", "30"],
        ["Año: ", "Mes: ", "Día: ", '2019', '5', '1'],
        ["Revisa qué debe pasar si te dan el último día de un mes de 30 días"]
    )
]
