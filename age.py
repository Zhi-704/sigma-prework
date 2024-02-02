'''
When given a date, calculates the age between the current dat and the given date.
'''

from datetime import datetime

def main():
    user_input = input('Please give a date in format (DD-MM-YYYY): ')
    caclculate_date(user_input)
    return

def caclculate_date(user_input):
    try:
        formatted_date = datetime.strptime(user_input, "%d-%m-%Y")
        difference = datetime.now().year - formatted_date.year
        if (datetime.now().month, datetime.now().day) < (formatted_date.month, formatted_date.day):
          difference -= 1
        print(difference)
    except ValueError:
        print("Error Formatting User Input. Please Try Again.")
    return

if __name__ == '__main__':
    main()