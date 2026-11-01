# Task 1

from datetime import datetime


def get_days_from_today(date):
    """
    Calculates the number of days between the given date and today.

    Args:
        date (str): Date in YYYY-MM-DD format.

    Returns:
        int: Number of days between the given date and today.
    """
    try:
        # Convert the string into a date object
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Get today's date
        today = datetime.today().date()

        # Calculate the difference between dates
        difference = today - given_date

        # Return the difference in days
        return difference.days

    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."


# Test the function
print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-11-05"))
print(get_days_from_today("hello"))



# Task 2

import random


def get_numbers_ticket(min, max, quantity):
    """
    Generate a set of unique random lottery numbers.

    Args:
        min (int): Minimum possible number.
        max (int): Maximum possible number.
        quantity (int): Number of random numbers to generate.

    Returns:
        list: Sorted list of unique random numbers.
              Returns an empty list if parameters are invalid.
    """

    # Check if parameters are valid
    if not all(isinstance(value, int) and not isinstance(value, bool)
               for value in (min, max, quantity)):
        return []

    if min < 1 or max > 1000 or min >= max:
        return []

    if quantity < 1 or quantity > (max - min + 1):
        return []

    # Generate unique random numbers
    numbers = random.sample(range(min, max + 1), quantity)

    # Sort numbers in ascending order
    return sorted(numbers)


# Test the function

lottery_numbers = get_numbers_ticket(1, 49, 6)

print("Your lottery numbers:", lottery_numbers)

# Test invalid parameters
print(get_numbers_ticket(0, 49, 6))
print(get_numbers_ticket(1, 49, 60))
print(get_numbers_ticket(1, 1001, 6))
print(get_numbers_ticket("1", 49, 6))



# Task 3

import re


def normalize_phone(phone_number):
    """
    Normalize a phone number to the international Ukrainian format.

    Args:
        phone_number (str): Phone number in any format.

    Returns:
        str: Normalized phone number starting with +380.
    """

    # Remove all characters except digits and plus sign
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # Check if the number starts with +380
    if cleaned_number.startswith("+380"):
        return cleaned_number

    # Check if the number starts with 380
    elif cleaned_number.startswith("380"):
        return "+" + cleaned_number

    # Check if the number starts with +38
    elif cleaned_number.startswith("+38"):
        return cleaned_number

    # Add Ukrainian country code if it is missing
    else:
        return "+38" + cleaned_number


# Test the function

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Normalized phone numbers:", sanitized_numbers)


# Task 4

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    """
    Find users who have birthdays within the next 7 days.

    If a birthday falls on a weekend, move the
    congratulation date to the next Monday.

    Args:
        users (list): List of dictionaries with names and birthdays.

    Returns:
        list: List of users with their congratulation dates.
    """

    # Get today's date
    today = datetime.today().date()

    # Create an empty list for upcoming birthdays
    upcoming_birthdays = []

    # Check every user in the list
    for user in users:

        # Convert birthday string into a date object
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        # Create birthday date for the current year
        birthday_this_year = birthday.replace(year=today.year)

        # If birthday has already passed, use next year
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Calculate the number of days until the birthday
        days_until_birthday = (birthday_this_year - today).days

        # Check if birthday is within the next 7 days
        if 0 <= days_until_birthday <= 7:

            # Set the congratulation date
            congratulation_date = birthday_this_year

            # If birthday is on Saturday, move to Monday
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            # If birthday is on Sunday, move to Monday
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Add user and congratulation date to the result
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays



# Test the function

users = [
    {"name": "John Doe", "birthday": "1990.11.01"},
    {"name": "Jane Smith", "birthday": "1995.11.07"},
    {"name": "Alex Brown", "birthday": "1992.11.08"},
    {"name": "Mike Wilson", "birthday": "1988.11.10"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Upcoming birthdays:", upcoming_birthdays)
