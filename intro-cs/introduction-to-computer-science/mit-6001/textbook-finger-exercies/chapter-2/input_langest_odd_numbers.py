def get_largest_odd_number(numbers):
    largest_odd = None
    for num in numbers:
        if num % 2 != 0:
            if largest_odd is None or num > largest_odd:
                largest_odd = num
    return largest_odd

def main():
    print("Please enter 10 integers:")
    integers = []
    for i in range(10):
        try:
            num = int(input(f"Integer {i+1}: "))
            integers.append(num)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            return

    largest_odd = get_largest_odd_number(integers)

    if largest_odd is not None:
        print(f"The largest odd number entered is: {largest_odd}")
    else:
        print("No odd number was entered.")

if __name__ == "__main__":
    main()
