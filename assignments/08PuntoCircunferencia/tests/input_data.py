# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["5", "0", "0", "0", "6" ],
            ["Introduce el radio: ", "Introduce x1: ", "Introduce y1: ", "Introduce x2: ", "Introduce y2: ", "FUERA"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["5", "0", "0", "0", "5" ],
            ["Introduce el radio: ", "Introduce x1: ", "Introduce y1: ", "Introduce x2: ", "Introduce y2: ", "SOBRE"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["5", "0", "0", "0", "3" ],
            ["Introduce el radio: ", "Introduce x1: ", "Introduce y1: ", "Introduce x2: ", "Introduce y2: ", "DENTRO"],
            "Revisa tu código",
        ),
    ]
