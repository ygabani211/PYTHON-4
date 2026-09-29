import math

def display_welcome():
    print("Welcome to the Data Analyzer and Transformer Program")

def factorial_recursive(n):
    """Calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def get_dataset_statistics(data_list):
    """Returns multiple values (min, max, sum, average) as a tuple."""
    if not data_list:
        return None, None, None, None
    
    total_elements = len(data_list)
    min_val = min(data_list)
    max_val = max(data_list)
    sum_val = sum(data_list)
    avg_val = sum_val / total_elements if total_elements > 0 else 0
    
    return min_val, max_val, sum_val, avg_val

def main():
    display_welcome()
    
    data = []
    
    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        
        choice = input("Please enter your choice: ")

        if choice == '1':
            print("\nStep 1: Input Data")
            input_str = input("Enter data for a 1D array (separated by spaces):\n")
            try:
                data = [int(x) for x in input_str.split()]
                print("\nData has been stored successfully!")
            except ValueError:
                print("\nInvalid input. Please enter valid numbers separated by spaces.")
                
                
        elif choice == '2':
            print("\nStep 2: Display Data Summary (Built-in Functions)")
            if not data:
                print("No data available. Please input data first (Option 1).")
            else:
                total_elements = len(data)
                min_val = min(data)
                max_val = max(data)
                sum_val = sum(data)
                avg_val = sum_val / total_elements if total_elements > 0 else 0
                
                print("\nData Summary:")
                print(f"- Total elements: {total_elements}")
                print(f"- Minimum value: {min_val}")
                print(f"- Maximum value: {max_val}")
                print(f"- Sum of all values: {sum_val}")
                print(f"- Average value: {avg_val:.2f}")
                
        elif choice == '3':
            print("\nStep 3: Calculate Factorial (Recursion)")
            try:
                num = int(input("Enter a number to calculate its factorial: "))
                if num < 0:
                    print("Factorial is not defined for negative numbers.")
                else:
                    result = factorial_recursive(num)
                    print(f"Factorial of {num} is: {result}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
                
        elif choice == '4':
            print("\nStep 4: Filter Data by Threshold (Lambda Function)")
            if not data:
                print("No data available. Please input data first (Option 1).")
            else:
                try:
                    threshold = int(input("Enter a threshold value to filter out data above this value:\n"))
                    filtered_data = list(filter(lambda x: x >= threshold, data))
                  
                    filtered_str = ", ".join(map(str, filtered_data))
                    print(f"\nFiltered Data (values >= {threshold}):")
                    print(filtered_str)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
                
        elif choice == '5':
            print("\nStep 5: Sort Data")
            if not data:
                print("No data available. Please input data first (Option 1).")
            else:
                print("\nChoose sorting option:")
                print("1. Ascending")
                print("2. Descending")
                sort_choice = input("\nEnter your choice: ")
                
                if sort_choice == '1':
                    sorted_data = sorted(data)
                    print("\nSorted Data in Ascending Order:")
                    print(", ".join(map(str, sorted_data)))
                elif sort_choice == '2':
                    sorted_data = sorted(data, reverse=True)
                    print("\nSorted Data in Descending Order:")
                    print(", ".join(map(str, sorted_data)))
                else:
                    print("Invalid sorting choice. Please enter 1 or 2.")
                    
        elif choice == '6':
            print("\nStep 6: Display Dataset Statistics (Return Multiple Values)")
            if not data:
                print("No data available. Please input data first (Option 1).")
            else:
                min_val, max_val, sum_val, avg_val = get_dataset_statistics(data)
                
                print("\nDataset Statistics:")
                print(f"- Minimum value: {min_val}")
                print(f"- Maximum value: {max_val}")
                print(f"- Sum of all values: {sum_val}")
                print(f"- Average value: {avg_val:.2f}")
                
        elif choice == '7':
            print("\nStep 7: Exit Program")
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()