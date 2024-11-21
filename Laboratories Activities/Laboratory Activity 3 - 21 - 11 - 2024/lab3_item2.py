def perfect_number(number):
    if number <= 0:
        return False

    divisors_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisors_sum += i

    return divisors_sum == number

if __name__ == "__main__":
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        
        if perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
    except ValueError:
        print("Please enter a valid integer.")
