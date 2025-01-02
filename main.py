from calculator import calculate_cost
from inputs import gather_inputs

def main():
    print("Welcome to the 3D Printing Cost Calculator!")
    inputs = gather_inputs()

    total_cost = calculate_cost(*inputs)
    print(f"\nThe total cost of the 3D print job is: ${total_cost:.2f}")

if __name__ == "__main__":
    main()
