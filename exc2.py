import argparse
import math

def main():
    try:
        # argument parser
        parser = argparse.ArgumentParser(description="calculations with command line parameters.")
        parser.add_argument('numbers', type=float, nargs='+', help="Use numbers after the command, e.g. python exc2.py 5 6.")
        args = parser.parse_args()
        numbers = args.numbers

        # calculations
        minimum = min(numbers)
        maximum = max(numbers)
        mean = sum(numbers) / len(numbers)

        # median needs sorted list where we can find the middle number
        numbers.sort()
        n = len(numbers)
        if n % 2 == 0:
            median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
        else:
            median = numbers[n // 2]

        # in order to find mode (most used number), we need to do a new list with them
        how_often = {}

        for number in numbers:
            how_often[number] = how_often.get(number, 0) + 1
        found_most = max(how_often.values())
        mode = [key for key, val in how_often.items() if val == found_most]

        if len(mode) == 1: # if there is no most used number
            mode = mode[0]
        else:
            mode = "No unique mode"

        print(f"Smalles number is: {minimum}")
        print(f"Biggest number is: {maximum}")
        print(f"Average of all numbers is: {mean}")
        print(f"Median number is: {median}")
        print(f"Most used number is (if available): {mode}")

    except ValueError:
        print("Invalid input. Use numbers after the command, e.g. python exc2.py 5 6.")

if __name__ == "__main__":
    main()
