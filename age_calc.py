from datetime import datetime

# Function to calculate age
def calculate_age(birth_date):
    today = datetime.today()
    # Calculate the difference
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
        
    if days < 0:
        months -= 1
        days += 30  
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
try:
    birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
    years, months, days = calculate_age(birth_date)
    print(f"You are {years} years, {months} months, and {days} days old.")
except ValueError:
    print("Invalid date format! Please enter the date in YYYY-MM-DD format.")
