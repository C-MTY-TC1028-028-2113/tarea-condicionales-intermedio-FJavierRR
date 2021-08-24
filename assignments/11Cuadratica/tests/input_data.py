# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["1", "2", "3"],
            ["Da el valor de a: ", "Da el valor de b: ", "Da el valor de c: ", "Raices complejas"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["0", "1", "2"],
            ["Da el valor de a: ", "Da el valor de b: ", "Da el valor de c: ", "-2.0"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["1", "5", "6"],
            ["Da el valor de a: ", "Da el valor de b: ", "Da el valor de c: ", "-2.0", "-3.0"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["0", "0", "2"],
            ["Da el valor de a: ", "Da el valor de b: ", "Da el valor de c: ", "No tiene solucion"],
            "Revisa tu código",
        ),
    ]
