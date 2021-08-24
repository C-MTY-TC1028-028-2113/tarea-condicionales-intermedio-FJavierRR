# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case the test fails
# To test another case, add another tuple

input_values = [
        # Test case 1
        (
            ["100"],
            ["Introduce los cm: ", "1 m"],
            "Revisa tu código",
        ),
        # Test case 2
        (
            ["240005"],
            ["Introduce los cm: ", "2 km", "400 m", "5 cm"],
            "Revisa tu código",
        ),
        # Test case 3
        (
            ["67"],
            ["Introduce los cm: ", "67 cm"],
            "Revisa tu código",
        ),
        # Test case 4
        (
            ["300004"],
            ["Introduce los cm: ", "3 km", "4 cm"],
            "Revisa tu código",
        ),
        # Test case 5
        (
            ["1200500"],
            ["Introduce los cm: ", "12 km", "5 m"],
            "Revisa tu código",
        ),
    ]
