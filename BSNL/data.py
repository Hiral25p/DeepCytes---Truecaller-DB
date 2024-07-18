import pandas as pd

# Function to load CSV data into a Pandas DataFrame and select specific columns
def load_data(csv_file):
    # Specify columns to include
    use_columns = ['Number', 'Carrier', 'Name', 'Gender', 'Address', 'Email']
    df = pd.read_csv(csv_file, usecols=use_columns)
    return df

# Function to perform search based on user input criteria
def perform_search(df, criteria_dict):
    filtered_df = df.copy()

    for criterion, value in criteria_dict.items():
        if criterion in filtered_df.columns:
            # Handle exact match for Name criteria
            if criterion == 'Name':
                filtered_df = filtered_df[filtered_df[criterion].str.lower().str.strip() == value.lower().strip()]
            else:
                # Case-insensitive search using str.contains for partial matches
                filtered_df = filtered_df[filtered_df[criterion].str.contains(value, case=False, na=False)]
            # Print intermediate results for debugging
            print(f"\nAfter filtering by {criterion} = '{value}':")
            if not filtered_df.empty:
                print(filtered_df.head(10))  # Show only the first 10 rows for readability
            else:
                print("No matching records found.")
        else:
            print(f"Column '{criterion}' not found in the DataFrame.")

    return filtered_df

# Main function to handle user interaction
def main():
    # Load CSV data and select specific columns
    csv_file = '19M-BSNL_Mobile_sample.csv'
    df = load_data(csv_file)

    print("\nInitial DataFrame (first 5 rows):")
    print(df.head())

    criteria_dict = {}
    while True:
        print("\nSearch Options:")
        print("1. Number")
        print("2. Carrier")
        print("3. Name")
        print("4. Gender")
        print("5. Address (Enter State)")
        print("6. Email")
        print("7. Done")

        choice = input("Enter your choice (1-7): ").strip().lower()

        if choice == '7' or choice.lower() == 'done':
            print("Exiting search.")
            break

        if choice in ['1', '2', '4', '6']:  # Number, Carrier, Gender, Email
            column_name = df.columns[int(choice) - 1]
            search_value = input(f"Enter {column_name}: ").strip()
            criteria_dict[column_name] = search_value

        elif choice == '3':  # Name
            search_value = input("Enter Name: ").strip().lower()
            criteria_dict['Name'] = search_value

        elif choice == '5':  # Address (Enter State)
            state_value = input("Enter State: ").strip().lower()
            address_value = input(f"Enter Address (searching within {state_value}): ").strip().lower()
            criteria_dict['Address'] = address_value
            criteria_dict['State'] = state_value

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

        # Perform search based on current criteria
        print("\nCurrent search criteria:")
        print(criteria_dict)
        result_df = perform_search(df, criteria_dict)

        # Display intermediate results
        if not result_df.empty:
            print("\nIntermediate Search Results (first 5 rows):")
            print(result_df.head())
        else:
            print("No matching records found for the current criteria.")

    # Perform final search based on all user input criteria
    result_df = perform_search(df, criteria_dict)

    # Display results
    if not result_df.empty:
        print("\nFinal Search Results (first 10 rows):")
        print(result_df.head(10))
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
