# Product-Expiration-calculator
Python script to show the expiration date of a given product.
# About the script
The code uses two Python libraries: ***'datetime'*** and ***'dateutil'***.

1. **datetime:**
   - This library provides classes for working with dates and times in Python. In the code, ***'datetime.strptime'*** is used to parse the manufacturing date entered by the user.
   - ***'datetime'*** is part of the Python standard library, and it's commonly used for date and time manipulation.
    
2. **dateutil.relativedelta:**
   - The ***'relativedelta'*** class from the ***'dateutil.relativedelta'*** module is used to perform arithmetic with ***'datetime'*** objects, specifically to add or subtract months from a given date.
   - It allows for more flexible date calculations than the basic ***'datetime'*** module.

 >[!NOTE]
   >The ***'dateutil'*** library is not part of the Python standard library by default, so you may need to install it separately using:
   >>**pip install python-dateutil**

# Output
![expire_m](https://github.com/seinenali01/Product-Expiration-calculator/assets/157710508/ed917c43-23b5-4214-bbbd-55899d61fc48)
