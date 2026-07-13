# Exercise 1 

def order_price(quantity: int) -> int:
    """
    A refactor of exercise 1 from 2.4

    Paramenters:
    quantity: kilos of bananas (int)

    Returns:
    total: Cost of order in pence 
    """
    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer.")

    price  = quantity * 3

    if price > 50:
        total = int((price + 4.99 - 1.50)*100)
    else:
        total = int((price + 4.99)*100)

    return total

# Exercise 2

def maximum_heart_rate(age: int) -> int:
    """
    A refactor of exercise 2 from 2.4
    Returns the maximum heart rate for a person

    Paramenters:
    Age: A person age (int)

    Returns:
    Maximum hear rate (int)
    """
    return int(208 - (0.7 * age))
    


def training_zone(age: int, rate: int) -> str:
    """
    Returns the training zome for a person based on their age
    and current heart rate.

    Paramenters:
    age: A person Age (int)
    rate: a persons current heart rate (int)

    Returns:
    zone: the training for a person (str)
    """

    m = maximum_heart_rate(age)

    if rate >= 0.9 * m:
        zone = "Interval training"
    elif 0.7 * m <= rate < 0.9 * m:
        zone = "Threshold training"
    elif 0.5 * m <= rate < 0.7 * m:
        zone = "Aerobic training"
    else:
        zone = "Couch potato"
    
    return zone

# Exercise 3

def is_valid_password(
        password: str,
        min_length: int = 8,
        has_upper: bool = True,
        has_lower: bool = True,
        has_numeric: bool = True
    ) -> bool:
    """
    Returns True if the password meets the required criteria.

    Parameters:
    password: The password to check (str)
    min_length: Minimum required password length (int)
    has_upper: Require at least one uppercase letter (bool)
    has_lower: Require at least one lowercase letter (bool)
    has_numeric: Require at least one numeric character (bool)

    Returns:
    True if the password is valid, otherwise False.
    """

    if not isinstance(password, str):
        return TypeError("password must be a string")
    
    if len(password) < min_length:
        return False
    
    if not password.isalnum():
        return False
    
    if has_upper and not any(char.isupper() for char in password):
        return False
    
    if has_lower and not any(char.islower() for char in password):
        return False
    
    if has_numeric and not any(char.isdigit() for char in password):
        return False
    
    return True
    
# Exercise 4

def sum_digits(number: int) -> int:

    if not isinstance(number, int):
        return TypeError("number must be an int")
    
    total = 0
    for digit in str(number):
        total = total + int(digit)

    return int(total)

# Exercise 5

def pairwise_digits(number_a: str, number_b: str) -> str:
    """
    Compares the digits of two numbers represented as strings.

    Parameters:
    number_a: First number as a string
    number_b: Second number as a string

    Returns:
    A binary string where:
    - '1' indicates the digits at the same index are equal.
    - '0' indicates they are different.
    - If one string is shorter, the output is padded with '0's on the right.
    """

    if not isinstance(number_a, str) or not isinstance(number_b, str):
        raise TypeError("Both inputs must be strings")

    result = ""

    shortest = min(len(number_a), len(number_b))
    longest = max(len(number_a), len(number_b))

    for i in range(shortest):
        if number_a[i] == number_b[i]:
            result += "1"
        else:
            result += "0"

    result += "0" * (longest - shortest)

    return result