from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
def calculate_expiration_date(manufacturing_date, shelf_life_months):
    manufacturing_date = datetime.strptime(manufacturing_date,"%Y-%m")
    expiration_date = manufacturing_date + relativedelta(months=shelf_life_months)
    return expiration_date
manufacturing_date_input = input("Enter the manufacturing date(YYYY-MM):")
shelf_life_input = input("Enter the shelf life in months:")
try:
    shelf_life_months = int(shelf_life_input)
    expiration_date = calculate_expiration_date(manufacturing_date_input,shelf_life_months)
    print(f"The expiration date is: {expiration_date.strftime('%Y-%m-%d')}")
except ValueError:
    print("Invalid input.Please enter a valid shelf life as a number of months.")
except Exception as e:
    print(f"An error occurred: {e}")        