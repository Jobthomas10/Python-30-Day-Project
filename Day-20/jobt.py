def greet(name):
    def message():
        return "Welcome!"
    return f"Hello, {name}. {message()}"
print(greet("Alice"))  


def process_numbers(numbers):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    results = {"squares": [], "cubes": []}
    for num in numbers:
        results["squares"].append(square(num))
        results["cubes"].append(cube(num))

    return results

numbers = [1, 2, 3, 4]
processed = process_numbers(numbers)
print("Squares:", processed["squares"])  # Output: Squares: [1, 4, 9, 16]
print("Cubes:", processed["cubes"])      