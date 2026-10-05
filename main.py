def multiplicative_persistence(n: int) -> int:
    steps = 0
    while n >= 10:
        digits = [int(d) for d in str(n)]

        print(" * ".join(str(d)for d in digits), "=", end=" ")
        n = 1
        for d in digits:
            n *= d
        print(n)
        steps += 1

    return steps

def main ():
    print("Program starting.\n")
    print("Check multiplicative persistence.")

    try:
        num = int(input("Insert an integer: "))
        if num <= 0:
            print("Please insert a non-negative integer.")
            return
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return
    
    steps = multiplicative_persistence(num)

    print("No more steps.\n")
    print(f"This program took {steps} step(s)")
    print("\nProgram ending.")


if __name__ == "__main__":
    main()
