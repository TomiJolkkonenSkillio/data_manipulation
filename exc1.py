import math

def main():
    try:
        user_input = input("Enter comma-separated number_list, e.g. 1.5, 3, 67, 2: ")
        
        # convert input string to number list
        number_list = [float(number) for number in user_input.split(',')]

        # calculations
        minimum = min(number_list)
        maximum = max(number_list)
        mean = sum(number_list) / len(number_list)

        # in order to find median, we need to sort the number list and find the middle number
        number_list.sort()

        n = len(number_list)
        if n % 2 == 0:
            median = (number_list[n // 2 - 1] + number_list[n // 2]) / 2
        else:
            median = number_list[n // 2]

        # in order to find mode (most used number), we need to do a new list with them
        how_often = {}

        for number in number_list:
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
        print("Invalid input. Please enter a list of comma-separated number_list, e.g. 1.5, 3, 67, 2")

if __name__ == "__main__":
    main()