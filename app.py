# L1
import math  # L2
import random  # L3
# L4
def generate_numbers(count):  # L5
    numbers = []  # L6
    for _ in range(count):  # L7
        numbers.append(random.randint(1, 100))  # L8
    return numbers  # L9
# L10
def calculate_statistics(numbers):  # L11
    total = sum(numbers)  # L12
    average = total / len(numbers)  # L13
    minimum = min(numbers)  # L14
    maximum = max(numbers)  # L15
    return total, average, minimum, maximum  # L16
# L17
def normalize_numbers(numbers):  # L18
    max_value = max(numbers)  # L19
    normalized = []  # L20
    for n in numbers:  # L21
        normalized.append(n / max_value)  # L22
    return normalized  # L23
# L24
def print_report(numbers, stats):  # L25
    total, average, minimum, maximum = stats  # L26
    print("Report")  # L27
    print("------")  # L28
    print("Numbers:", numbers)  # L29
    print("Total:", total)  # L30
    print("Average:", round(average, 2))  # L31
    print("Min:", minimum)  # L32
    print("Max:", maximum)  # L33
# L34
def square_numbers(numbers):  # L35
    squared = []  # L36
    for n in numbers:  # L37
        squared.append(n ** 2)  # L38
    return squared  # L39
# L40
def filter_even(numbers):  # L41
    evens = []  # L42
    for n in numbers:  # L43
        if n % 2 == 0:  # L44
            evens.append(n)  # L45
    return evens  # L46
# L47
def main():  # L48
    count = 10  # L49
    numbers = generate_numbers(count)  # L50
    stats = calculate_statistics(numbers)  # L51
    normalized = normalize_numbers(numbers)  # L52
    squared = square_numbers(numbers)  # L53
    evens = filter_even(numbers)  # L54
    print_report(numbers, stats)  # L55
    print("Normalized:", normalized)  # L56
    print("Squared:", squared)  # L57
    print("Even numbers:", evens)  # L58
# L59
class NumberProcessor:  # L60
    def __init__(self, numbers):  # L61
        self.numbers = numbers  # L62
# L63
    def cube(self):  # L64
        result = []  # L65
        for n in self.numbers:  # L66
            result.append(n ** 3)  # L67
        return result  # L68
# L69
    def sqrt(self):  # L70
        result = []  # L71
        for n in self.numbers:  # L72
            result.append(math.sqrt(n))  # L73
        return result  # L74
# L75
if __name__ == "__main__":  # L76
    main()  # L77
    sample = generate_numbers(5)  # L78
    processor = NumberProcessor(sample)  # L79
    print("Cubes:", processor.cube())  # L80
    print("Square roots:", processor.sqrt())  # L81
# L82
def goodbye():  # L83
    message = "Program finished successfully."  # L84
    print(message)  # L85
# L86
goodbye()  # L87
# L88
# End of program  # L89
# Thank you for reading  # L90
# L91
# L92
# L93
# L94
# L95
# L96
# L97
# L98
# L99
# L100
