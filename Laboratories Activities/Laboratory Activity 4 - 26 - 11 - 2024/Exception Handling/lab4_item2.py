try:
    size = float(input("Enter the size of the array: "))
    if size <= 0:
        raise ValueError("Size must be a positive integer.")
except ValueError as ve:
    print("Invalid size. Please enter a positive integer.")
else:
    arr = [0.0] * size
    print("Enter the elements of the array:")
    for i in range(size):
        try:
            arr[i] = float(input())
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            break
    try:
        x = int(input("Enter the index of the element to print: "))
        print(f"Element at index {x}: {arr[x]:.2f}")
    except IndexError:
        print(f"Index {x} is invalid.")
    except ValueError:
        print("Invalid index. Please enter a valid integer.")