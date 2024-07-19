import pandas as pd

# Function to load CSV data into a Pandas DataFrame and select specific columns
def load_data(csv_file):
    """
    Load CSV data into a Pandas DataFrame and select specific columns.
    Args:
    - csv_file (str): File path of the CSV file.
    Returns:
    - Pandas DataFrame containing the CSV data with specified columns.
    """
    # Specify columns to include
    use_columns = ['Number', 'Carrier', 'Name', 'Gender', 'Address', 'Email']

    # Load CSV data into DataFrame
    df = pd.read_csv(csv_file, usecols=use_columns)
    return df

# Function to perform search based on user input criteria
def perform_search(df, criteria_dict):
    """
    Function to perform search on DataFrame based on user input criteria.
    Args:
    - df (Pandas DataFrame): DataFrame containing the data to search.
    - criteria_dict (dict): Dictionary where keys are criteria (e.g., 'Name', 'Gender') and values are search values.
    Returns:
    - Pandas DataFrame with filtered results
    """
    filtered_df = df.copy()

    for criterion, value in criteria_dict.items():
        if criterion in filtered_df.columns:
            # Handle exact match for Name criteria
            if criterion == 'Name':
                filtered_df = filtered_df[filtered_df[criterion].str.lower() == value.lower()]
            else:
                # Case-insensitive search using str.contains for partial matches
                filtered_df = filtered_df[filtered_df[criterion].str.contains(value, case=False, na=False)]
        else:
            print(f"Column '{criterion}' not found in the DataFrame.")

    return filtered_df

# Main function to handle user interaction
def main():
    # Load CSV data and select specific columns
    csv_file = '767k-MTNL.csv'  # Replace with your CSV file path
    df = load_data(csv_file)

    # Ask user for input criteria and values
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
            search_value = input(f"Enter {df.columns[int(choice) - 1]}: ").strip()
            criteria_dict[df.columns[int(choice) - 1]] = search_value

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

    # Perform search based on user input criteria
    result_df = perform_search(df, criteria_dict)

    # Display results
    if not result_df.empty:
        print("\nSearch Results:")
        print(result_df)
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()