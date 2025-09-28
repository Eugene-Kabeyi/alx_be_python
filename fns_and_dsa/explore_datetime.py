from datetime import datetime, timedelta

# Part 1: Display current date and time
def display_current_datetime():
    # Save the current date and time in current_date variable
    current_date = datetime.now()
    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)
    return current_date

# Part 2: Calculate a future date
def calculate_future_date(current_date, days_to_add):
    # Save the future date inside a future_date variable
    future_date = current_date + timedelta(days=days_to_add)
    # Format as "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future)
    return future_date

# Main program flow
if __name__ == "__main__":
    # Display current datetime
    current_date = display_current_datetime()
    
    try:
        # Ask user for number of days
        days = int(input("Enter the number of days to add to the current date: "))
        # Calculate future date
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an integer value for days.")