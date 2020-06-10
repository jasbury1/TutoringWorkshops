def factorial(num):
    # Base Cases
    if num == 0:
        return 1
    if num < 0:
        return 1

    # Reduction
    reduced_factorial = factorial(num - 1)

    # combining reduced result and num
    combined_value = reduced_factorial * num

    # Return combined results
    return combined_value

if __name__ == "__main__":
    print(factorial(0))
    print(factorial(7))
    print(factorial(52))
